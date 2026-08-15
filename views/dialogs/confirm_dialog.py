from PyQt6 import QtCore, QtWidgets, QtGui
from utils.button_factory import ButtonFactory


class ConfirmDialog(QtWidgets.QDialog):
    confirmation_clicked = QtCore.pyqtSignal(bool)

    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory: ButtonFactory = ButtonFactory(self.icon_manager)
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setWindowTitle("CalenTrack | Delete data")
        self.setWindowIcon(self.icon_manager.get_app_icon())
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
        button_container = QtWidgets.QWidget()
        button_container.setStyleSheet("background: transparent;")
        button_layout = QtWidgets.QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(10)
        self.ok_button = self.factory.get_btn(button_container, "green", "Yes", [80, 20], QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred, None, None)
        self.no_button = self.factory.get_btn(button_container, "red", "No", [80, 20], QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred, None, None)
        button_layout.addStretch()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.no_button)
        button_layout.addStretch()
        self._main_gridlayout.addWidget(button_container, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self._main_gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self._pushbutton = self.factory.get_btn(self, "gray", "", [400, 225], QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred, "are_you_sure.png", [400, 225])
        self._main_gridlayout.addWidget(self._pushbutton, 1, 0, 1, 1)
        self._gridlayout.addLayout(self._main_gridlayout, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.ok_button.clicked.connect(lambda: (self.confirmation_clicked.emit(True), self.close()))
        self.no_button.clicked.connect(lambda: (self.confirmation_clicked.emit(False), self.close()))

    def closeEvent(self, event: QtGui.QCloseEvent):
        if event.spontaneous():
            self.confirmation_clicked.emit(False)
        self.close()

    def run(self) -> None:
        self.exec()