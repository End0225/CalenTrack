from PyQt6 import QtCore, QtWidgets


class DateDialog(QtWidgets.QDialog):
    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setWindowIcon(self.icon_manager.get_icon("app-logo.ico"))
        self.setObjectName("dialog")
        self.resize(400, 300)
        self.setMinimumSize(QtCore.QSize(280, 250))
        self.setStyleSheet("""QDialog {
    background-color: #252525;
    border: 1px solid #3e3e42;
}""")
        self.dialog_gridlayout = QtWidgets.QGridLayout(self)
        self.dialog_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_gridlayout.setSpacing(0)
        self.dialog_gridlayout.setObjectName("dialog_gridlayout")
        self.dialog_main_gridlayout = QtWidgets.QGridLayout()
        self.dialog_main_gridlayout.setContentsMargins(10, 12, 10, 8)
        self.dialog_main_gridlayout.setObjectName("dialog_main_gridlayout")
        self.dialog_title_lineedit = QtWidgets.QLineEdit(parent=self)
        self.dialog_title_lineedit.setPlaceholderText("Not selected")
        self.dialog_title_lineedit.setStyleSheet("""QLineEdit {
    color: #fff;
    font-weight: 700;
    background-color: #3e3e42;
    font-size: 12px;
    border-radius: 4%;
    margin-left: 4px;
}""")
        self.dialog_title_lineedit.setObjectName("dialog_title_lineedit")
        self.dialog_title_lineedit.setReadOnly(True)
        self.dialog_main_gridlayout.addWidget(self.dialog_title_lineedit, 0, 1, 1, 1)
        self.dialog_time_lineedit = QtWidgets.QLineEdit(parent=self)
        self.dialog_time_lineedit.setPlaceholderText("Not selected")
        self.dialog_time_lineedit.setStyleSheet("""QLineEdit {
    color: #fff;
    font-weight: 700;
    background-color: #3e3e42;
    font-size: 12px;
    border-radius: 4%;
    margin-right: 4px;
}""")
        self.dialog_time_lineedit.setObjectName("dialog_time_lineedit")
        self.dialog_time_lineedit.setReadOnly(True)
        self.dialog_main_gridlayout.addWidget(self.dialog_time_lineedit, 0, 0, 1, 1)
        self.dialog_plaintextedit = QtWidgets.QPlainTextEdit(parent=self)
        self.dialog_plaintextedit.setPlaceholderText("Not selected")
        self.dialog_plaintextedit.setStyleSheet("""QPlainTextEdit {
    color: #fff;
    font-weight: 700;
    background-color: #3e3e42;
    font-size: 12px;
    border-radius: 6%;
    margin: 8px 0px 8px 0px;
}""")
        self.dialog_plaintextedit.setObjectName("dialog_plaintextedit")
        self.dialog_plaintextedit.setReadOnly(True)
        self.dialog_main_gridlayout.addWidget(self.dialog_plaintextedit, 1, 0, 1, 2)
        self.dialog_buttonBox = QtWidgets.QDialogButtonBox(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_buttonBox.sizePolicy().hasHeightForWidth())
        self.dialog_buttonBox.setSizePolicy(sizePolicy)
        self.dialog_buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.dialog_buttonBox.setStyleSheet("""QPushButton {
    background-color: #3e3e42;
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
QPushButton:hover {
    background-color: #52525a;
}""")
        self.dialog_buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dialog_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close)
        self.dialog_buttonBox.setCenterButtons(False)
        self.dialog_buttonBox.setObjectName("dialog_buttonBox")
        self.dialog_main_gridlayout.addWidget(self.dialog_buttonBox, 2, 0, 1, 2)
        self.dialog_gridlayout.addLayout(self.dialog_main_gridlayout, 0, 0, 1, 1)
        self.dialog_buttonBox.rejected.connect(self.reject)
        self.dialog_buttonBox.accepted.connect(self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

    def load_data(self, date: str, stopwatch_note: str, note_title: str, note_text: str) -> None:
        self.setWindowTitle(f"CalenTrack | {date}")
        if stopwatch_note != "None":
            self.dialog_time_lineedit.setText(stopwatch_note)
        if note_title != "None":
            self.dialog_title_lineedit.setText(note_title)
        if note_text != "None":
                self.dialog_plaintextedit.setPlainText(note_text)

    def run(self) -> None:
        self.show()
