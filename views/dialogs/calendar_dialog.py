from PyQt6 import QtCore, QtWidgets
from utils.button_factory import ButtonFactory


class CalendarDialog(QtWidgets.QDialog):
    color_dialog_clicked = QtCore.pyqtSignal()
    apply_clicked = QtCore.pyqtSignal(QtCore.QDate, str, str, str)

    def __init__(self, icon_manager, color_dialog: QtWidgets.QColorDialog):
        super().__init__()
        self.icon_manager = icon_manager
        self.color_dialog: QtWidgets.QColorDialog = color_dialog
        self.color: str = "#252525"
        self.date: QtCore.QDate
        self.factory: ButtonFactory = ButtonFactory(self.icon_manager)
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setWindowIcon(self.icon_manager.get_app_icon())
        self.setWindowTitle("CalenTrack | Choose data")
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
        self.time_label = QtWidgets.QLabel("Select time:", parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.main_gridlayout.addWidget(self.time_label, 0, 0, 1, 1)
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
        self.note_label = QtWidgets.QLabel("Select note:", parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note_label.sizePolicy().hasHeightForWidth())
        self.note_label.setSizePolicy(sizePolicy)
        self.note_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.main_gridlayout.addWidget(self.note_label, 4, 0, 1, 1)
        self.color_label = QtWidgets.QLabel("Color date:", parent=self)
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
        self.note_combobox = QtWidgets.QComboBox(parent=self)
        self.note_combobox.setMinimumSize(QtCore.QSize(0, 20))
        combobox_style: str = """QComboBox {
    color: #fff;
    font-weight: 700;
    background-color: #3e3e42;
    font-size: 12px;
    border-radius: 4%;
    padding: 2px;
}
QComboBox QAbstractItemView {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 4px;
    outline: none;
    color: #fff;
}"""
        self.note_combobox.setStyleSheet(combobox_style)
        self.main_gridlayout.addWidget(self.note_combobox, 6, 0, 1, 1)
        self.time_combobox = QtWidgets.QComboBox(parent=self)
        self.time_combobox.setMinimumSize(QtCore.QSize(0, 20))
        self.time_combobox.setStyleSheet(combobox_style)
        self.main_gridlayout.addWidget(self.time_combobox, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem4, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.main_gridlayout.addItem(spacerItem5, 9, 0, 1, 1)
        self.gridlayout.addLayout(self.main_gridlayout, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.my_color = "#252525"
        self.color_pushbutton.clicked.connect(self.color_dialog_clicked.emit)
        self.apply_button.clicked.connect(lambda: (self.apply_clicked.emit(self.date, self.time_combobox.currentText(), self.note_combobox.currentText(), self.color), self._close()))
        self.discard_button.clicked.connect(self._close)
        self.finished.connect(self._close)

    def _fill_comboboxes(self, stopwatch_times: list[str], notes_titles: list[str]) -> None:
        self.time_combobox.addItems(["None"])
        self.note_combobox.addItems(["None"])
        try:
            for i in stopwatch_times:
                self.time_combobox.addItems([i])
            for i in notes_titles:
                self.note_combobox.addItems([i])
        except:  pass

    def _close(self) -> None:
        self.time_combobox.clear()
        self.note_combobox.clear()
        self.color = "#252525"
        self.set_btn_color(self.color)
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

    def run(self, stopwatch_times: list[str], notes_titles: list[str], date: QtCore.QDate) -> None:
        self._fill_comboboxes(stopwatch_times, notes_titles)
        self.date = date
        self.exec()