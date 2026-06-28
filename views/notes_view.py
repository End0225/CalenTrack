from PyQt6 import QtCore, QtWidgets
from utils.button_factory import ButtonFactory


class NotesView(QtWidgets.QWidget):
    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory = ButtonFactory(self.icon_manager)
        self.setup_ui()
        
    def setup_ui(self):
        self.setObjectName("notes_page")
        self.gridLayout_20 = QtWidgets.QGridLayout(self)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.notes_grid = QtWidgets.QGridLayout()
        self.notes_grid.setContentsMargins(12, 10, 12, 14)
        self.notes_grid.setObjectName("notes_grid")
        self.notes_title_label = QtWidgets.QLabel(parent=self)
        self.notes_title_label.setText("New note")
        self.notes_title_label.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;""")
        self.notes_title_label.setObjectName("notes_title_label")
        self.notes_grid.addWidget(self.notes_title_label, 2, 0, 1, 1)
        self.notes_deleteall_btn = self.factory.get_btn(self, "red", "Delete all", [80, 20], QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed, None, None)
        self.notes_grid.addWidget(self.notes_deleteall_btn, 2, 1, 1, 1)
        self.editor_frame = QtWidgets.QFrame(parent=self)
        self.editor_frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
}""")
        self.editor_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.editor_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.editor_frame.setObjectName("editor_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.editor_frame)
        self.gridLayout_4.setContentsMargins(8, 8, 8, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.editor_save_btn = self.factory.get_btn(self.editor_frame, "green", "Save", [0, 20], None, None, "save-icon.png", [19, 19])
        self.gridLayout_4.addWidget(self.editor_save_btn, 2, 0, 1, 1)
        self.editor_lineedit = QtWidgets.QLineEdit(parent=self.editor_frame)
        self.editor_lineedit.setPlaceholderText("Title")
        self.editor_lineedit.setMinimumSize(QtCore.QSize(0, 24))
        self.editor_lineedit.setStyleSheet("""QLineEdit {
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
        self.editor_lineedit.setObjectName("editor_lineedit")
        self.gridLayout_4.addWidget(self.editor_lineedit, 0, 0, 1, 2)
        self.editor_clear_btn = self.factory.get_btn(self, "gray", "Clear", [0, 20], None, None, "delete-icon.png", None)
        self.gridLayout_4.addWidget(self.editor_clear_btn, 2, 1, 1, 1)
        self.editor_plaintextedit = QtWidgets.QPlainTextEdit(parent=self.editor_frame)
        self.editor_plaintextedit.setStyleSheet("""QPlainTextEdit {
    color: #fff;
    font-weight: 700;
    font-size: 12px;
    border-radius: 8%;
    margin-bottom: 6px;
}
QPlainTextEdit:focus{
    border: 1px solid #8b5cf6;
}""")
        self.editor_plaintextedit.setPlainText("")
        self.editor_plaintextedit.setPlaceholderText("Text...")
        self.editor_plaintextedit.setBackgroundVisible(False)
        self.editor_plaintextedit.setCenterOnScroll(False)
        self.editor_plaintextedit.setObjectName("editor_plaintextedit")
        self.gridLayout_4.addWidget(self.editor_plaintextedit, 1, 0, 1, 2)
        self.notes_grid.addWidget(self.editor_frame, 1, 0, 1, 2)
        self.notes_listwidget = QtWidgets.QListWidget(parent=self)
        self.notes_listwidget.setStyleSheet("""QListWidget {
    background-color: #252525;
    border: 1px solid #3e3e42;
    padding: 4px 8px;
    border-radius: 15%;
}""")
        self.notes_listwidget.setObjectName("notes_listwidget")
        self.notes_grid.addWidget(self.notes_listwidget, 3, 0, 1, 2)
        self.note_title_label = QtWidgets.QLabel(parent=self)
        self.note_title_label.setText("Notes")
        self.note_title_label.setMinimumSize(QtCore.QSize(0, 20))
        self.note_title_label.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;""")
        self.note_title_label.setObjectName("note_title_label")
        self.notes_grid.addWidget(self.note_title_label, 0, 0, 1, 2)
        self.gridLayout_20.addLayout(self.notes_grid, 0, 0, 1, 1)