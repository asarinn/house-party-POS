# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1600, 900)
        main_window.setBaseSize(QtCore.QSize(1600, 900))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 251, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(124, 124, 124))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        main_window.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setBaseSize(QtCore.QSize(1850, 1000))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_user_button.setMinimumSize(QtCore.QSize(75, 75))
        self.new_user_button.setObjectName("new_user_button")
        self.horizontalLayout.addWidget(self.new_user_button)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.menu_tab = QtWidgets.QWidget()
        self.menu_tab.setObjectName("menu_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.menu_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.menu_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.menu_grid_layout = QtWidgets.QGridLayout()
        self.menu_grid_layout.setObjectName("menu_grid_layout")
        self.verticalLayout_2.addLayout(self.menu_grid_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.menu_tab, "")
        self.tab_tab = QtWidgets.QWidget()
        self.tab_tab.setObjectName("tab_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tab_tab)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.tab_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.settle_up_button = QtWidgets.QPushButton(self.tab_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.settle_up_button.setFont(font)
        self.settle_up_button.setObjectName("settle_up_button")
        self.verticalLayout_4.addWidget(self.settle_up_button)
        self.tabWidget.addTab(self.tab_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        main_window.setMenuBar(self.menubar)
        self.actionOsilloscope_Setup = QtGui.QAction(main_window)
        self.actionOsilloscope_Setup.setObjectName("actionOsilloscope_Setup")
        self.actionPulser_Setup = QtGui.QAction(main_window)
        self.actionPulser_Setup.setObjectName("actionPulser_Setup")
        self.actionLeakage_Setup = QtGui.QAction(main_window)
        self.actionLeakage_Setup.setObjectName("actionLeakage_Setup")
        self.actionBias_Setup = QtGui.QAction(main_window)
        self.actionBias_Setup.setObjectName("actionBias_Setup")
        self.actionProbe_Station_Setup = QtGui.QAction(main_window)
        self.actionProbe_Station_Setup.setObjectName("actionProbe_Station_Setup")
        self.actionStandard_TLP = QtGui.QAction(main_window)
        self.actionStandard_TLP.setObjectName("actionStandard_TLP")
        self.actionVF_TLP_TDR_S = QtGui.QAction(main_window)
        self.actionVF_TLP_TDR_S.setObjectName("actionVF_TLP_TDR_S")
        self.actionSave_Settings = QtGui.QAction(main_window)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionLoad_Settings = QtGui.QAction(main_window)
        self.actionLoad_Settings.setObjectName("actionLoad_Settings")
        self.actionStop_Criteria = QtGui.QAction(main_window)
        self.actionStop_Criteria.setObjectName("actionStop_Criteria")
        self.actionCalibration_Setup = QtGui.QAction(main_window)
        self.actionCalibration_Setup.setObjectName("actionCalibration_Setup")
        self.actionCalibration_Wizard = QtGui.QAction(main_window)
        self.actionCalibration_Wizard.setObjectName("actionCalibration_Wizard")
        self.actionOpen_Manual_Test_Window = QtGui.QAction(main_window)
        self.actionOpen_Manual_Test_Window.setEnabled(True)
        self.actionOpen_Manual_Test_Window.setIconVisibleInMenu(True)
        self.actionOpen_Manual_Test_Window.setObjectName("actionOpen_Manual_Test_Window")
        self.actionVersion_Information = QtGui.QAction(main_window)
        self.actionVersion_Information.setObjectName("actionVersion_Information")
        self.actionESDEMC_Website = QtGui.QAction(main_window)
        self.actionESDEMC_Website.setObjectName("actionESDEMC_Website")
        self.actionBias_Setup_2 = QtGui.QAction(main_window)
        self.actionBias_Setup_2.setObjectName("actionBias_Setup_2")
        self.actionBias_Setup_3 = QtGui.QAction(main_window)
        self.actionBias_Setup_3.setObjectName("actionBias_Setup_3")
        self.actionEnable_Autosave = QtGui.QAction(main_window)
        self.actionEnable_Autosave.setCheckable(True)
        self.actionEnable_Autosave.setChecked(True)
        self.actionEnable_Autosave.setObjectName("actionEnable_Autosave")
        self.actionManual_Test_Window = QtGui.QAction(main_window)
        self.actionManual_Test_Window.setObjectName("actionManual_Test_Window")
        self.actionSave_Settings_2 = QtGui.QAction(main_window)
        self.actionSave_Settings_2.setObjectName("actionSave_Settings_2")
        self.actiontest = QtGui.QAction(main_window)
        self.actiontest.setObjectName("actiontest")
        self.actionAdvanced_Mode = QtGui.QAction(main_window)
        self.actionAdvanced_Mode.setCheckable(True)
        self.actionAdvanced_Mode.setObjectName("actionAdvanced_Mode")
        self.actionPerformance_Stats = QtGui.QAction(main_window)
        self.actionPerformance_Stats.setObjectName("actionPerformance_Stats")
        self.actionOutput_Log = QtGui.QAction(main_window)
        self.actionOutput_Log.setObjectName("actionOutput_Log")
        self.actionVerification = QtGui.QAction(main_window)
        self.actionVerification.setObjectName("actionVerification")
        self.actionMeasuremt_Method = QtGui.QAction(main_window)
        self.actionMeasuremt_Method.setObjectName("actionMeasuremt_Method")
        self.actionScope_Log = QtGui.QAction(main_window)
        self.actionScope_Log.setObjectName("actionScope_Log")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "POS"))
        self.label_3.setText(_translate("main_window", "Patron Selection"))
        self.new_user_button.setText(_translate("main_window", "+"))
        self.label.setText(_translate("main_window", "Available Drinks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.menu_tab), _translate("main_window", "Menu"))
        self.label_2.setText(_translate("main_window", "Your Open Tab"))
        self.settle_up_button.setText(_translate("main_window", "Settle Up!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tab), _translate("main_window", "Your Tab"))
        self.menuFile.setTitle(_translate("main_window", "File"))
        self.actionOsilloscope_Setup.setText(_translate("main_window", "Osilloscope Setup"))
        self.actionPulser_Setup.setText(_translate("main_window", "Pulser Setup"))
        self.actionLeakage_Setup.setText(_translate("main_window", "Leakage Setup"))
        self.actionBias_Setup.setText(_translate("main_window", "Bias Setup"))
        self.actionProbe_Station_Setup.setText(_translate("main_window", "Probe Station Setup"))
        self.actionStandard_TLP.setText(_translate("main_window", "Standard TLP (TDR-O)"))
        self.actionVF_TLP_TDR_S.setText(_translate("main_window", "VF-TLP (TDR-S)"))
        self.actionSave_Settings.setText(_translate("main_window", "Save Settings"))
        self.actionSave_Settings.setShortcut(_translate("main_window", "Ctrl+S"))
        self.actionLoad_Settings.setText(_translate("main_window", "Load Settings"))
        self.actionLoad_Settings.setShortcut(_translate("main_window", "Ctrl+O"))
        self.actionStop_Criteria.setText(_translate("main_window", "Stop Criteria"))
        self.actionCalibration_Setup.setText(_translate("main_window", "Calibration Window"))
        self.actionCalibration_Wizard.setText(_translate("main_window", "Calibration Wizard"))
        self.actionOpen_Manual_Test_Window.setText(_translate("main_window", "Open Manual Test Window"))
        self.actionVersion_Information.setText(_translate("main_window", "Version Information"))
        self.actionESDEMC_Website.setText(_translate("main_window", "ESDEMC Website"))
        self.actionBias_Setup_2.setText(_translate("main_window", "Bias Setup"))
        self.actionBias_Setup_3.setText(_translate("main_window", "Bias Setup"))
        self.actionEnable_Autosave.setText(_translate("main_window", "Enable Autosave"))
        self.actionManual_Test_Window.setText(_translate("main_window", "Manual Test Window"))
        self.actionSave_Settings_2.setText(_translate("main_window", "Save Settings"))
        self.actiontest.setText(_translate("main_window", "test"))
        self.actionAdvanced_Mode.setText(_translate("main_window", "Advanced Mode"))
        self.actionPerformance_Stats.setText(_translate("main_window", "Performance Stats"))
        self.actionOutput_Log.setText(_translate("main_window", "Output Log"))
        self.actionVerification.setText(_translate("main_window", "Verification"))
        self.actionMeasuremt_Method.setText(_translate("main_window", "Measurement Method"))
        self.actionScope_Log.setText(_translate("main_window", "Scope Log"))
