import sys

# 3rd party imports
from PyQt6.QtWidgets import QApplication, QMainWindow

# Local imports
from main_window_init import Ui_main_window


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Basic pyqt init for gui window
        self.ui = Ui_main_window()
        self.ui.setupUi(self)


if __name__ == '__main__':
    # Initialize Qt sys
    app = QApplication(sys.argv)
    app.setStyle("fusion")

    # Create instance of main control class
    instance = MainWindow()

    # Start by showing the main window
    instance.show()
    instance.activateWindow()
    instance.showMaximized()

    # Execute and close on end on program exit
    sys.exit(app.exec())
