import json
import math
import time
import urllib
import warnings
from datetime import datetime
from functools import partial
from pathlib import Path
from random import choice
from urllib.parse import urljoin
import os
import urllib.request
import tempfile

# 3rd party imports
import requests
from PyQt6 import QtCore, QtWidgets, QtGui
from colorhash import ColorHash
from PyQt6.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QWidget, QPushButton, QScroller
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QUrl, QSize, QBuffer, QByteArray
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PIL import Image
from PIL.ImageQt import ImageQt
from requests import ConnectTimeout

# Local imports
from .main_window_init import Ui_main_window
from drink_template import Ui_drink_template
from tab_row_template import Ui_tab_row_template
from cart_row_template import Ui_cart_row_template
from settle_up_dialog import SettleUpDialog
from utilities import resource_path
from patron import Patron
from drink import Drink
from order import Order, OrderItem

API_URL = 'http://192.168.1.9/api/'
DRINK_COLUMNS = 4
PATRON_COLUMNS = 8
DEFAULT_SPIRAL_SHELLS = 7
DEBUG = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic pyqt init for gui window
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.settle_up_dialog = SettleUpDialog(self)

        # Sound player
        self.player = QMediaPlayer()
        self.output = QAudioOutput()
        self.player.setAudioOutput(self.output)
        self.output.setVolume(50)
        self.sound_files = [f.as_posix() for f in resource_path('sounds').glob('*.mp3')]

        self.patrons: list[Patron] = []
        self.cart: OrderItem = []
        self._active_patron: Patron | None = None

        self.ui.new_patron_button.clicked.connect(self.add_patron)
        self.ui.settle_up_button.clicked.connect(self.settle_up)
        self.ui.back_to_patrons_button.clicked.connect(self.back_to_patrons)
        self.ui.add_to_tab_button.clicked.connect(self.add_to_tab)
        self.ui.clear_cart_button.clicked.connect(self.clear_cart)

        # Need these as instance variables to avoid garbage collection
        self.movie: QtGui.QMovie | None = None
        self.temp_dir: tempfile.TemporaryDirectory | None = None

        if not DEBUG:
            # Grab scroll area gesture for single finger scroll
            QScroller.grabGesture(self.ui.scrollArea.viewport(), QScroller.ScrollerGestureType.TouchGesture)
            QScroller.grabGesture(self.ui.scrollArea_2.viewport(), QScroller.ScrollerGestureType.TouchGesture)
            QScroller.grabGesture(self.ui.scrollArea_3.viewport(), QScroller.ScrollerGestureType.TouchGesture)

        # Load from database
        self.load_patrons()
        self.load_drinks()

    ####################################################################################################################
    # Patron
    ####################################################################################################################

    @property
    def active_patron(self) -> Patron:
        return self._active_patron

    @active_patron.setter
    def active_patron(self, patron: Patron):
        self._active_patron = patron
        self.clear_cart()
        self.update_tab()

    def patron_clicked(self, patron: Patron):
        self.active_patron = patron
        self.ui.stacked_widget.setCurrentIndex(1)
        self.ui.patron_name_label.setText(patron.name)

    def back_to_patrons(self):
        self.ui.stacked_widget.setCurrentIndex(0)
        self.ui.tab_widget.setCurrentIndex(0)

    # Load in existing patrons from the database
    def load_patrons(self):
        # Fetch patrons
        url = urljoin(API_URL, 'patrons')
        try:
            request = requests.get(url)
        except ConnectTimeout:
            warnings.warn("Database connection timed out")
            return

        for i, patron_json in enumerate(request.json()):
            # Construct Order objects
            orders = []
            for order_json in patron_json['orders']:
                orders.append(self.create_order(order_json))

            patron_json['orders'] = orders
            patron = Patron(**patron_json)
            self.patrons.append(patron)

            self.add_patron_to_gui(patron, i)

    # Add new patron from GUI
    def add_patron(self):
        name, ok = QInputDialog().getText(self, 'Add a Patron', "Please enter your full name:")
        if ok:
            if name in [p.name for p in self.patrons]:
                QMessageBox(QMessageBox.Icon.Critical, 'Duplicate Patron Name',
                            'The desired name already exists, please try again.').exec()
                return

            url = urljoin(API_URL, 'patrons')
            response = requests.post(url, data={'name': name})
            patron = Patron(**response.json())

            self.patrons.append(patron)

            self.add_patron_to_gui(patron, len(self.patrons) - 1)

            # Select newly added patron
            self.patron_clicked(patron)

    def add_patron_to_gui(self, patron: Patron, num_patrons: int):
        # Get new user button and move it to next grid cell
        new_x, new_y = self.get_new_patron_grid_cell(num_patrons + 1)
        self.ui.new_patron_button.setParent(None)
        self.ui.patron_selection_layout.addWidget(self.ui.new_patron_button, new_y, new_x)

        # Create new button
        patron_button = QPushButton()
        font = patron_button.font()
        font.setPointSize(36)
        patron_button.setFont(font)

        # Get the scaling to behave and have uniform buttons even with pictures
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        patron_button.setSizePolicy(sizePolicy)

        # OK I give up
        patron_button.setMinimumSize(150, 150)
        patron_button.setMaximumSize(150, 150)

        # If the user has a picture use that, otherwise use initials and color
        self.set_patron_icon(patron, patron_button)

        # Connect button press to change active user
        patron_button.clicked.connect(lambda: self.patron_clicked(patron))

        # Setup context menu
        patron_button.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        patron_button.customContextMenuRequested.connect(lambda: self.patron_button_context_menu(patron, patron_button))

        # Add new button to gui
        patron_x, patron_y = self.get_new_patron_grid_cell(num_patrons)
        self.ui.patron_selection_layout.addWidget(patron_button, patron_y, patron_x)

    def set_patron_icon(self, patron: Patron, patron_button: QPushButton):
        if patron.photo:
            if ".gif" in patron.photo:
                # Create temporary directory
                self.temp_dir = tempfile.TemporaryDirectory()
                gif_file_path = Path(self.temp_dir.name) / "temp.gif"

                # Download the gif file
                response = requests.get(patron.photo)
                response.raise_for_status()  # Ensure we got a successful response

                # Write the content of the response to a new file in the temporary directory
                gif_file_path.write_bytes(response.content)

                self.movie = QtGui.QMovie()
                self.movie.setFileName(str(gif_file_path))
                self.movie.setCacheMode(QtGui.QMovie.CacheMode.CacheAll)
                self.movie.frameChanged.connect(lambda: patron_button.setIcon(QIcon(self.movie.currentPixmap())))
                self.movie.start()
            else:
                response = requests.get(patron.photo)
                response.raise_for_status()  # Ensure we got a successful response

                image = QtGui.QImage()
                image.loadFromData(response.content)
                pixmap = QtGui.QPixmap(image)
                patron_button.setIcon(QIcon(pixmap))
            patron_button.setIconSize(patron_button.size())
        else:
            # Set button color based on patron name
            color = ColorHash(patron.name)
            patron_button.setStyleSheet(f'background-color: {color.hex}; color: #202124')

            # Extract initials from patron name
            initials = ''.join([x[0] for x in patron.name.split(' ')]).upper()
            patron_button.setText(initials)

    def patron_button_context_menu(self, patron, patron_button):
        menu = QtWidgets.QMenu()
        edit_patron_action = menu.addAction('Edit Patron')
        remove_patron_action = menu.addAction('Remove Patron')
        add_picture_action = menu.addAction('Add Picture')
        res = menu.exec(QtGui.QCursor.pos())
        if res == edit_patron_action:
            self.edit_patron(patron, patron_button)
        elif res == remove_patron_action:
            return
            self.remove_patron(patron, patron_button)
        elif res == add_picture_action:
                self.add_picture(patron, patron_button)

    def edit_patron(self, patron, patron_button):
        name, ok = QInputDialog().getText(self, 'Edit Patron', "Please enter the new name:",
                                          text=patron.name)
        if ok and patron.name.lower() != "benchj":
            if name in [p.name for p in self.patrons]:
                QMessageBox(QMessageBox.Icon.Critical, 'Duplicate Patron Name',
                            'The desired name already exists, please try again.').exec()
                return

            url = urljoin(API_URL, f'patrons/{patron.id}')
            response = requests.patch(url, data={'name': name})

            patron.name = name

            # Extract initials from patron name
            initials = ''.join([x[0] for x in patron.name.split(' ')]).upper()
            patron_button.setText(initials)

    def remove_patron(self, patron, patron_button):
        reply = QMessageBox.question(self, 'Remove Patron',
                                     'Are you sure you want to remove patron from the database?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            url = urljoin(API_URL, f'patrons/{patron.id}')
            response = requests.delete(url)

            if response.status_code == 204 and patron.name.lower() != "benchj":
                self.patrons.remove(patron)
                patron_button.setParent(None)
            else:
                QMessageBox(QMessageBox.Icon.Critical, 'Delete Error',
                            'An error occurred while trying to delete the patron. Please try again.').exec()

    def add_picture(self, patron, patron_button):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            with open(file_path, 'rb') as file:
                url = urljoin(API_URL, f'patrons/{patron.id}')
                response = requests.post(url, data={'photo': file})
                if response.status_code == 200:
                    patron.photo = response.json()['photo']
                    self.set_patron_icon(patron, patron_button)
                else:
                    QMessageBox(QMessageBox.Icon.Critical, 'Upload Error',
                                'An error occurred while trying to upload the picture. Please try again.').exec()

    def settle_up(self):
        # Update order total
        self.settle_up_dialog.ui.total_label.setText(f'Total: ${self.active_patron.active_order.total:.2f}')

        settled = self.settle_up_dialog.exec()
        if settled:
            order_id = self.active_patron.active_order.id
            url = urljoin(API_URL, f'orders/{order_id}')
            requests.patch(url, data={'settled': True})

            self.active_patron.active_order.settled = True

            self.back_to_patrons()

    def get_new_patron_grid_cell(self, num_patrons: int) -> (int, int):
        direction_names = ['right', 'down', 'left', 'up']
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        final_direction = (0, 0)

        direction = 0
        side_length = 1
        side_position = 0
        turns_this_length = 0

        for i in range(num_patrons):
            next_direction = directions[direction]
            final_direction = tuple(map(sum, zip(final_direction, next_direction)))

            side_position += 1
            if side_position == side_length:
                direction += 1
                turns_this_length += 1
                side_position = 0

            if turns_this_length == 2:
                side_length += 1
                turns_this_length = 0

            if direction == 4:
                direction = 0

        return final_direction[0] + DEFAULT_SPIRAL_SHELLS, final_direction[1] + DEFAULT_SPIRAL_SHELLS

    ####################################################################################################################
    # Cart
    ####################################################################################################################

    def increase_item_quantity(self, item: OrderItem):
        item.quantity += 1

        # Update labels
        item.ui.quantity_label.setText(str(item.quantity))
        item.ui.total_label.setText(f'${item.total:.2f}')
        self.update_cart_total()

        if item.quantity > 1:
            item.ui.decrease_quantity_button.setEnabled(True)

    def decrease_item_quantity(self, item: OrderItem):
        item.quantity -= 1

        # Update labels
        item.ui.quantity_label.setText(str(item.quantity))
        item.ui.total_label.setText(f'${item.total:.2f}')
        self.update_cart_total()

        if item.quantity == 1:
            item.ui.decrease_quantity_button.setEnabled(False)

    def add_to_cart(self, drink: Drink):
        for item in self.cart:
            if item.drink == drink.name:
                self.increase_item_quantity(item)
                return

        item = OrderItem(len(self.cart), drink.name, drink.price, 1)
        self.cart.append(item)

        cart_row_widget = QWidget()
        cart_row_ui = Ui_cart_row_template()
        cart_row_ui.setupUi(cart_row_widget)

        # Populate labels from information
        cart_row_ui.name_label.setText(item.drink)
        cart_row_ui.cost_label.setText(f'${item.price:.2f}')
        cart_row_ui.total_label.setText(f'${item.total:.2f}')

        # Connect UI
        cart_row_ui.remove_button.clicked.connect(lambda: self.remove_from_cart(item))
        cart_row_ui.increase_quantity_button.clicked.connect(lambda: self.increase_item_quantity(item))
        cart_row_ui.decrease_quantity_button.clicked.connect(lambda: self.decrease_item_quantity(item))

        # Add widget to layout
        self.ui.cart_layout.addWidget(cart_row_widget)

        # Add UI to item for convenience
        item.ui = cart_row_ui

        # Update cart total
        self.update_cart_total()

        # Enable Add to Tab and Clear Cart buttons
        self.ui.add_to_tab_button.setEnabled(True)
        self.ui.clear_cart_button.setEnabled(True)

        # Show cart
        self.set_cart_visible(True)

    def update_cart_total(self):
        total = sum(i.total for i in self.cart)
        self.ui.cart_total_label.setText(f'Cart Total: ${total:.2f}')

    def remove_from_cart(self, item: OrderItem):
        index = self.cart.index(item)
        self.cart.pop(index)
        self.ui.cart_layout.itemAt(index).widget().setParent(None)

        self.update_cart_total()

        # If cart is empty, hide cart
        if not self.cart:
            self.set_cart_visible(False)

    def clear_cart(self):
        self.cart.clear()

        # Clear widgets in cart layout
        for i in reversed(range(self.ui.cart_layout.count())):
            self.ui.cart_layout.itemAt(i).widget().setParent(None)

        # Reset cart total
        self.ui.cart_total_label.setText('Cart Total: $0.00')

        # Disable Add to Tab and Clear Cart buttons
        self.ui.add_to_tab_button.setEnabled(False)
        self.ui.clear_cart_button.setEnabled(False)

        # Hide cart
        self.set_cart_visible(False)

    def set_cart_visible(self, visible: bool):
        self.ui.cart_frame.setVisible(visible)

    ####################################################################################################################
    # Tab
    ####################################################################################################################

    def add_to_tab(self):
        order_id = self.active_patron.active_order.id
        order_items = []
        for item in self.cart:
            order_items.append({'drink': item.drink, 'quantity': item.quantity})

        data = json.dumps({'order_items': order_items})
        headers = {'content-type': 'application/json'}
        url = urljoin(API_URL, f'orders/{order_id}')
        request = requests.patch(url, data=data, headers=headers)
        order = self.create_order(request.json())
        self.active_patron.active_order = order

        # Play random soundbyte
        sound = choice(self.sound_files)
        path = QUrl.fromLocalFile(sound)
        self.player.setSource(path)
        self.player.play()

        self.update_tab()
        self.clear_cart()
        self.ui.tab_widget.setCurrentIndex(1)

    def update_tab(self):
        for i in reversed(range(self.ui.tab_layout.count())):
            self.ui.tab_layout.itemAt(i).widget().setParent(None)

        order = self.active_patron.active_order
        if order is None:
            # If active order does not exist, create new order
            url = urljoin(API_URL, 'orders')
            request = requests.post(url, data={'patron': self.active_patron.name})
            order = Order(**request.json())
            self.active_patron.orders.append(order)

        self.ui.settle_up_button.setEnabled(False)
        order.total = 0

        for item in order.order_items:
            tab_row_widget = QWidget()
            tab_row_ui = Ui_tab_row_template()
            tab_row_ui.setupUi(tab_row_widget)

            # Populate labels from information
            tab_row_ui.name_label.setText(item.drink)
            tab_row_ui.cost_label.setText(f'${(item.total / item.quantity):.2f}')
            tab_row_ui.quantity_label.setText(str(item.quantity))
            tab_row_ui.total_label.setText(f'${item.total:.2f}')

            # Connect UI
            tab_row_ui.remove_button.clicked.connect(partial(self.remove_from_tab, item))

            # Add widget to layout
            self.ui.tab_layout.addWidget(tab_row_widget)

            # Enable settle up button
            self.ui.settle_up_button.setEnabled(True)

            # Update order total
            order.total += item.total

        self.ui.tab_total_label.setText(f'Total: ${order.total:.2f}')

    def remove_from_tab(self, item: OrderItem):
        url = urljoin(API_URL, f'order_items/{item.id}')
        requests.delete(url)
        self.active_patron.active_order.order_items.remove(item)
        self.update_tab()

    def create_order(self, order_json: dict) -> Order:
        items = []
        for item_json in order_json['order_items']:
            price = item_json['total'] / item_json['quantity']
            item = OrderItem(item_json['id'], item_json['drink'], price, item_json['quantity'])
            items.append(item)

        order_json['order_items'] = items
        order_json['created'] = datetime.fromisoformat(order_json['created'])

        return Order(**order_json)

    ####################################################################################################################
    # Drink Menu
    ####################################################################################################################

    def add_drink_to_menu(self, drink: Drink, x: int, y: int):
        # Init new widget from template
        drink_widget = QWidget()
        drink_ui = Ui_drink_template()
        drink_ui.setupUi(drink_widget)

        # Resize photo to template size
        photo = drink.photo.scaled(
            drink_widget.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        # Populate labels from information
        drink_ui.photo_label.setPixmap(QPixmap.fromImage(photo))
        drink_ui.name_label.setText(drink.name)
        drink_ui.price_label.setText(f'${drink.price:.2f}')

        # Connect UI
        drink_ui.add_to_cart_button.clicked.connect(lambda: self.add_to_cart(drink))
        # drink_ui.photo_button.clicked.connect(lambda: self.add_to_cart(drink))

        # Add widget to layout
        self.ui.menu_grid_layout.addWidget(drink_widget, x, y)

    def load_drinks(self):
        # Fetch drinks
        # TODO(brett): error handling on request
        url = urljoin(API_URL, 'drinks')
        try:
            request = requests.get(url)
        except ConnectTimeout:
            warnings.warn("Database connection timed out")
            return

        # Populate drink menu
        drinks_json = [d for d in request.json() if d['in_stock']]
        for i, drink_json in enumerate(drinks_json):
            # Create image object
            request = requests.get(drink_json['photo'], stream=True)
            drink_json['photo'] = ImageQt(Image.open(request.raw))

            # Construct drink object
            drink = Drink(**drink_json)

            self.add_drink_to_menu(drink, i // DRINK_COLUMNS, i % DRINK_COLUMNS)
