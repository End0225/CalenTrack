from PyQt6 import QtWidgets, QtCore
from utils.button_factory import ButtonFactory


class TagDialog(QtWidgets.QDialog):
    color_dialog_clicked = QtCore.pyqtSignal()
    apply_clicked = QtCore.pyqtSignal(str, str)
    apply_remake_clicked = QtCore.pyqtSignal(str, str, int)

    def __init__(self, icon_manager, color_dialog: QtWidgets.QColorDialog):
        super().__init__()
        self.icon_manager = icon_manager
        self.color_dialog: QtWidgets.QColorDialog = color_dialog
        self.color: str = "#252525"
        self.factory: ButtonFactory = ButtonFactory(self.icon_manager)
        self.tag_dialog_mode: str = "add"
        self.tag_id: int
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setWindowIcon(self.icon_manager.get_app_icon())
        self.setWindowTitle("CalenTrack | Add tag")
        self.resize(400, 300)
        self.setStyleSheet("""QDialog {
    background-color: #252525;
    border: 1px solid #3e3e42;
}""")
        self.gridlayout = QtWidgets.QGridLayout(self)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.main_gridlayout = QtWidgets.QGridLayout()
        self.main_gridlayout.setContentsMargins(10, 12, 10, 8)
        self.main_gridlayout.setSpacing(0)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem1, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.main_gridlayout.addItem(spacerItem2, 11, 0, 1, 1)
        self.tag_label = QtWidgets.QLabel("Tag name:", parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tag_label.sizePolicy().hasHeightForWidth())
        self.tag_label.setSizePolicy(sizePolicy)
        self.tag_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.main_gridlayout.addWidget(self.tag_label, 0, 0, 1, 1)
        self.color_pushbutton = QtWidgets.QPushButton(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_pushbutton.sizePolicy().hasHeightForWidth())
        self.color_pushbutton.setSizePolicy(sizePolicy)
        self.color_pushbutton.setMinimumSize(QtCore.QSize(0, 20))
        self.color_pushbutton.setStyleSheet("""QPushButton {
    background-color: #252525;
    border: 1px solid #777777;
}
QPushButton:focus {
    border: 1px solid #777777;
    outline: none;
}""")
        self.color_pushbutton.setText("")
        self.main_gridlayout.addWidget(self.color_pushbutton, 10, 0, 1, 1)
        self.color_label = QtWidgets.QLabel("Tag color:", parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_label.sizePolicy().hasHeightForWidth())
        self.color_label.setSizePolicy(sizePolicy)
        self.color_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.main_gridlayout.addWidget(self.color_label, 8, 0, 1, 1)
        button_container = QtWidgets.QWidget()
        button_container.setStyleSheet("background: transparent;")
        button_layout = QtWidgets.QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 8, 0, 0)
        button_layout.setSpacing(10)
        self.apply_button = self.factory.get_btn(button_container, "green", "Apply", [80, 20], QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred, None, None)
        self.discard_button = self.factory.get_btn(button_container, "red", "Discard", [80, 20], QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred, None, None)
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.discard_button)
        button_layout.addStretch()
        self.main_gridlayout.addWidget(button_container, 12, 0, 1, 1)
        self.tag_lineedit = QtWidgets.QLineEdit(parent=self)
        self.tag_lineedit.setPlaceholderText("Name")
        self.tag_lineedit.setMinimumSize(QtCore.QSize(0, 20))
        self.tag_lineedit.setStyleSheet("""QLineEdit {
    color: #fff;
    border: 1px solid #52525a;
    border-radius: 6%;
    background-color: #3e3e42;
    font-weight: 700;
    font-size: 12px;
}
QLineEdit:focus{
    border: 1px solid #8b5cf6;
}""")
        self.main_gridlayout.addWidget(self.tag_lineedit, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem5, 9, 0, 1, 1)
        self.gridlayout.addLayout(self.main_gridlayout, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.color_pushbutton.clicked.connect(self.color_dialog_clicked.emit)
        self.apply_button.clicked.connect(self._preclose)
        self.discard_button.clicked.connect(self._close)

    def _preclose(self) -> None:
        match self.tag_dialog_mode:
            case "add":
                self.apply_clicked.emit(*self.get_tag_data())
            case "remake":
                self.apply_remake_clicked.emit(*self.get_tag_data(), self.tag_id)
                self.tag_dialog_mode = "add"
        self._close()

    def get_tag_data(self) -> list[str, str]:
        return [self.tag_lineedit.text(), self.color]

    def _close(self) -> None:
        self.color = "#252525"
        self.set_btn_color(self.color)
        self.tag_lineedit.clear()
        self.close()

    def open_color_dialog(self) -> None:
        if check_color := self.color_dialog.get_color():
            self.color = check_color
        self.set_btn_color(self.color)

    def set_btn_color(self, color: str) -> None:
        self.color_pushbutton.setStyleSheet(f"""QPushButton {{
    background-color: {color};
    border: 1px solid #777777;
}}
QPushButton:focus {{
    border: 1px solid #777777;
    outline: none;
}}""")

    def run(self) -> None:
        self.exec()

    def run_remake_tag_dialog(self, name: str, color: str, id: int) -> None:
        self.tag_lineedit.setText(name)
        self.set_btn_color(color)
        self.tag_id = id
        self.tag_dialog_mode = "remake"
        self.run()