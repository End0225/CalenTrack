from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from utils.button_factory import ButtonFactory


class MainWindowView(QMainWindow):
    def __init__(self, icon_manager):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("CalenTrack")
        self.resize(615, 670)
        self.setMinimumSize(QtCore.QSize(480, 580))
        self.icon_manager = icon_manager
        self.setWindowIcon(self.icon_manager.get_icon("app-logo.ico"))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.body = QtWidgets.QGridLayout()
        self.body.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.body.setSpacing(0)
        self.body.setObjectName("body")
        self.pages = {}
        self.factory = ButtonFactory(self.icon_manager)
        self.buttons = {}
        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet("background-color: #1e1c1a;")
        self.main_frame.setObjectName("main_frame")
        self.main = QtWidgets.QGridLayout(self.main_frame)
        self.main.setContentsMargins(0, 0, 0, 0)
        self.main.setObjectName("main")
        self.main_grid = QtWidgets.QGridLayout()
        self.main_grid.setObjectName("main_grid")
        self.main_stackedwidget = QtWidgets.QStackedWidget(parent=self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_stackedwidget.sizePolicy().hasHeightForWidth())
        self.main_stackedwidget.setSizePolicy(sizePolicy)
        self.main_stackedwidget.setObjectName("main_stackedwidget")
        self.main_grid.addWidget(self.main_stackedwidget, 0, 0, 1, 1)
        self.main.addLayout(self.main_grid, 0, 0, 1, 1)
        self.body.addWidget(self.main_frame, 0, 1, 1, 1)
        self.body.setColumnStretch(0, 1)
        self.body.setColumnStretch(1, 4)
        self.gridLayout_6.addLayout(self.body, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)
        self._create_sidebar()
        self.show()

    def _create_sidebar(self) -> None:
        self.aside_frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aside_frame.sizePolicy().hasHeightForWidth())
        self.aside_frame.setSizePolicy(sizePolicy)
        self.aside_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.aside_frame.setStyleSheet("background-color: #1a1817;\nborder-right: 1px solid #3e3e42;\npadding: 1px;")
        self.aside_frame.setObjectName("aside_frame")
        self.aside = QtWidgets.QVBoxLayout(self.aside_frame)
        self.aside.setContentsMargins(0, 0, 0, 0)
        self.aside.setSpacing(0)
        self.aside.setObjectName("aside")
        self.app_title_label = QtWidgets.QLabel(parent=self.aside_frame)
        self.app_title_label.setText("CalenTrack")
        self.app_title_label.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.app_title_label.setFont(font)
        self.app_title_label.setStyleSheet("color: #8B5CF6;\nborder: none;\nfont-size: 19px;\nfont-weight: 700;\nborder-bottom: 1px solid #3e3e42;")
        self.app_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.app_title_label.setObjectName("app_title_label")
        self.aside.addWidget(self.app_title_label)
        self._add_nav_button(self.aside_frame, "stopwatch_view", "Stopwatch", "stopwatch-icon.png", [18, 18])
        self._add_nav_button(self.aside_frame, "history_view", "History", "history-icon.svg", [17, 17])
        self._add_nav_button(self.aside_frame, "notes_view", "Notes", "note-icon.png", [18, 18])
        self._add_nav_button(self.aside_frame, "calendar_view", "Calendar", "calendar-icon.png", [18, 18])
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.aside.addItem(spacerItem)
        self._add_nav_button(self.aside_frame, "settings_view", "Settings", "settings-icons.png", [22, 22])
        self.body.addWidget(self.aside_frame, 0, 0, 1, 1)

    def _add_nav_button(self, parent: QtWidgets.QVBoxLayout, name: str, btn_text: str, icon_file_name: str, icon_size: list[int]) -> None:
        button = self.factory.get_aside_tool_btn(parent, btn_text, icon_file_name, icon_size)
        self.aside.addWidget(button)
        self.buttons[name] = button

    def add_page(self, name: str, widget: QtWidgets.QWidget) -> None:
        self.pages[name] = widget
        self.main_stackedwidget.addWidget(widget)
        if name in self.buttons:
            self.buttons[name].clicked.connect(lambda: self.show_page(widget, self.buttons[name]))

    def show_page(self, page: QtWidgets.QWidget, button: QtWidgets.QToolButton) -> None:
        self.main_stackedwidget.setCurrentWidget(page)
        for _, btn in self.buttons.items():
            btn.setStyleSheet(self.factory.base_tool_btn_style)
        button.setStyleSheet(self.factory.base_tool_btn_style + self.factory.checked_tool_btn_style)