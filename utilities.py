import sys
from pathlib import Path

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel


# Get absolute path of resource (works both for dev and PyInstaller)
def resource_path(relative_path: str):
    base_path = Path(getattr(sys, '_MEIPASS', Path(sys.argv[0]).resolve().parent))
    return base_path / relative_path


# Custom QLabel with mouse click event
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, _):
        self.clicked.emit()