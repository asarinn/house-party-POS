import sys

# 3rd party imports
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox

# Local imports
from main_window_init import Ui_main_window
from patron import Patron


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Basic pyqt init for gui window
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.patron: list[Patron] = []
        self.active_patron: Patron | None = None

        self.ui.new_user_button.pressed.connect(self.add_user)
        self.ui.settle_up_button.pressed.connect(self.settle_up)

    # Add user from GUI
    def add_user(self):
        text, ok = QInputDialog().getText(self, 'Add a Patron',
                                          "Please enter a unique name for tracking your purchases.\nPatron Name:")
        if ok:
            # TODO(from Mike): Check if given name already exists in the database, popup and return if yes

            # TODO(from Mike) Add new user to database

            new_patron = Patron(text)
            self.patron.append(new_patron)
            self.active_patron = new_patron

    # On database connect, load in existing users
    def load_users(self):
        self.patron = []
        # TODO(from Mike): Fill in the users list from the database
        pass

    def settle_up(self):
        msg = QMessageBox(QMessageBox.Icon.Critical, 'Settle Up Confirmation', 'WAIT!\nOnly press apply if you have already paid Mike')
        msg.addButton(QMessageBox.StandardButton.Abort)
        msg.addButton(QMessageBox.StandardButton.Apply)
        response = msg.exec()

        if response == QMessageBox.StandardButton.Apply:
            self.active_patron.settle_up()


if __name__ == '__main__':
    # Initialize Qt sys
    app = QApplication(sys.argv)
    app.setStyle("fusion")

    # Create instance of main control class
    instance = MainWindow()

    # Start by showing the main window
    instance.show()
    instance.activateWindow()
    # TODO(from Mike): Re-enable this after major development complete
    # instance.showMaximized()

    # Execute and close on end on program exit
    sys.exit(app.exec())
