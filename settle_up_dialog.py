from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap

from settle_up_dialog_init import Ui_settle_up_dialog


class SettleUpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Basic pyqt init for gui window
        self.ui = Ui_settle_up_dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Load QR code
        #width = self.width() // 2
        image = QImage('venmo_qrcode.png')
        self.ui.qr_code_label.setPixmap(QPixmap.fromImage(image))

        # Connect buttons
        self.ui.button_box.accepted.connect(self.accept)
        self.ui.button_box.rejected.connect(self.reject)

    def settle_up(self):
       print('accepted')
       self.accept()

    def cancel(self):
       print('rejected')
       self.reject()
