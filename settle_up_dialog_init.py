# Form implementation generated from reading ui file '.\settle_up_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_settle_up_dialog(object):
    def setupUi(self, settle_up_dialog):
        settle_up_dialog.setObjectName("settle_up_dialog")
        settle_up_dialog.resize(1280, 960)
        settle_up_dialog.setStyleSheet("QDialog {\n"
"    border: 1px solid #424242;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(settle_up_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(settle_up_dialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.qr_code_label = QtWidgets.QLabel(settle_up_dialog)
        self.qr_code_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qr_code_label.setObjectName("qr_code_label")
        self.verticalLayout.addWidget(self.qr_code_label)
        self.label_3 = QtWidgets.QLabel(settle_up_dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: red")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.button_box = QtWidgets.QDialogButtonBox(settle_up_dialog)
        self.button_box.setStyleSheet("padding: 15px 20px;\n"
"font-size: 16pt")
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.button_box.setCenterButtons(True)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(settle_up_dialog)
        QtCore.QMetaObject.connectSlotsByName(settle_up_dialog)

    def retranslateUi(self, settle_up_dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("settle_up_dialog", "@Michael-Proemsey"))
        self.label_3.setText(_translate("settle_up_dialog", "Please select OK only after you\'ve paid!"))
