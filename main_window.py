import sys

# 3rd party imports
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox, QWidget, QPushButton
from PyQt6 import QtCore, QtGui

# Local imports
from main_window_init import Ui_main_window
from drink_template_init import Ui_drink_template
from tab_row_template_init import Ui_tab_row_template
from patron import Patron
from drink import Drink


class MainWindow(QMainWindow):
    DEFAULT_DRINK_COLUMNS = 5

    def __init__(self):
        super().__init__()

        # Basic pyqt init for gui window
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.patrons: list[Patron] = []
        self._active_patron: Patron | None = None

        self.ui.new_user_button.pressed.connect(self.add_user)
        self.ui.settle_up_button.pressed.connect(self.settle_up)

        # TODO(from mike): replace this with server connection, and initialize from database
        drinks = [['test drink name', 10.00, 'test drinks sure cost a lot']] * 13

        # Populate drink menu
        for i, drink in enumerate(drinks):
            self.add_drink_to_menu(drink[0], drink[1], drink[2], int(i/self.DEFAULT_DRINK_COLUMNS),
                                   i % self.DEFAULT_DRINK_COLUMNS)

    @property
    def active_patron(self):
        return self._active_patron

    @active_patron.setter
    def active_patron(self, value):
        try:
            self._active_patron.button.setStyleSheet('')
        except AttributeError:  # If active patron doesn't exist yet
            pass

        self._active_patron = value
        self._active_patron.button.setStyleSheet('background-color: green')

    def patron_clicked(self, patron):
        self.active_patron = patron
        self.update_tab()

    def drink_removed(self, drink, quantity):
        self.active_patron.remove_drink(drink, quantity)

    def update_tab(self):
        for i in reversed(range(self.ui.tab_layout.count())):
            self.ui.tab_layout.itemAt(i).widget().setParent(None)

        total = 0
        for drink, quantity in self.active_patron.drinks:
            # Init new widget from template
            tab_row_widget = QWidget()
            tab_row_ui = Ui_tab_row_template()
            tab_row_ui.setupUi(tab_row_widget)

            # Populate labels from information
            tab_row_ui.drink_name_label.setText(drink.name)
            tab_row_ui.drink_cost_label.setText(f'Price: {drink.price:.2f}')
            tab_row_ui.drink_quantity_label.setText(str(quantity))

            # Connect UI
            tab_row_ui.remove_button.pressed.connect(lambda: self.drink_removed(drink, quantity))

            # Add widget to layout
            self.ui.tab_layout.addWidget(tab_row_widget)

            # Calculate total
            total += drink.price * quantity

        self.ui.total_label.setText(f'Total: {total}')

    def add_drink_to_menu(self, name: str, price: float, description: str, x: int, y: int):
        # Init new widget from template
        drink_widget = QWidget()
        drink_ui = Ui_drink_template()
        drink_ui.setupUi(drink_widget)

        # Populate labels from information
        drink_ui.drink_name_label.setText(name)
        drink_ui.drink_description_label.setText(description)
        drink_ui.price_label.setText(f'{price:.2f}')

        # Create drink object
        drink = Drink(name, price)

        # Connect UI
        drink_ui.add_to_tab_button.pressed.connect(
            lambda: self.add_drink_to_patron(drink, drink_ui.quantity_spin_box.value()))

        # Add widget to layout
        self.ui.menu_grid_layout.addWidget(drink_widget, x, y)

    def add_drink_to_patron(self, drink: Drink, quantity: int):
        try:
            self.active_patron.add_drink(drink, quantity)
        except AttributeError:
            QMessageBox(QMessageBox.Icon.Critical, 'No Patron Selected',
                        'Please select yourself from the top bar or add new patron if needed').exec()
            return

        self.update_tab()

    # Add user from GUI
    def add_user(self):
        text, ok = QInputDialog().getText(self, 'Add a Patron',
                                          "Please enter a unique name for tracking your purchases.\nPatron Name:")
        if ok:
            # TODO(from Mike): Check if given name already exists in the database, popup and return if yes

            # TODO(from Mike) Add new user to database

            new_patron = Patron(text)
            self.patrons.append(new_patron)
            self.add_patron_to_gui(new_patron)
            self.active_patron = new_patron

    # On database connect, load in existing users
    def load_users(self):
        self.patrons = []
        # TODO(from Mike): Fill in the users list from the database
        pass

    def add_patron_to_gui(self, patron: Patron):
        # Create new button
        user_button = QPushButton()
        font = QtGui.QFont()
        font.setPointSize(24)
        user_button.setFont(font)
        user_button.setMinimumSize(QtCore.QSize(75, 75))

        # Extract initials from patron name
        try:
            initials = [x[0] for x in patron.name.split(' ')]
            initials_str = ''
            for initial in initials:
                initials_str += initial
            user_button.setText(initials_str)
        except IndexError:
            QMessageBox(QMessageBox.Icon.Critical, 'Invalid Patron Name',
                        'The suggested name format is:\n "First Last"').exec()
            return

        # Connect button press to change active user
        user_button.pressed.connect(lambda: self.patron_clicked(patron))

        # Add to gui
        self.ui.patron_layout.addWidget(user_button)

        # Add to patron object
        patron.button = user_button

    def settle_up(self):
        msg = QMessageBox(QMessageBox.Icon.Critical, 'Settle Up Confirmation',
                          'WAIT!\nOnly press apply if you have already paid Mike')
        msg.addButton(QMessageBox.StandardButton.Abort)
        msg.addButton(QMessageBox.StandardButton.Apply)
        response = msg.exec()

        if response == QMessageBox.StandardButton.Apply:
            self.active_patron.settle_up()

        self.update_tab()


if __name__ == '__main__':
    import cgitb
    cgitb.enable(format='text')

    # Initialize Qt sys
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    app.setStyleSheet("""
    QSpinBox::down-button{
        width: 75
    }
    QSpinBox::up-button{
        width: 75
    }""")

    # Create instance of main control class
    instance = MainWindow()

    # Start by showing the main window
    instance.show()
    instance.activateWindow()
    # TODO(from Mike): Re-enable this after major development complete
    # instance.showMaximized()

    # Execute and close on end on program exit
    sys.exit(app.exec())
