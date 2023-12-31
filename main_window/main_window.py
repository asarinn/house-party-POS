import json
from datetime import datetime
from functools import partial
from random import choice
from urllib.parse import urljoin

# 3rd party imports
import requests
from colorhash import ColorHash
from PyQt6.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QWidget, QPushButton, QScroller
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PIL import Image
from PIL.ImageQt import ImageQt

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

        if not DEBUG:
            # Grab scroll area gesture for single finger scroll
            QScroller.grabGesture(self.ui.scrollArea.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)
            QScroller.grabGesture(self.ui.scrollArea_2.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)
            QScroller.grabGesture(self.ui.scrollArea_3.viewport(), QScroller.ScrollerGestureType.LeftMouseButtonGesture)

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
        self.ui.scrollArea.setFocus()

    def back_to_patrons(self):
        self.ui.stacked_widget.setCurrentIndex(0)
        self.ui.tab_widget.setCurrentIndex(0)

    # Load in existing patrons from the database
    def load_patrons(self):
        # Fetch patrons
        # TODO(brett): error handling on request
        url = urljoin(API_URL, 'patrons')
        request = requests.get(url)

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
        patron_x, patron_y = self.get_patron_grid_cell(num_patrons)

        # Get new user button and move it to next grid cell
        new_x, new_y = self.get_patron_grid_cell(num_patrons + 1)
        new_user_button = self.ui.patron_layout.itemAtPosition(patron_x, patron_y).widget()
        new_user_button.setParent(None)
        self.ui.patron_layout.addWidget(new_user_button, new_x, new_y)

        # Create new button
        patron_button = QPushButton()
        font = patron_button.font()
        font.setPointSize(32)
        patron_button.setFont(font)
        patron_button.setMinimumSize(150, 150)

        # Set button color based on patron name
        color = ColorHash(patron.name)
        patron_button.setStyleSheet(f'background-color: {color.hex}; color: #202124')

        # Extract initials from patron name
        initials = ''.join([x[0] for x in patron.name.split(' ')]).upper()
        patron_button.setText(initials)

        # Connect button press to change active user
        patron_button.clicked.connect(lambda: self.patron_clicked(patron))

        # Add button to gui (+1 to compensate for add button)
        self.ui.patron_layout.addWidget(patron_button, patron_x, patron_y)

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

    def get_patron_grid_cell(self, num_patrons: int) -> (int, int):
        return num_patrons // PATRON_COLUMNS, num_patrons % PATRON_COLUMNS

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
        drink_ui.photo_label.clicked.connect(lambda: self.add_to_cart(drink))

        # Add widget to layout
        self.ui.menu_grid_layout.addWidget(drink_widget, x, y)

    def load_drinks(self):
        # Fetch drinks
        # TODO(brett): error handling on request
        url = urljoin(API_URL, 'drinks')
        request = requests.get(url)

        # Populate drink menu
        drinks_json = [d for d in request.json() if d['in_stock']]
        for i, drink_json in enumerate(drinks_json):
            # Create image object
            request = requests.get(drink_json['photo'], stream=True)
            drink_json['photo'] = ImageQt(Image.open(request.raw))

            # Construct drink object
            drink = Drink(**drink_json)

            self.add_drink_to_menu(drink, i // DRINK_COLUMNS, i % DRINK_COLUMNS)
