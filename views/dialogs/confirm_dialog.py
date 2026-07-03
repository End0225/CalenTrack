from PyQt6 import QtCore, QtWidgets, QtGui


class ConfirmDialog(QtWidgets.QDialog):
    confirmation_clicked = QtCore.pyqtSignal(bool)

    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setWindowTitle("CalenTrack | Delete data")
        self.setWindowIcon(self.icon_manager.get_icon("app-logo.ico"))
        self.setObjectName("")
        self.resize(412, 300)
        self.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.setStyleSheet("""QDialog {
    background-color: #252525;
    border: 1px solid #3e3e42;
}""")
        self._gridlayout = QtWidgets.QGridLayout(self)
        self._gridlayout.setContentsMargins(0, 0, 0, 0)
        self._gridlayout.setSpacing(0)
        self._gridlayout.setObjectName("_gridlayout")
        self._main_gridlayout = QtWidgets.QGridLayout()
        self._main_gridlayout.setContentsMargins(-1, 4, -1, 4)
        self._main_gridlayout.setObjectName("_main_gridlayout")
        self._buttonbox = QtWidgets.QDialogButtonBox(parent=self)
        self._buttonbox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self._buttonbox.setStyleSheet("""QPushButton {
    background-color: #48b585;
    border-radius: 4%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
    height: 20px;
    width: 80px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton[text=\"&Yes\"] {
    background-color: #48b585;
}
QPushButton[text=\"&No\"] {
        background-color: #d13c30;
}
QPushButton[text=\"&Yes\"]:hover {
        background-color: #38936c;
}
QPushButton[text=\"&No\"]:hover {
        background-color: #af3025;
}""")
        self._buttonbox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self._buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.No|QtWidgets.QDialogButtonBox.StandardButton.Yes)
        self._buttonbox.setCenterButtons(True)
        self._buttonbox.setObjectName("_buttonbox")
        self._main_gridlayout.addWidget(self._buttonbox, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self._main_gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self._pushbutton = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._pushbutton.sizePolicy().hasHeightForWidth())
        self._pushbutton.setSizePolicy(sizePolicy)
        self._pushbutton.setText("")
        self._pushbutton.setIcon(self.icon_manager.get_icon("are_you_sure.webp"))
        self._pushbutton.setIconSize(QtCore.QSize(400, 225))
        self._pushbutton.setShortcut("")
        self._pushbutton.setAutoDefault(True)
        self._pushbutton.setDefault(False)
        self._pushbutton.setFlat(True)
        self._pushbutton.setObjectName("_pushbutton")
        self._main_gridlayout.addWidget(self._pushbutton, 1, 0, 1, 1)
        self._gridlayout.addLayout(self._main_gridlayout, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
        self._buttonbox.accepted.connect(lambda: (self.confirmation_clicked.emit(True), self.close()))
        self._buttonbox.rejected.connect(lambda: (self.confirmation_clicked.emit(False), self.close()))

    def closeEvent(self, event: QtGui.QCloseEvent):
        if event.spontaneous():
            self.confirmation_clicked.emit(False)
        self.close()

    def run(self) -> None:
        self.exec()