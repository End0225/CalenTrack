from PyQt6 import QtCore, QtWidgets
from utils.button_factory import ButtonFactory


class HistoryView(QtWidgets.QWidget):
    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory = ButtonFactory(self.icon_manager)
        self.setup_ui()
        
    def setup_ui(self):
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