from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTime, QTimer, QDate
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QDateEdit, QListWidgetItem, QMessageBox
import sqlite3
import shutil
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if getattr(sys, "frozen", False):
            app_dir = os.path.join(os.getenv("APPDATA"), "CalenTrack")
            os.makedirs(app_dir, exist_ok=True)
            self.path_to_db = os.path.join(app_dir, "app_db.db")
            self.path_to_icons = os.path.join(app_dir, "resources", "icons")
            os.makedirs(self.path_to_icons, exist_ok=True)
            src_icons_dir = os.path.join(sys._MEIPASS, "resources", "icons")
            if os.path.exists(src_icons_dir):
                for file in os.listdir(src_icons_dir):
                    src = os.path.join(src_icons_dir, file)
                    dst = os.path.join(self.path_to_icons, file)
                    if not os.path.exists(dst):
                        shutil.copyfile(src, dst)
            src_db = os.path.join(sys._MEIPASS, "app_db.db")
            if not os.path.exists(self.path_to_db):
                if os.path.exists(src_db):
                    shutil.copyfile(src_db, self.path_to_db)
                else:
                    self.create_tables()
        else:
            self.path_to_db = os.path.join(os.path.dirname(__file__), "app_db.db")
            self.path_to_icons = os.path.join(os.path.dirname(__file__), "resources", "icons")
        if not os.path.exists(self.path_to_db) or not self.check_database_integrity():
            self.create_tables()
        self.copy_all_resources(self.path_to_icons)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 670)
        MainWindow.setMinimumSize(QtCore.QSize(480, 580))
        logo_icon = self.get_icon("app-logo.ico")
        MainWindow.setWindowIcon(logo_icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.body = QtWidgets.QGridLayout()
        self.body.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.body.setSpacing(0)
        self.body.setObjectName("body")
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
        self.app_title_label.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.app_title_label.setFont(font)
        self.app_title_label.setStyleSheet("color: #8B5CF6;\nborder: none;\nfont-size: 19px;\nfont-weight: 700;\nborder-bottom: 1px solid #3e3e42;")
        self.app_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.app_title_label.setObjectName("app_title_label")
        self.aside.addWidget(self.app_title_label)
        self.stopwatch_btn = QtWidgets.QToolButton(parent=self.aside_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_btn.sizePolicy().hasHeightForWidth())
        self.stopwatch_btn.setSizePolicy(sizePolicy)
        self.stopwatch_btn.setMinimumSize(QtCore.QSize(93, 14))
        style_aside_btn = """QToolButton {
    color: #9E9EA7;
    border: none;
    font-size: 12px;
    font-weight: 700;
}
QToolButton:hover {
    background-color: #252525;
}"""
        self.stopwatch_btn.setStyleSheet(style_aside_btn)
        stopwatch_icon = self.get_icon("stopwatch-icon.png")
        self.stopwatch_btn.setIcon(stopwatch_icon)
        self.stopwatch_btn.setIconSize(QtCore.QSize(18, 18))
        self.stopwatch_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.stopwatch_btn.setAutoRaise(False)
        self.stopwatch_btn.setObjectName("stopwatch_btn")
        self.aside.addWidget(self.stopwatch_btn)
        self.history_btn = QtWidgets.QToolButton(parent=self.aside_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_btn.sizePolicy().hasHeightForWidth())
        self.history_btn.setSizePolicy(sizePolicy)
        self.history_btn.setMinimumSize(QtCore.QSize(93, 14))
        self.history_btn.setStyleSheet(style_aside_btn)
        history_icon = self.get_icon("history-icon.svg")
        self.history_btn.setIcon(history_icon)
        self.history_btn.setIconSize(QtCore.QSize(17, 17))
        self.history_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.history_btn.setObjectName("history_btn")
        self.aside.addWidget(self.history_btn)
        self.notes_btn = QtWidgets.QToolButton(parent=self.aside_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes_btn.sizePolicy().hasHeightForWidth())
        self.notes_btn.setSizePolicy(sizePolicy)
        self.notes_btn.setMinimumSize(QtCore.QSize(93, 14))
        self.notes_btn.setStyleSheet(style_aside_btn)
        notes_icon = self.get_icon("note-icon.png")
        self.notes_btn.setIcon(notes_icon)
        self.notes_btn.setIconSize(QtCore.QSize(18, 18))
        self.notes_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.notes_btn.setObjectName("notes_btn")
        self.aside.addWidget(self.notes_btn)
        self.calendar_btn = QtWidgets.QToolButton(parent=self.aside_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar_btn.sizePolicy().hasHeightForWidth())
        self.calendar_btn.setSizePolicy(sizePolicy)
        self.calendar_btn.setMinimumSize(QtCore.QSize(93, 14))
        self.calendar_btn.setStyleSheet(style_aside_btn)
        calendar_icon = self.get_icon("calendar-icon.png")
        self.calendar_btn.setIcon(calendar_icon)
        self.calendar_btn.setIconSize(QtCore.QSize(18, 18))
        self.calendar_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.calendar_btn.setObjectName("calendar_btn")
        self.aside.addWidget(self.calendar_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.aside.addItem(spacerItem)
        self.settings_btn = QtWidgets.QToolButton(parent=self.aside_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QtCore.QSize(93, 14))
        self.settings_btn.setStyleSheet(style_aside_btn)
        settings_icon = self.get_icon("settings-icons.png")
        self.settings_btn.setIcon(settings_icon)
        self.settings_btn.setIconSize(QtCore.QSize(20, 20))
        self.settings_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.settings_btn.setObjectName("settings_btn")
        self.aside.addWidget(self.settings_btn)
        self.body.addWidget(self.aside_frame, 0, 0, 1, 1)
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
        self.stopwatch_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_page.sizePolicy().hasHeightForWidth())
        self.stopwatch_page.setSizePolicy(sizePolicy)
        self.stopwatch_page.setObjectName("stopwatch_page")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.stopwatch_page)
        self.gridLayout_17.setContentsMargins(36, 120, 36, 192)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.stopwatch_frame = QtWidgets.QFrame(parent=self.stopwatch_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_frame.sizePolicy().hasHeightForWidth())
        self.stopwatch_frame.setSizePolicy(sizePolicy)
        self.stopwatch_frame.setMaximumSize(QtCore.QSize(400, 380))
        self.stopwatch_frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
}""")
        self.stopwatch_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.stopwatch_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.stopwatch_frame.setObjectName("stopwatch_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.stopwatch_frame)
        self.gridLayout_2.setContentsMargins(32, 20, 32, 36)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stopwatch_time_label = QtWidgets.QLabel(parent=self.stopwatch_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_time_label.sizePolicy().hasHeightForWidth())
        self.stopwatch_time_label.setSizePolicy(sizePolicy)
        self.stopwatch_time_label.setMinimumSize(QtCore.QSize(242, 117))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stopwatch_time_label.setFont(font)
        self.stopwatch_time_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.stopwatch_time_label.setStyleSheet("""border: none;
