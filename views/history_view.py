from PyQt6 import QtCore, QtWidgets
from utils.button_factory import ButtonFactory


class HistoryView(QtWidgets.QWidget):
    del_item_clicked = QtCore.pyqtSignal(QtWidgets.QListWidgetItem)
    establish_item_clicked = QtCore.pyqtSignal(str)
    clear_all_clicked = QtCore.pyqtSignal()

    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory: ButtonFactory = ButtonFactory(self.icon_manager)
        self.setup_ui()
        
    def setup_ui(self) -> None:
        self.setObjectName("history_page")
        self.gridLayout_19 = QtWidgets.QGridLayout(self)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.history_grid = QtWidgets.QGridLayout()
        self.history_grid.setContentsMargins(12, 10, 12, 55)
        self.history_grid.setObjectName("history_grid")
        self.history_title_label = QtWidgets.QLabel(parent=self)
        self.history_title_label.setText("History")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_title_label.sizePolicy().hasHeightForWidth())
        self.history_title_label.setSizePolicy(sizePolicy)
        self.history_title_label.setStyleSheet("""color: white;
font-size: 18px;
font-weight: 700;""")
        self.history_title_label.setLineWidth(1)
        self.history_title_label.setObjectName("history_title_label")
        self.history_grid.addWidget(self.history_title_label, 0, 0, 1, 1)
        self.history_clear_btn = self.factory.get_btn(self, "red", "Clear", [90, 20], None, None, "delete-icon.png", None)
        self.history_clear_btn.clicked.connect(self.clear_all_clicked.emit)
        self.history_grid.addWidget(self.history_clear_btn, 0, 1, 1, 1)
        self.history_listwidget = QtWidgets.QListWidget(parent=self)
        self.history_listwidget.setMinimumSize(QtCore.QSize(0, 486))
        self.history_listwidget.setStyleSheet("""QListWidget {
    background-color: #252525;
    border: 1px solid #3e3e42;
    padding: 4px 8px;
    border-radius: 15%;
}""")
        self.history_listwidget.setObjectName("history_listwidget")
        self.history_grid.addWidget(self.history_listwidget, 1, 0, 1, 2)
        self.gridLayout_19.addLayout(self.history_grid, 0, 0, 1, 1)

    def add_item(self, note_text: str, note_time: str, note_id: int) -> None:
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(0, 28)) 
        self.history_listwidget.addItem(item)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 1, 1)
        if self.history_listwidget.count() == 1:
            widget.setStyleSheet("""QWidget {
    border: none;
    background-color:#252525;
    padding: 0;
}
QWidget:hover {
    background-color: #2d2d2d;
}""")
        else:
            widget.setStyleSheet("""QWidget {
    border: none;
    background-color:#252525;
    border-top: 1px solid #3e3e42;
    padding: 0;
}
QWidget:hover {
    background-color: #2d2d2d;
}""")
        label = QtWidgets.QLabel(note_text)
        label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
        layout.addWidget(label)
        establish_btn = QtWidgets.QPushButton("Establish")
        establish_btn.setStyleSheet("""QPushButton {
    background-color: #48b585;
    padding: 0;
    border-top: none;
    border-radius: 4%;
    color: #fff; 
    font-weight: 700;
    font-size: 12px;
    }
    QPushButton:focus {
    border: none;
    outline: none;
    }
    QPushButton:hover {
    background-color: #38936c !important;
    }""")
        establish_btn.setFixedSize(60, 18)
        del_button = QtWidgets.QPushButton("Delete")
        del_button.setStyleSheet("""QPushButton {
    background-color: #d13c30;
    padding: 0;
    border-top: none;
    border-radius: 4%;
    color: white;
    font-weight: 700;
    font-size: 12px;
    }
    QPushButton:focus {
    border: none;
    outline: none;
    }
    QPushButton:hover {
    background-color: #af3025 !important;
    }""")
        del_button.setFixedSize(55, 18)
        layout.addWidget(establish_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.history_listwidget.setItemWidget(item, widget)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        del_button.clicked.connect(lambda: self.del_item_clicked.emit(item))
        establish_btn.clicked.connect(lambda: self.establish_item_clicked.emit(note_time))

    def get_listwidget_row(self, item: QtWidgets.QListWidgetItem) -> int:
        return self.history_listwidget.row(item)

    def listwidget_takeitem(self, row: int) -> None:
        self.history_listwidget.takeItem(row)

    def clear_all(self) -> None:
        self.history_listwidget.clear()