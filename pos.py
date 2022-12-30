import sys

# 3rd party imports
import qdarktheme
from PyQt6.QtWidgets import QApplication

# Local imports
from main_window import MainWindow

if __name__ == '__main__':
    import cgitb
    cgitb.enable(format='text')

    # Initialize Qt sys
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()

    # Create instance of main control class
    instance = MainWindow()

    # Start by showing the main window
    instance.show()
    instance.activateWindow()
    instance.showFullScreen()

    # Execute and close on end on program exit
    sys.exit(app.exec())