font-family: 'Consolas', 'Courier New', monospace;
font-size: 32px;
font-weight: 700;
color: #D4D4D4;""")
        self.stopwatch_time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stopwatch_time_label.setObjectName("stopwatch_time_label")
        self.gridLayout_2.addWidget(self.stopwatch_time_label, 0, 0, 1, 2)
        self.stopwatch_start_stop_btn = QtWidgets.QPushButton(parent=self.stopwatch_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_start_stop_btn.sizePolicy().hasHeightForWidth())
        self.stopwatch_start_stop_btn.setSizePolicy(sizePolicy)
        self.stopwatch_start_stop_btn.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.stopwatch_start_stop_btn.setFont(font)
        self.stopwatch_start_stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.stopwatch_start_stop_btn.setStyleSheet("""QPushButton {
    background-color: #8365ee;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #7349e5;
}""")
        start_icon = self.get_icon("start-icon.png")
        self.stopwatch_start_stop_btn.setIcon(start_icon)
        self.stopwatch_start_stop_btn.setIconSize(QtCore.QSize(15, 15))
        self.stopwatch_start_stop_btn.setShortcut("")
        self.stopwatch_start_stop_btn.setCheckable(False)
        self.stopwatch_start_stop_btn.setObjectName("stopwatch_start_stop_btn")
        self.gridLayout_2.addWidget(self.stopwatch_start_stop_btn, 1, 0, 1, 1)
        self.stopwatch_reset_btn = QtWidgets.QPushButton(parent=self.stopwatch_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_reset_btn.sizePolicy().hasHeightForWidth())
        self.stopwatch_reset_btn.setSizePolicy(sizePolicy)
        self.stopwatch_reset_btn.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.stopwatch_reset_btn.setFont(font)
        self.stopwatch_reset_btn.setStyleSheet("""QPushButton {
    background-color: #52525a;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #3e3e42;
}""")
        reset_icon = self.get_icon("reset-icon.png")
        self.stopwatch_reset_btn.setIcon(reset_icon)
        self.stopwatch_reset_btn.setIconSize(QtCore.QSize(12, 12))
        self.stopwatch_reset_btn.setObjectName("stopwatch_reset_btn")
        self.gridLayout_2.addWidget(self.stopwatch_reset_btn, 1, 1, 1, 1)
        self.stopwatch_save_btn = QtWidgets.QPushButton(parent=self.stopwatch_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_save_btn.sizePolicy().hasHeightForWidth())
        self.stopwatch_save_btn.setSizePolicy(sizePolicy)
        self.stopwatch_save_btn.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.stopwatch_save_btn.setFont(font)
        self.stopwatch_save_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.stopwatch_save_btn.setStyleSheet("""QPushButton {
    background-color: #48b585;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #38936c;
}""")
        save_icon = self.get_icon("save-icon.png")
        self.stopwatch_save_btn.setIcon(save_icon)
        self.stopwatch_save_btn.setIconSize(QtCore.QSize(19, 19))
        self.stopwatch_save_btn.setObjectName("stopwatch_save_btn")
        self.gridLayout_2.addWidget(self.stopwatch_save_btn, 2, 0, 1, 2)
        self.gridLayout_17.addWidget(self.stopwatch_frame, 1, 0, 1, 1)
        self.main_stackedwidget.addWidget(self.stopwatch_page)
        self.calendar_page = QtWidgets.QWidget()
        self.calendar_page.setObjectName("calendar_page")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.calendar_page)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.calendar_grid = QtWidgets.QGridLayout()
        self.calendar_grid.setContentsMargins(12, 10, 12, 14)
        self.calendar_grid.setVerticalSpacing(4)
        self.calendar_grid.setObjectName("calendar_grid")
        self.dates_frame = QtWidgets.QFrame(parent=self.calendar_page)
        self.dates_frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
    margin-top: 8px;
}""")
        self.dates_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dates_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dates_frame.setObjectName("dates_frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dates_frame)
        self.gridLayout_8.setContentsMargins(-1, 4, -1, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.dates_title = QtWidgets.QLabel(parent=self.dates_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dates_title.sizePolicy().hasHeightForWidth())
        self.dates_title.setSizePolicy(sizePolicy)
        self.dates_title.setMinimumSize(QtCore.QSize(0, 0))
        self.dates_title.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dates_title.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;
border: none;""")
        self.dates_title.setObjectName("dates_title")
        self.gridLayout_8.addWidget(self.dates_title, 0, 0, 1, 1)
        self.dates_deleteall_btn = QtWidgets.QPushButton(parent=self.dates_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dates_deleteall_btn.sizePolicy().hasHeightForWidth())
        self.dates_deleteall_btn.setSizePolicy(sizePolicy)
        self.dates_deleteall_btn.setMinimumSize(QtCore.QSize(80, 20))
        self.dates_deleteall_btn.setStyleSheet("""QPushButton {
    background-color: #d13c30;
    border-radius: 8%;
    color: #fff;
    font-weight: 700;
    font-size: 13px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #af3025;
}""")
        self.dates_deleteall_btn.setObjectName("dates_deleteall_btn")
        self.gridLayout_8.addWidget(self.dates_deleteall_btn, 0, 1, 1, 1)
        self.dates_listwidget = QtWidgets.QListWidget(parent=self.dates_frame)
        self.dates_listwidget.setStyleSheet("""QListWidget {
    background-color: #252525;
    border: 1px solid #252525;
}""")
        self.dates_listwidget.setObjectName("dates_listwidget")
        self.gridLayout_8.addWidget(self.dates_listwidget, 1, 0, 1, 2)
        self.calendar_grid.addWidget(self.dates_frame, 5, 1, 1, 1)
        self.calendar_title_label = QtWidgets.QLabel(parent=self.calendar_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar_title_label.sizePolicy().hasHeightForWidth())
        self.calendar_title_label.setSizePolicy(sizePolicy)
        self.calendar_title_label.setMinimumSize(QtCore.QSize(100, 20))
        self.calendar_title_label.setStyleSheet("""color: white;
font-size: 18px;
font-weight: 700;""")
        self.calendar_title_label.setObjectName("calendar_title_label")
        self.calendar_grid.addWidget(self.calendar_title_label, 1, 1, 1, 1)
        self.calendar_frame = QtWidgets.QFrame(parent=self.calendar_page)
        self.calendar_frame.setMinimumSize(QtCore.QSize(0, 20))
        self.calendar_frame.setStyleSheet("""QFrame {
    border-radius: 15%;
    border: 1px solid #3e3e42;
    background-color: #252525;
}""")
        self.calendar_frame.setObjectName("calendar_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.calendar_frame)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.calendarwidget = QtWidgets.QCalendarWidget(parent=self.calendar_frame)
        self.calendarwidget.setAccessibleName("")
        self.calendarwidget.setStyleSheet("""QCalendarWidget QToolButton {
    color: #fff;
    font-size: 15px;
    font-weight: bold;
    margin: 2px 5px 1px 5px;
    background-color: transparent;
}
QCalendarWidget QToolButton#qt_calendar_prevmonth,
QCalendarWidget QToolButton#qt_calendar_nextmonth {
        background-color: transparent;
        border-radius: 4px;
}
QCalendarWidget QAbstractItemView {
    background-color: #252525;
    selection-background-color: #1a1a1a;
    outline: none;
    font-size: 12px;
    font-weight: 700;
    color: #fff;
    border: none;
}
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: #252525;
}
QCalendarWidget QMenu {
    background-color: #252525;
    color: white;
    border: 1px solid #3e3e42;
}
QCalendarWidget QMenu::item {
    padding: 5px 20px;
}
QCalendarWidget QMenu::item:selected {
    background-color: #52525a;
    color: white;
}
QCalendarWidget QWidget {
    alternate-background-color: #252525;
}
QCalendarWidget QAbstractItemView:disabled {
    color: transparent;
}
QCalendarWidget QToolButton#qt_calendar_prevmonth {""" +
f"    qproperty-icon: url('{self.icon_path["left-arrow-icon.png"].replace('\\', '/')}');" +
"""}
QCalendarWidget QToolButton#qt_calendar_nextmonth {""" +
f"    qproperty-icon: url('{self.icon_path["right-arrow-icon.png"].replace('\\', '/')}');" +
"}")
        self.calendarwidget.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.Germany))
        self.calendarwidget.setObjectName("calendarwidget")
        self.verticalLayout_2.addWidget(self.calendarwidget)
        self.calendar_grid.addWidget(self.calendar_frame, 2, 1, 1, 1)
        self.gridLayout_15.addLayout(self.calendar_grid, 0, 0, 1, 1)
        self.main_stackedwidget.addWidget(self.calendar_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.settings_page)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.settings_grid = QtWidgets.QGridLayout()
        self.settings_grid.setContentsMargins(12, 10, 12, 60)
        self.settings_grid.setObjectName("settings_grid")
        self.settings_title_label = QtWidgets.QLabel(parent=self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_title_label.sizePolicy().hasHeightForWidth())
        self.settings_title_label.setSizePolicy(sizePolicy)
        self.settings_title_label.setMinimumSize(QtCore.QSize(0, 20))
        self.settings_title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.settings_title_label.setStyleSheet("""color: white;
font-size: 18px;
font-weight: 700;""")
        self.settings_title_label.setObjectName("settings_title_label")
        self.settings_grid.addWidget(self.settings_title_label, 0, 0, 1, 1)
        self.settings_frame = QtWidgets.QFrame(parent=self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_frame.sizePolicy().hasHeightForWidth())
        self.settings_frame.setSizePolicy(sizePolicy)
        self.settings_frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
}""")
        self.settings_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settings_frame)
        self.verticalLayout.setContentsMargins(12, 0, 12, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backup_frame = QtWidgets.QFrame(parent=self.settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_frame.sizePolicy().hasHeightForWidth())
        self.backup_frame.setSizePolicy(sizePolicy)
        self.backup_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.backup_frame.setStyleSheet("border: none;")
        self.backup_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.backup_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.backup_frame.setObjectName("backup_frame")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.backup_frame)
        self.gridLayout_22.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_22.setHorizontalSpacing(0)
        self.gridLayout_22.setVerticalSpacing(10)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.loadbackup_btn = QtWidgets.QPushButton(parent=self.backup_frame)
        self.loadbackup_btn.setMinimumSize(QtCore.QSize(0, 20))
        self.loadbackup_btn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.loadbackup_btn.setStyleSheet("""QPushButton {
    background-color: #52525a;
    border: 1px solid #3e3e42;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #3e3e42;
    border: 1px solid #52525a;
}
""")
        loadbackup_icon = self.get_icon("export-icons.png")
        self.loadbackup_btn.setIcon(loadbackup_icon)
        self.loadbackup_btn.setIconSize(QtCore.QSize(14, 14))
        self.loadbackup_btn.setObjectName("loadbackup_btn")
        self.gridLayout_22.addWidget(self.loadbackup_btn, 3, 0, 1, 1)
        self.savebackup_btn = QtWidgets.QPushButton(parent=self.backup_frame)
        self.savebackup_btn.setMinimumSize(QtCore.QSize(0, 20))
        self.savebackup_btn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.savebackup_btn.setStyleSheet("""QPushButton {
    background-color: #48b585;
    border-radius: 6%;
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #38936c;
}""")
        savebackup_icon = self.get_icon("import-icon.png")
        self.savebackup_btn.setIcon(savebackup_icon)
        self.savebackup_btn.setIconSize(QtCore.QSize(15, 15))
        self.savebackup_btn.setObjectName("savebackup_btn")
        self.gridLayout_22.addWidget(self.savebackup_btn, 2, 0, 1, 1)
        self.backup_title_label = QtWidgets.QLabel(parent=self.backup_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_title_label.sizePolicy().hasHeightForWidth())
        self.backup_title_label.setSizePolicy(sizePolicy)
        self.backup_title_label.setMinimumSize(QtCore.QSize(0, 27))
        self.backup_title_label.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;
border: none;
margin-bottom: 10%;
""")
        self.backup_title_label.setObjectName("backup_title_label")
        self.gridLayout_22.addWidget(self.backup_title_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.backup_frame)
        self.parameters_frame = QtWidgets.QFrame(parent=self.settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_frame.sizePolicy().hasHeightForWidth())
        self.parameters_frame.setSizePolicy(sizePolicy)
        self.parameters_frame.setMinimumSize(QtCore.QSize(0, 120))
        self.parameters_frame.setStyleSheet("""border: none;
border-radius: 0;
border-top: 1px solid #3e3e42;
""")
        self.parameters_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.parameters_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.parameters_frame.setObjectName("parameters_frame")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.parameters_frame)
        self.gridLayout_23.setContentsMargins(0, -1, 0, 8)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.parameter_1_chechbox = QtWidgets.QCheckBox(parent=self.parameters_frame)
        self.parameter_1_chechbox.setStyleSheet("""QCheckBox {
    border: none;
    background-color: none;
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
QCheckBox::indicator {
    width: 12px;
    height: 12px;
    border: 1px solid #858585;
    border-radius: 4%;
    background: #3b3b3b;
}
QCheckBox::indicator:checked {
    background-color: #48b585;
}
QCheckBox::indicator:hover {
    border-color: #acacac;
}""")
        self.parameter_1_chechbox.setObjectName("parameter_1_chechbox")
        self.gridLayout_23.addWidget(self.parameter_1_chechbox, 2, 0, 1, 1)
        self.parameters_title_label = QtWidgets.QLabel(parent=self.parameters_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_title_label.sizePolicy().hasHeightForWidth())
        self.parameters_title_label.setSizePolicy(sizePolicy)
        self.parameters_title_label.setMinimumSize(QtCore.QSize(0, 30))
        self.parameters_title_label.setStyleSheet("""border: none;
color: white;
font-size: 15px;
font-weight: 700;""")
        self.parameters_title_label.setObjectName("parameters_title_label")
        self.gridLayout_23.addWidget(self.parameters_title_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.parameters_frame)
        self.dangerzone_frame = QtWidgets.QFrame(parent=self.settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dangerzone_frame.sizePolicy().hasHeightForWidth())
        self.dangerzone_frame.setSizePolicy(sizePolicy)
        self.dangerzone_frame.setStyleSheet("""border: none;
border-radius: 0;
border-top: 1px solid #3e3e42;""")
        self.dangerzone_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dangerzone_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dangerzone_frame.setObjectName("dangerzone_frame")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.dangerzone_frame)
        self.gridLayout_24.setContentsMargins(0, -1, 0, 12)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.dangerzone_title_label = QtWidgets.QLabel(parent=self.dangerzone_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dangerzone_title_label.sizePolicy().hasHeightForWidth())
        self.dangerzone_title_label.setSizePolicy(sizePolicy)
        self.dangerzone_title_label.setMinimumSize(QtCore.QSize(0, 30))
        self.dangerzone_title_label.setStyleSheet("""border: none;
font-size: 15px;
font-weight: 700;
color: #DC2626;""")
        self.dangerzone_title_label.setObjectName("dangerzone_title_label")
        self.gridLayout_24.addWidget(self.dangerzone_title_label, 0, 0, 1, 1)
        self.dangerzone_deleteall_btn = QtWidgets.QPushButton(parent=self.dangerzone_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dangerzone_deleteall_btn.sizePolicy().hasHeightForWidth())
        self.dangerzone_deleteall_btn.setSizePolicy(sizePolicy)
        self.dangerzone_deleteall_btn.setMinimumSize(QtCore.QSize(0, 20))
        self.dangerzone_deleteall_btn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dangerzone_deleteall_btn.setStyleSheet("""QPushButton {
    border: none;
    background-color: #d13c30;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #af3025;
}""")
        deleteall_icon = self.get_icon("delete-icon.png")
        self.dangerzone_deleteall_btn.setIcon(deleteall_icon)
        self.dangerzone_deleteall_btn.setIconSize(QtCore.QSize(14, 14))
        self.dangerzone_deleteall_btn.setObjectName("dangerzone_deleteall_btn")
        self.gridLayout_24.addWidget(self.dangerzone_deleteall_btn, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.dangerzone_frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.settings_grid.addWidget(self.settings_frame, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.settings_grid.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_18.addLayout(self.settings_grid, 0, 0, 1, 1)
        self.main_stackedwidget.addWidget(self.settings_page)
        self.notes_page = QtWidgets.QWidget()
        self.notes_page.setObjectName("notes_page")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.notes_page)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.notes_grid = QtWidgets.QGridLayout()
        self.notes_grid.setContentsMargins(12, 10, 12, 14)
        self.notes_grid.setObjectName("notes_grid")
        self.notes_title_label = QtWidgets.QLabel(parent=self.notes_page)
        self.notes_title_label.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;""")
        self.notes_title_label.setObjectName("notes_title_label")
        self.notes_grid.addWidget(self.notes_title_label, 2, 0, 1, 1)
        self.notes_deleteall_btn = QtWidgets.QPushButton(parent=self.notes_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes_deleteall_btn.sizePolicy().hasHeightForWidth())
        self.notes_deleteall_btn.setSizePolicy(sizePolicy)
        self.notes_deleteall_btn.setMinimumSize(QtCore.QSize(80, 20))
        self.notes_deleteall_btn.setStyleSheet("""QPushButton {
    background-color: #d13c30;
    border-radius: 8%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #af3025;
}""")
        self.notes_deleteall_btn.setObjectName("notes_deleteall_btn")
        self.notes_grid.addWidget(self.notes_deleteall_btn, 2, 1, 1, 1)
        self.editor_frame = QtWidgets.QFrame(parent=self.notes_page)
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
        self.editor_save_btn = QtWidgets.QPushButton(parent=self.editor_frame)
        self.editor_save_btn.setMinimumSize(QtCore.QSize(0, 20))
        self.editor_save_btn.setStyleSheet("""QPushButton {
    background-color: #48b585;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #38936c;
}""")
        self.editor_save_btn.setIcon(save_icon)
        self.editor_save_btn.setIconSize(QtCore.QSize(19, 19))
        self.editor_save_btn.setObjectName("editor_save_btn")
        self.gridLayout_4.addWidget(self.editor_save_btn, 2, 0, 1, 1)
        self.editor_lineedit = QtWidgets.QLineEdit(parent=self.editor_frame)
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
        self.editor_clear_btn = QtWidgets.QPushButton(parent=self.editor_frame)
        self.editor_clear_btn.setMinimumSize(QtCore.QSize(0, 20))
        self.editor_clear_btn.setStyleSheet("""QPushButton {
    background-color: #52525a;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #3e3e42;
}""")
        self.editor_clear_btn.setIcon(deleteall_icon)
        self.editor_clear_btn.setObjectName("editor_clear_btn")
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
        self.editor_plaintextedit.setBackgroundVisible(False)
        self.editor_plaintextedit.setCenterOnScroll(False)
        self.editor_plaintextedit.setObjectName("editor_plaintextedit")
        self.gridLayout_4.addWidget(self.editor_plaintextedit, 1, 0, 1, 2)
        self.notes_grid.addWidget(self.editor_frame, 1, 0, 1, 2)
        self.notes_listwidget = QtWidgets.QListWidget(parent=self.notes_page)
        self.notes_listwidget.setStyleSheet("""QListWidget {
    background-color: #252525;
    border: 1px solid #3e3e42;
    padding: 4px 8px;
    border-radius: 15%;
}""")
        self.notes_listwidget.setObjectName("notes_listwidget")
        self.notes_grid.addWidget(self.notes_listwidget, 3, 0, 1, 2)
        self.note_title_label = QtWidgets.QLabel(parent=self.notes_page)
        self.note_title_label.setMinimumSize(QtCore.QSize(0, 20))
        self.note_title_label.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;""")
        self.note_title_label.setObjectName("note_title_label")
        self.notes_grid.addWidget(self.note_title_label, 0, 0, 1, 2)
        self.gridLayout_20.addLayout(self.notes_grid, 0, 0, 1, 1)
        self.main_stackedwidget.addWidget(self.notes_page)
        self.history_page = QtWidgets.QWidget()
        self.history_page.setObjectName("history_page")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.history_page)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.history_grid = QtWidgets.QGridLayout()
        self.history_grid.setContentsMargins(12, 10, 12, 55)
        self.history_grid.setObjectName("history_grid")
        self.history_title_label = QtWidgets.QLabel(parent=self.history_page)
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
        self.history_clear_btn = QtWidgets.QPushButton(parent=self.history_page)
        self.history_clear_btn.setMinimumSize(QtCore.QSize(90, 20))
        self.history_clear_btn.setStyleSheet("""QPushButton {
    background-color: #d13c30;
    border-radius: 8%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}
QPushButton:hover {
    background-color: #af3025;
}""")
        self.history_clear_btn.setIcon(deleteall_icon)
        self.history_clear_btn.setObjectName("history_clear_btn")
        self.history_grid.addWidget(self.history_clear_btn, 0, 1, 1, 1)
        self.history_listwidget = QtWidgets.QListWidget(parent=self.history_page)
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
        self.main_stackedwidget.addWidget(self.history_page)
        self.main_grid.addWidget(self.main_stackedwidget, 0, 0, 1, 1)
        self.main.addLayout(self.main_grid, 0, 0, 1, 1)
        self.body.addWidget(self.main_frame, 0, 1, 1, 1)
        self.body.setColumnStretch(0, 1)
        self.body.setColumnStretch(1, 4)
        self.gridLayout_6.addLayout(self.body, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_stackedwidget.setCurrentWidget(self.stopwatch_page)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer()
        self.date_edit = QDateEdit()
        self.load_stopwatch_notes()
        self.load_notes_history()
        self.load_calendar_history()
        self.user_setting = {self.parameter_1_chechbox.objectName(): self.parameter_1_chechbox.isChecked()}
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_settings")
            rows = cursor.fetchall()
        if rows == []:
            for k, v in self.user_setting.items():
                self.load_setting_to_db(k, v)
        self.load_user_settings()
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalenTrack"))
        self.app_title_label.setText(_translate("MainWindow", "CalenTrack"))
        self.stopwatch_btn.setText(_translate("MainWindow", "Stopwatch"))
        self.history_btn.setText(_translate("MainWindow", "History"))
        self.notes_btn.setText(_translate("MainWindow", "Notes"))
        self.calendar_btn.setText(_translate("MainWindow", "Calendar"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.stopwatch_time_label.setText(_translate("MainWindow", "00:00:00, 00"))
        self.stopwatch_start_stop_btn.setText(_translate("MainWindow", "Start"))
        self.stopwatch_reset_btn.setText(_translate("MainWindow", "Reset"))
        self.stopwatch_save_btn.setText(_translate("MainWindow", "Save"))
        self.dates_title.setText(_translate("MainWindow", "Dates"))
        self.dates_deleteall_btn.setText(_translate("MainWindow", "Delete all"))
        self.calendar_title_label.setText(_translate("MainWindow", "Calendar"))
        self.settings_title_label.setText(_translate("MainWindow", "Settings"))
        self.loadbackup_btn.setText(_translate("MainWindow", "Load backup"))
        self.savebackup_btn.setText(_translate("MainWindow", "Save backup"))
        self.backup_title_label.setText(_translate("MainWindow", "Backup"))
        self.parameter_1_chechbox.setText(_translate("MainWindow", "Open stopwatch when you establish time from history"))
        self.parameters_title_label.setText(_translate("MainWindow", "Parameters"))
        self.dangerzone_title_label.setText(_translate("MainWindow", "Danger zone"))
        self.dangerzone_deleteall_btn.setText(_translate("MainWindow", "Delete all data"))
        self.notes_title_label.setText(_translate("MainWindow", "Notes"))
        self.notes_deleteall_btn.setText(_translate("MainWindow", "Delete all"))
        self.editor_save_btn.setText(_translate("MainWindow", "Save"))
        self.editor_lineedit.setPlaceholderText(_translate("MainWindow", "Title"))
        self.editor_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.editor_plaintextedit.setPlaceholderText(_translate("MainWindow", "Text..."))
        self.note_title_label.setText(_translate("MainWindow", "New note"))
        self.history_title_label.setText(_translate("MainWindow", "History"))
        self.history_clear_btn.setText(_translate("MainWindow", "Clear"))

    def add_functions(self):
        self.page_mapping = {
            self.stopwatch_btn: self.stopwatch_page,
            self.history_btn: self.history_page,
            self.notes_btn: self.notes_page,
            self.calendar_btn: self.calendar_page,
            self.settings_btn: self.settings_page
        }
        for btn, page in self.page_mapping.items():
            btn.clicked.connect(lambda checked, p=page: self.show_page(p))
        self.stopwatch_start_stop_btn.clicked.connect(self.start_stop_stopwatch)
        self.stopwatch_reset_btn.clicked.connect(self.reset_stopwatch)
        self.stopwatch_save_btn.clicked.connect(self.add_to_history_stopwatch)
        self.timer.timeout.connect(self.update_time)
        self.history_clear_btn.clicked.connect(lambda: self.del_all_stopwatch_history() if self.check_user_permission_delete() == True else None)
        self.notes_deleteall_btn.clicked.connect(lambda: self.del_all_notes_history() if self.check_user_permission_delete() == True else None)
        self.editor_save_btn.clicked.connect(self.save_note)
        self.editor_clear_btn.clicked.connect(self.del_note)
        self.calendarwidget.clicked.connect(self.calendar_dialog)
        self.dates_deleteall_btn.clicked.connect(lambda: self.del_all_calendar_history() if self.check_user_permission_delete() == True else None)
        self.savebackup_btn.clicked.connect(self.save_backup)
        self.loadbackup_btn.clicked.connect(self.load_backup)
        self.parameter_1_chechbox.clicked.connect(self.read_user_setting_value)
        self.dangerzone_deleteall_btn.clicked.connect(lambda: self.del_all_data() if self.check_user_permission_delete() == True else None)

    def load_stopwatch_notes(self):
        """Stopwatch method"""
        self.history_listwidget.clear()
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, note FROM stopwatch_history ORDER BY id")
            rows = cursor.fetchall()
            for index, (row_id, note_text) in enumerate(rows):
                item = QListWidgetItem()    
                item.setData(QtCore.Qt.ItemDataRole.UserRole, row_id)
                self.history_listwidget.addItem(item)
                widget = QtWidgets.QWidget()
                item.setSizeHint(QtCore.QSize(0, 28)) 
                if index == 0:
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
    background-color: #252525;
    border-top: 1px solid #3e3e42;
}
QWidget:hover {
    background-color: #2d2d2d;
}""")
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(2, 1, 1, 1)
                label = QtWidgets.QLabel(note_text)
                label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
                layout.addWidget(label)
                set_new_stopwatch_btn = QtWidgets.QPushButton("Establish")
                set_new_stopwatch_btn.setStyleSheet("""QPushButton {
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
                set_new_stopwatch_btn.setFixedSize(60, 18)
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
                layout.addWidget(set_new_stopwatch_btn)
                layout.addWidget(del_button)
                widget.setLayout(layout)
                self.history_listwidget.setItemWidget(item, widget)
                del_button.clicked.connect(lambda _, it=item: self.del_history(it) if self.check_user_permission_delete() == True else None)
                with sqlite3.connect(self.path_to_db) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT time_note FROM stopwatch_history WHERE id = ?", (row_id,))
                    note_time = cursor.fetchone()
                set_new_stopwatch_btn.clicked.connect(lambda _, nt=note_time[0]: self.set_new_time_stopwatch(nt))

    def del_history(self, item):
        """Stopwatch method"""
        if item is not None:
            note_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row = self.history_listwidget.row(item)
            self.history_listwidget.takeItem(row)
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stopwatch_history WHERE id = ?", (note_id,))
                conn.commit()

    def set_new_time_stopwatch(self, stopwatch_text: str):
        """Stopwatch method"""
        hh, mm, ss, = stopwatch_text.split(":")
        ss, ms = ss.split(", ")
        self.stopwatch_start_stop_btn.setText("Start")
        self.timer.stop()
        self.time = QTime(int(hh), int(mm), int(ss), int(ms) * 10)
        self.stopwatch_time_label.setText(stopwatch_text)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT objectValue FROM user_settings WHERE objectName = 'parameter_1_chechbox'")
            row = cursor.fetchall()
        if row[0][0] == 1:
            self.main_stackedwidget.setCurrentWidget(self.stopwatch_page)

    def start_stop_stopwatch(self):
        """Stopwatch method"""
        if self.stopwatch_start_stop_btn.text() == "Start":
            self.timer.start(10)
            self.stopwatch_start_stop_btn.setText("Stop")
            self.stopwatch_start_stop_btn.setIcon(self.get_icon("stop-icon.png"))
        else:
            self.timer.stop()
            self.stopwatch_start_stop_btn.setText("Start")
            self.stopwatch_start_stop_btn.setIcon(self.get_icon("start-icon.png"))

    def reset_stopwatch(self):
        """Stopwatch method"""
        self.stopwatch_start_stop_btn.setText("Start")
        self.stopwatch_start_stop_btn.setIcon(self.get_icon("start-icon.png"))
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.stopwatch_time_label.setText(self.format_time(self.time))

    def add_to_history_stopwatch(self):
        """Stopwatch method"""
        item = QListWidgetItem()
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
        data = self.date_edit.date().currentDate().toString("dd-MM-yyyy")
        note_time = self.stopwatch_time_label.text()
        note_text = f"{data}  {QTime.currentTime().toString('hh:mm')} | {note_time}"
        label = QtWidgets.QLabel(note_text)
        label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
        layout.addWidget(label)
        set_new_stopwatch_btn = QtWidgets.QPushButton("Establish")
        set_new_stopwatch_btn.setStyleSheet("""QPushButton {
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
        set_new_stopwatch_btn.setFixedSize(60, 18)
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
        layout.addWidget(set_new_stopwatch_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.history_listwidget.setItemWidget(item, widget)
        note_id = self.add_stopwatch_note_to_db(note_text, note_time)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        del_button.clicked.connect(lambda: self.del_history(item) if self.check_user_permission_delete() == True else None)
        set_new_stopwatch_btn.clicked.connect(lambda: self.set_new_time_stopwatch(note_time))

    def add_stopwatch_note_to_db(self, note, time_note):
        """Stopwatch method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stopwatch_history (note, time_note) VALUES (?, ?)", (note, time_note))
            conn.commit()
            return cursor.lastrowid

    def del_all_stopwatch_history(self):
        """Stopwatch method"""
        self.history_listwidget.clear()
        with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stopwatch_history")
                conn.commit()

    def update_time(self):
        """Stopwatch method"""
        self.time = self.time.addMSecs(10)
        self.stopwatch_time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        """Stopwatch method"""        
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}, {(time.msec() // 10):02d}"

    def load_notes_history(self):
        """Notes method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title FROM notes ORDER BY id")
            rows = cursor.fetchall()
            for index, (id, note_title) in enumerate(rows):
                item = QListWidgetItem()
                item.setSizeHint(QtCore.QSize(0, 28))
                item.setData(QtCore.Qt.ItemDataRole.UserRole, id)
                self.notes_listwidget.addItem(item)
                widget = QtWidgets.QWidget()
                if index == 0:
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
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(2, 1, 1, 1)
                label = QtWidgets.QLabel(note_title)
                layout.addWidget(label)
                label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
                edit_btn = QtWidgets.QPushButton("Edit")
                edit_btn.setStyleSheet("""QPushButton {
    background-color: #eea138;
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
    background-color: #d17b2b !important;
}""")
                edit_btn.setFixedSize(60, 18)
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
                layout.addWidget(edit_btn)
                layout.addWidget(del_button)
                widget.setLayout(layout)
                self.notes_listwidget.setItemWidget(item, widget)                
                del_button.clicked.connect(lambda _, it=item: self.del_note_history(it) if self.check_user_permission_delete() == True else None)
                edit_btn.clicked.connect(lambda _, it=item: self.reduct_note(it.data(QtCore.Qt.ItemDataRole.UserRole)))

    def del_note_history(self, item):
        """Notes method"""
        if item is not None:
            note_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row = self.notes_listwidget.row(item)
            self.notes_listwidget.takeItem(row)
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                conn.commit()

    def reduct_note(self, item):
        """Notes method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, text FROM notes WHERE id = ?", (item,))
            rows = cursor.fetchall()
        self.editor_lineedit.setText(rows[0][0])
        self.editor_plaintextedit.setPlainText(rows[0][1])

    def del_all_notes_history(self):
        """Notes method"""
        self.notes_listwidget.clear()
        with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notes")
                conn.commit()

    def save_note(self):
        """Notes method"""
        if self.editor_lineedit.text() == "":
            self.message_error_none_title()
        else:
            self.add_to_history_notes(title=self.editor_lineedit.text())

    def message_error_none_title(self):
        """Notes method"""
        new_window = QMessageBox()
        new_window.setWindowTitle("CalenTrack | Error")
        new_window.setWindowIcon(self.get_icon("app-logo.ico"))
        new_window.setText("Error!\nTitle don't have any name")
        new_window.setIcon(QMessageBox.Icon.Warning)
        new_window.setStandardButtons(QMessageBox.StandardButton.Ok)
        new_window.setStyleSheet("""QMessageBox {
    background-color: #252525;
    border: 1px solid #3e3e42;
}
QMessageBox QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
QPushButton {
    background-color: #48b585;
    border-radius: 4px;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
    padding: 5px 10px;
    min-width: 50px;
    border: none;
}
QPushButton:hover {
    background-color: #38936c;
}
""")
        new_window.exec()

    def add_to_history_notes(self, title):
        """Notes method"""
        item = QListWidgetItem()
        item.setSizeHint(QtCore.QSize(0, 28))
        self.notes_listwidget.addItem(item)
        widget = QtWidgets.QWidget()
        if self.notes_listwidget.count() == 1:
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
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 1, 1)
        label = QtWidgets.QLabel(title)
        label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
        edit_btn = QtWidgets.QPushButton("Edit")
        edit_btn.setFixedSize(60, 18)
        edit_btn.setStyleSheet("""QPushButton {
    background-color: #eea138;
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
    background-color: #d17b2b !important;
}""")
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
        layout.addWidget(label)
        layout.addWidget(edit_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.notes_listwidget.setItemWidget(item, widget)
        row = self.notes_listwidget.row(item)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM notes WHERE title = ?", (title,))
            rows = cursor.fetchall()
        if rows and rows[0][0] == title:
            self.notes_listwidget.takeItem(row)
        note_id = self.add_notes_note_to_db(self.editor_plaintextedit.toPlainText(), self.editor_lineedit.text())
        self.editor_lineedit.clear()
        self.editor_plaintextedit.clear()
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        edit_btn.clicked.connect(lambda: self.reduct_note(item.data(QtCore.Qt.ItemDataRole.UserRole)))
        del_button.clicked.connect(lambda: self.del_note_history(item) if self.check_user_permission_delete() == True else None)

    def add_notes_note_to_db(self, text, title):
        """Notes method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM notes WHERE title = ?", (title,)) 
            try:
                if cursor.fetchall()[0][0] == title:
                    cursor.execute("UPDATE notes SET text = ? WHERE title = ?", (text, title))
            except:
                cursor.execute("INSERT INTO notes (title, text) VALUES (?, ?)", (title, text))
            conn.commit()
            return cursor.lastrowid

    def del_note(self):
        """Notes method"""
        self.editor_lineedit.clear()
        self.editor_plaintextedit.clear()

    def load_calendar_history(self):
        """Calendar Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, date, date_color FROM calendar ORDER BY id")
            rows = cursor.fetchall()
            for index, (id, date, date_color) in enumerate(rows):
                format = QtGui.QTextCharFormat()
                format.setBackground(QtGui.QColor(date_color))
                self.calendarwidget.setDateTextFormat(QDate.fromString(date, "dd-MM-yyyy"), format)
                item = QListWidgetItem()
                item.setSizeHint(QtCore.QSize(0, 28))
                item.setData(QtCore.Qt.ItemDataRole.UserRole, id)
                self.dates_listwidget.addItem(item)
                widget = QtWidgets.QWidget()
                if index == 0:
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
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(2, 1, 1, 1)
                label = QtWidgets.QLabel(date)
                label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
                open_btn = QtWidgets.QPushButton("View")
                open_btn.setStyleSheet("""QPushButton {
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
                open_btn.setFixedSize(60, 18)
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
                layout.addWidget(label)
                layout.addWidget(open_btn)
                layout.addWidget(del_button)
                widget.setLayout(layout)
                item.setData(QtCore.Qt.ItemDataRole.UserRole, id)
                self.dates_listwidget.setItemWidget(item, widget)                
                open_btn.clicked.connect(lambda _, it=item:  self.view_calendar_data_date(it.data(QtCore.Qt.ItemDataRole.UserRole)))
                del_button.clicked.connect(lambda _, it=item: self.del_calendar_history(it) if self.check_user_permission_delete() == True else None)

    def view_calendar_data_date(self, id):
        """Calendar Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT date, stopwatch_note, note_title, note_text FROM calendar WHERE id = ?", (id,))
            rows = cursor.fetchall()
        date, stopwatch_note, note_title, note_text = rows[0]
        self.dialog_window_datas = QtWidgets.QDialog()
        self.dialog_window_datas.setWindowIcon(self.get_icon("app-logo.ico"))
        self.dialog_window_datas.setWindowTitle(f"CalenTrack | {date}")
        self.dialog_window_datas.setObjectName("dialog")
        self.dialog_window_datas.resize(400, 300)
        self.dialog_window_datas.setMinimumSize(QtCore.QSize(280, 250))
        self.dialog_window_datas.setStyleSheet("""QDialog {
    background-color: #252525;
    border: 1px solid #3e3e42;
}""")
        self.dialog_gridlayout = QtWidgets.QGridLayout(self.dialog_window_datas)
        self.dialog_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_gridlayout.setSpacing(0)
        self.dialog_gridlayout.setObjectName("dialog_gridlayout")
        self.dialog_main_gridlayout = QtWidgets.QGridLayout()
        self.dialog_main_gridlayout.setContentsMargins(10, 12, 10, 8)
        self.dialog_main_gridlayout.setObjectName("dialog_main_gridlayout")
        self.dialog_title_lineedit = QtWidgets.QLineEdit(parent=self.dialog_window_datas)
        self.dialog_title_lineedit.setPlaceholderText("Not selected")
        if note_title != "None":
            self.dialog_title_lineedit.setText(note_title)
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
        self.dialog_time_lineedit = QtWidgets.QLineEdit(parent=self.dialog_window_datas)
        self.dialog_time_lineedit.setPlaceholderText("Not selected")
        if stopwatch_note != "None":
            self.dialog_time_lineedit.setText(stopwatch_note)
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
        self.dialog_plaintextedit = QtWidgets.QPlainTextEdit(parent=self.dialog_window_datas)
        self.dialog_plaintextedit.setPlaceholderText("Not selected")
        if note_text != "None":
                self.dialog_plaintextedit.setPlainText(note_text)
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
        self.dialog_buttonBox = QtWidgets.QDialogButtonBox(parent=self.dialog_window_datas)
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
        self.dialog_buttonBox.rejected.connect(self.dialog_window_datas.reject)
        self.dialog_buttonBox.accepted.connect(self.dialog_window_datas.accept)
        QtCore.QMetaObject.connectSlotsByName(self.dialog_window_datas)
        self.dialog_window_datas.show()

    def del_calendar_history(self, item):
        """Calendar Method"""
        if item is not None:
            note_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row = self.dates_listwidget.row(item)
            self.dates_listwidget.takeItem(row)
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT date FROM calendar WHERE id = ?", (note_id,))
                row = cursor.fetchone()[0]
                text_format = QtGui.QTextCharFormat()
                text_format.setBackground(QtGui.QColor("#252525"))
                date = QDate.fromString(row, "dd-MM-yyyy")
                self.calendarwidget.setDateTextFormat(date, text_format)
                cursor.execute("DELETE FROM calendar WHERE id = ?", (note_id,))
                conn.commit()

    def calendar_dialog(self):
        """Calendar Method"""
        self.dialog_window_choose_datas = QtWidgets.QDialog()
        self.dialog_window_choose_datas.setWindowIcon(self.get_icon("app-logo.ico"))
        self.dialog_window_choose_datas.setObjectName("Dialog")
        self.dialog_window_choose_datas.setWindowTitle("CalenTrack | Choose data")
        self.dialog_window_choose_datas.resize(400, 300)
        self.dialog_window_choose_datas.setStyleSheet("""QDialog {
    background-color: #252525;
    border: 1px solid #3e3e42;
}""")
        self.dialog_gridlayout = QtWidgets.QGridLayout(self.dialog_window_choose_datas)
        self.dialog_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.dialog_gridlayout.setSpacing(0)
        self.dialog_gridlayout.setObjectName("dialog_gridlayout")
        self.dialog_main_gridlayout = QtWidgets.QGridLayout()
        self.dialog_main_gridlayout.setContentsMargins(10, 12, 10, 8)
        self.dialog_main_gridlayout.setSpacing(0)
        self.dialog_main_gridlayout.setObjectName("dialog_main_gridlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.dialog_main_gridlayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.dialog_main_gridlayout.addItem(spacerItem1, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.dialog_main_gridlayout.addItem(spacerItem2, 11, 0, 1, 1)
        self.dialog_time_label = QtWidgets.QLabel("Select time:", parent=self.dialog_window_choose_datas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_time_label.sizePolicy().hasHeightForWidth())
        self.dialog_time_label.setSizePolicy(sizePolicy)
        self.dialog_time_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.dialog_time_label.setObjectName("dialog_time_label")
        self.dialog_main_gridlayout.addWidget(self.dialog_time_label, 0, 0, 1, 1)
        self.dialog_color_pushbutton = QtWidgets.QPushButton(parent=self.dialog_window_choose_datas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_color_pushbutton.sizePolicy().hasHeightForWidth())
        self.dialog_color_pushbutton.setSizePolicy(sizePolicy)
        self.dialog_color_pushbutton.setMinimumSize(QtCore.QSize(0, 20))
        self.dialog_color_pushbutton.setStyleSheet("""QPushButton {
    background-color: #252525;
    border: 1px solid #777777;
}
QPushButton:focus {
    border: none;
    outline: none;
}""")
        self.dialog_color_pushbutton.setText("")
        self.dialog_color_pushbutton.setObjectName("dialog_color_pushbutton")
        self.dialog_main_gridlayout.addWidget(self.dialog_color_pushbutton, 10, 0, 1, 1)
        self.dialog_note_label = QtWidgets.QLabel("Select note:", parent=self.dialog_window_choose_datas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_note_label.sizePolicy().hasHeightForWidth())
        self.dialog_note_label.setSizePolicy(sizePolicy)
        self.dialog_note_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.dialog_note_label.setObjectName("dialog_note_label")
        self.dialog_main_gridlayout.addWidget(self.dialog_note_label, 4, 0, 1, 1)
        self.dialog_color_label = QtWidgets.QLabel("Color date:", parent=self.dialog_window_choose_datas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_color_label.sizePolicy().hasHeightForWidth())
        self.dialog_color_label.setSizePolicy(sizePolicy)
        self.dialog_color_label.setStyleSheet("""QLabel {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}""")
        self.dialog_color_label.setObjectName("dialog_color_label")
        self.dialog_main_gridlayout.addWidget(self.dialog_color_label, 8, 0, 1, 1)
        self.dialog_buttonbox = QtWidgets.QDialogButtonBox(parent=self.dialog_window_choose_datas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_buttonbox.sizePolicy().hasHeightForWidth())
        self.dialog_buttonbox.setSizePolicy(sizePolicy)
        self.dialog_buttonbox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.dialog_buttonbox.setStyleSheet("""QPushButton {
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
QPushButton[text=\"Apply\"] {
        background-color: #48b585;
}
QPushButton[text=\"Discard\"] {
    background-color: #d13c30;
}
QPushButton[text=\"Apply\"]:hover {
    background-color: #38936c;
}
QPushButton[text=\"Discard\"]:hover {
    background-color: #af3025;
}""")
        self.dialog_buttonbox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dialog_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Apply|QtWidgets.QDialogButtonBox.StandardButton.Discard)
        self.dialog_buttonbox.setCenterButtons(False)
        self.dialog_buttonbox.setObjectName("dialog_buttonbox")
        self.dialog_main_gridlayout.addWidget(self.dialog_buttonbox, 12, 0, 1, 1)
        self.dialog_note_combobox = QtWidgets.QComboBox(parent=self.dialog_window_choose_datas)
        self.dialog_note_combobox.setMinimumSize(QtCore.QSize(0, 20))
        self.dialog_note_combobox.setStyleSheet("""QComboBox {
    color: #fff;
    font-weight: 700;
    background-color: #3e3e42;
    font-size: 12px;
    border-radius: 4%;
}
QComboBox QAbstractItemView {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 4px;
    outline: none;
    color: #fff;    
}""")
        self.dialog_note_combobox.setObjectName("dialog_note_combobox")
        self.dialog_main_gridlayout.addWidget(self.dialog_note_combobox, 6, 0, 1, 1)
        self.dialog_time_combobox = QtWidgets.QComboBox(parent=self.dialog_window_choose_datas)
        self.dialog_time_combobox.setMinimumSize(QtCore.QSize(0, 20))
        self.dialog_time_combobox.setStyleSheet("""QComboBox {
    color: #fff;
    font-weight: 700;
    background-color: #3e3e42;
    font-size: 12px;
    border-radius: 4%;
}
QComboBox QAbstractItemView {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 4px;
    outline: none;
    color: #fff;    
}""")
        self.dialog_time_combobox.setObjectName("dialog_time_combobox")
        self.dialog_main_gridlayout.addWidget(self.dialog_time_combobox, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.dialog_main_gridlayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.dialog_main_gridlayout.addItem(spacerItem4, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.dialog_main_gridlayout.addItem(spacerItem5, 9, 0, 1, 1)
        self.dialog_gridlayout.addLayout(self.dialog_main_gridlayout, 0, 0, 1, 1)

        self.dialog_buttonbox.accepted.connect(self.dialog_window_choose_datas.accept)
        self.dialog_buttonbox.rejected.connect(self.dialog_window_choose_datas.reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog_window_choose_datas)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT note FROM stopwatch_history")
            stopwatch_times = cursor.fetchall()
            cursor.execute("SELECT title FROM notes")
            notes_title = cursor.fetchall()
        self.dialog_time_combobox.addItems(["None"])
        self.dialog_note_combobox.addItems(["None"])
        try:
            for i in stopwatch_times:
                self.dialog_time_combobox.addItems([i[0]])
            for i in notes_title:
                self.dialog_note_combobox.addItems([i][0])
        except:  pass
        self.my_color = "#252525"
        self.dialog_color_pushbutton.clicked.connect(self.color_dialog)
        self.dialog_apply_button = self.dialog_buttonbox.button(QtWidgets.QDialogButtonBox.StandardButton.Apply)
        self.dialog_discard_button = self.dialog_buttonbox.button(QtWidgets.QDialogButtonBox.StandardButton.Discard)
        self.dialog_apply_button.clicked.connect(self.set_date)
        self.dialog_discard_button.clicked.connect(lambda close: self.dialog_window_choose_datas.close())
        self.dialog_window_choose_datas.show()

    def color_dialog(self):
        """Calendar Method"""
        color = QtWidgets.QColorDialog.getColor()
        if not color.isValid():
            self.my_color = "#252525"
        else:
            self.my_color = color.name()
        self.dialog_color_pushbutton.setStyleSheet("""QPushButton {
    font-weight: 700;""" +
f"    background-color: {self.my_color};" +
"""    border: 1px solid #777777;
}
QPushButton:focus {
    border: none;
    outline: none;
}""")

    def set_date(self):
        """Calendar Method"""
        selected_date = self.calendarwidget.selectedDate()
        date_str = selected_date.toString("dd-MM-yyyy")
        current_formats = self.calendarwidget.dateTextFormat()
        color = QtGui.QColor(self.my_color)
        text_format = QtGui.QTextCharFormat()
        text_format.setBackground(color)
        current_formats[selected_date] = text_format
        self.calendarwidget.setDateTextFormat(selected_date, text_format)
        self.add_date_to_calendar_history(date=date_str)
        self.dialog_window_choose_datas.close()

    def add_date_to_calendar_history(self, date):
        """Calendar Method"""
        item = QListWidgetItem()
        item.setSizeHint(QtCore.QSize(0, 28))
        self.dates_listwidget.addItem(item)
        widget = QtWidgets.QWidget()
        if self.dates_listwidget.count() == 1:
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
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 1, 1)
        label = QtWidgets.QLabel(date)
        label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
        open_btn = QtWidgets.QPushButton("View")
        open_btn.setStyleSheet("""QPushButton {
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
        open_btn.setFixedSize(60, 18)
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
        layout.addWidget(label)
        del_button.setFixedSize(55, 18)
        layout.addWidget(open_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.dates_listwidget.setItemWidget(item, widget)
        row = self.dates_listwidget.row(item)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT date FROM calendar WHERE date = ?", (date,))
            rows = cursor.fetchall()
        if rows and rows[0][0] == date:
            self.dates_listwidget.takeItem(row)
        note_id = self.add_date_note_to_db(label.text())
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        open_btn.clicked.connect(lambda _, id=note_id: self.view_calendar_data_date(id))
        del_button.clicked.connect(lambda _, it=item: self.del_calendar_history(it) if self.check_user_permission_delete() == True else None)

    def add_date_note_to_db(self, date):
        """Calendar Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            if self.dialog_note_combobox.currentText() != "None":
                cursor.execute("SELECT text FROM notes WHERE title = ?", (self.dialog_note_combobox.currentText(),))
                text = cursor.fetchone()[0]
            else: text = "None"    
            cursor.execute("SELECT date FROM calendar WHERE date = ?", (date,))
            rows = cursor.fetchall()
            if rows and rows[0][0] == date:
                cursor.execute("UPDATE calendar SET stopwatch_note = ?, note_title = ?, note_text = ?, date_color = ? WHERE date = ?", (self.dialog_time_combobox.currentText(), self.dialog_note_combobox.currentText(), text, self.my_color, date))
            else:
                cursor.execute("INSERT INTO calendar (date, stopwatch_note, note_title, note_text, date_color) VALUES (?, ?, ?, ?, ?)", (date, self.dialog_time_combobox.currentText(), self.dialog_note_combobox.currentText(), text, self.my_color))
            conn.commit()
            return cursor.lastrowid

    def del_all_calendar_history(self):
        """Calendar Method"""
        self.dates_listwidget.clear()
        with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                text_format = QtGui.QTextCharFormat()
                text_format.setBackground(QtGui.QColor("#252525"))
                cursor.execute("SELECT date FROM calendar")
                rows = cursor.fetchall()
                for row in rows:
                    date = QDate.fromString(*row, "dd-MM-yyyy")
                    self.calendarwidget.setDateTextFormat(date, text_format)
                cursor.execute("DELETE FROM calendar")
                conn.commit()

    def load_setting_to_db(self, k = None, v = None):
        """Settings method"""
        if k is not None and v is not None:
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT OR REPLACE INTO user_settings (objectName, objectValue) VALUES (?, ?)", (k, v))
                conn.commit()

    def load_user_settings(self):
        """Settings method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT objectName, objectValue FROM user_settings")
            rows = cursor.fetchall()
        for row in rows:
            eval(f"self.{row[0]}.setChecked(False if row[1] == 0 else True)")

    def read_user_setting_value(self):
        """Settings method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT objectName FROM user_settings")
            rows = cursor.fetchall()
        for row in rows:
            eval(f"self.load_setting_to_db(self.{row[0]}.objectName(), self.{row[0]}.isChecked())")

    def save_backup(self):
        """Settings Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            backup = ""
            for sql in conn.iterdump():
                backup += sql
        try:
            file_path = QtWidgets.QFileDialog.getSaveFileName(self.settings_page, "Save file", "", "TXT files (*.txt)")[0]
            with open(file_path, "w", encoding="UTF-8") as file:
                file.write(backup)
        except: pass

    def load_backup(self):
        """Settings Method"""
        file_path = QtWidgets.QFileDialog.getOpenFileName(self.settings_page, "Load file", "", "TXT files (*.txt)")[0]
        if file_path != "":
            self.del_all_data()
            with open(file_path, encoding="UTF-8") as file:
                script = file.read()
            with open(self.path_to_db, "w", encoding="UTF-8") as file:
                file.write("")
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                try:
                    cursor.executescript(script)
                except:
                    with open(self.path_to_db, "w", encoding="UTF-8") as file:
                        file.write("")
                    self.create_tables()
                conn.commit()
            self.load_user_settings()
            self.load_stopwatch_notes()
            self.load_notes_history()
            self.load_calendar_history()            
        else: return

    def del_all_data(self):
        """Settings Method"""
        self.del_all_calendar_history()
        self.del_all_stopwatch_history()
        self.del_all_notes_history()
        self.reset_stopwatch()
        self.del_note()

    def show_page(self, page):
        self.main_stackedwidget.setCurrentWidget(page)

    def copy_all_resources(self, base_path):
        self.icon_path = {}
        if os.path.exists(base_path):
            for file in os.listdir(base_path):
                self.icon_path[file] = os.path.join(base_path, file)

    def get_icon(self, icon_name, mode=QtGui.QIcon.Mode.Normal, state=QtGui.QIcon.State.Off):
        if hasattr(self, "icon_path"):
            if icon_name in self.icon_path:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.icon_path[icon_name]), mode, state)
                return icon

    def create_tables(self):
        """Database Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.executescript("""CREATE TABLE IF NOT EXISTS stopwatch_history
                            (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            note TEXT NOT NULL,
                            time_note TEXT NOT NULL
                            );
                            CREATE TABLE IF NOT EXISTS notes
                            (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            text TEXT NOT NULL
                            );
                            CREATE TABLE IF NOT EXISTS calendar
                            (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT NOT NULL,
                            stopwatch_note TEXT,
                            note_title TEXT,
                            note_text TEXT,
                            date_color TEXT
                            );
                            CREATE TABLE IF NOT EXISTS user_settings
                            (
                            objectName TEXT NOT NULL UNIQUE,
                            objectValue BOOL NOT NULL
                            );""")

    def check_database_integrity(self):
        """Database Method"""
        if not os.path.exists(self.path_to_db):
            return False
        try:
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = cursor.fetchall()
                print(f"Database valid, tables found: {len(tables)}")
                return True
        except sqlite3.DatabaseError as e:
            print(f"Database corrupted: {e}")
            return False
        except Exception as e:
            print(f"Error checking database: {e}")
            return False

    def check_user_permission_delete(self):
        self.delete_dialog = QtWidgets.QDialog()
        self.delete_dialog.setWindowTitle("CalenTrack | Delete data")
        self.delete_dialog.setWindowIcon(self.get_icon("app-logo.ico"))
        self.delete_dialog.setObjectName("delete_dialog")
        self.delete_dialog.resize(412, 300)
        self.delete_dialog.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.delete_dialog.setStyleSheet("""QDialog {
    background-color: #252525;
    border: 1px solid #3e3e42;
}""")
        self.delete_dialog_gridlayout = QtWidgets.QGridLayout(self.delete_dialog)
        self.delete_dialog_gridlayout.setContentsMargins(0, 0, 0, 0)
        self.delete_dialog_gridlayout.setSpacing(0)
        self.delete_dialog_gridlayout.setObjectName("delete_dialog_gridlayout")
        self.delete_dialog_main_gridlayout = QtWidgets.QGridLayout()
        self.delete_dialog_main_gridlayout.setContentsMargins(-1, 4, -1, 4)
        self.delete_dialog_main_gridlayout.setObjectName("delete_dialog_main_gridlayout")
        self.delete_dialog_buttonbox = QtWidgets.QDialogButtonBox(parent=self.delete_dialog)
        self.delete_dialog_buttonbox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.delete_dialog_buttonbox.setStyleSheet("""QPushButton {
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
        self.delete_dialog_buttonbox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.delete_dialog_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.No|QtWidgets.QDialogButtonBox.StandardButton.Yes)
        self.delete_dialog_buttonbox.setCenterButtons(True)
        self.delete_dialog_buttonbox.setObjectName("delete_dialog_buttonbox")
        self.delete_dialog_main_gridlayout.addWidget(self.delete_dialog_buttonbox, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.delete_dialog_main_gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self.delete_dialog_pushbutton = QtWidgets.QPushButton(parent=self.delete_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_dialog_pushbutton.sizePolicy().hasHeightForWidth())
        self.delete_dialog_pushbutton.setSizePolicy(sizePolicy)
        self.delete_dialog_pushbutton.setText("")
        self.delete_dialog_pushbutton.setIcon(self.get_icon("are_you_sure.webp"))
        self.delete_dialog_pushbutton.setIconSize(QtCore.QSize(400, 225))
        self.delete_dialog_pushbutton.setShortcut("")
        self.delete_dialog_pushbutton.setAutoDefault(True)
        self.delete_dialog_pushbutton.setDefault(False)
        self.delete_dialog_pushbutton.setFlat(True)
        self.delete_dialog_pushbutton.setObjectName("delete_dialog_pushbutton")
        self.delete_dialog_main_gridlayout.addWidget(self.delete_dialog_pushbutton, 1, 0, 1, 1)
        self.delete_dialog_gridlayout.addLayout(self.delete_dialog_main_gridlayout, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self.delete_dialog)
        self.status_delete = False
        self.delete_dialog_buttonbox.accepted.connect(lambda: self.set_status_delete(True) or self.delete_dialog.close())
        self.delete_dialog_buttonbox.rejected.connect(lambda: self.set_status_delete(False) or self.delete_dialog.close())
        self.delete_dialog.exec()
        return self.status_delete

    def set_status_delete(self, status_bool: bool):
        self.status_delete = status_bool

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
