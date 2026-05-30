from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 670)
        MainWindow.setMinimumSize(QtCore.QSize(480, 580))
        logo_icon = QtGui.QIcon()
        logo_icon.addPixmap(QtGui.QPixmap("resources/app-logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.app_title_label.setStyleSheet("color: #8B5CF6;\nborder: none;\nfont-size: 19px;\nfont-weight: 600;\nborder-bottom: 1px solid #3e3e42;")
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
        stopwatch_icon = QtGui.QIcon()
        stopwatch_icon.addPixmap(QtGui.QPixmap("resources/stopwatch-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        history_icon = QtGui.QIcon()
        history_icon.addPixmap(QtGui.QPixmap("resources/history-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        notes_icon = QtGui.QIcon()
        notes_icon.addPixmap(QtGui.QPixmap("resources/note-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        calendar_icon = QtGui.QIcon()
        calendar_icon.addPixmap(QtGui.QPixmap("resources/calendar-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        settings_icon = QtGui.QIcon()
        settings_icon.addPixmap(QtGui.QPixmap("resources/settings-icons.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
font-size: 32px;
font-weight: 600;
color: #D4D4D4;""")
        self.stopwatch_time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.stopwatch_time_label.setObjectName("stopwatch_time_label")
        self.gridLayout_2.addWidget(self.stopwatch_time_label, 0, 0, 1, 2)
        self.stopwatch_stop_btn = QtWidgets.QPushButton(parent=self.stopwatch_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopwatch_stop_btn.sizePolicy().hasHeightForWidth())
        self.stopwatch_stop_btn.setSizePolicy(sizePolicy)
        self.stopwatch_stop_btn.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(87)
        self.stopwatch_stop_btn.setFont(font)
        self.stopwatch_stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.stopwatch_stop_btn.setStyleSheet("""QPushButton {
    background-color: #8365ee;
    border-radius: 6%;
    color: #fff;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:hover {
    background-color: #7349e5;
}""")
        self.stopwatch_stop_btn.setText("Stop")
        pause_icon = QtGui.QIcon()
        pause_icon.addPixmap(QtGui.QPixmap("resources/pause-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.stopwatch_stop_btn.setIcon(pause_icon)
        self.stopwatch_stop_btn.setIconSize(QtCore.QSize(15, 15))
        self.stopwatch_stop_btn.setShortcut("")
        self.stopwatch_stop_btn.setCheckable(False)
        self.stopwatch_stop_btn.setObjectName("stopwatch_stop_btn")
        self.gridLayout_2.addWidget(self.stopwatch_stop_btn, 1, 0, 1, 1)
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
QPushButton:hover {
    background-color: #3e3e42;
}""")
        reset_icon = QtGui.QIcon()
        reset_icon.addPixmap(QtGui.QPixmap("resources/reset-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
QPushButton:hover {
    background-color: #38936c;
}""")
        save_icon = QtGui.QIcon()
        save_icon.addPixmap(QtGui.QPixmap("resources/save-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
QPushButton:hover {
    background-color: #af3025;
}""")
        self.dates_deleteall_btn.setObjectName("dates_deleteall_btn")
        self.gridLayout_8.addWidget(self.dates_deleteall_btn, 0, 1, 1, 1)
        self.dates_listwidget = QtWidgets.QListWidget(parent=self.dates_frame)
        self.dates_listwidget.setStyleSheet("border: none;")
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
QCalendarWidget QToolButton#qt_calendar_prevmonth {
    qproperty-icon: url("resources/left-arrow-icon.png");
}
QCalendarWidget QToolButton#qt_calendar_nextmonth {
    qproperty-icon: url("resources/right-arrow-icon.png");
}
QCalendarWidget QAbstractItemView {
    background-color: #252525;
    selection-background-color: #1a1a1a;
    outline: none;
    font-size: 12px;
    font-weight: 600;
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
}""")
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
QPushButton:hover {
    background-color: #3e3e42;
    border: 1px solid #52525a;
}
""")
        loadbackup_icon = QtGui.QIcon()
        loadbackup_icon.addPixmap(QtGui.QPixmap("resources/export-icons.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
QPushButton:hover {
    background-color: #38936c;
}""")
        savebackup_icon = QtGui.QIcon()
        savebackup_icon.addPixmap(QtGui.QPixmap("resources/import-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
QPushButton:hover {
    background-color: #af3025;
}""")
        deleteall_icon = QtGui.QIcon()
        deleteall_icon.addPixmap(QtGui.QPixmap("resources/delete-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.notes_listwidget.setStyleSheet("""background-color: #252525;
border: 1px solid #3e3e42;
border-radius: 15%;""")
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
QPushButton:hover {
    background-color: #af3025;
}""")
        self.history_clear_btn.setIcon(deleteall_icon)
        self.history_clear_btn.setObjectName("history_clear_btn")
        self.history_grid.addWidget(self.history_clear_btn, 0, 1, 1, 1)
        self.history_listwidget = QtWidgets.QListWidget(parent=self.history_page)
        self.history_listwidget.setMinimumSize(QtCore.QSize(0, 486))
        self.history_listwidget.setStyleSheet("""background-color: #252525;
border: 1px solid #3e3e42;
border-radius: 15%;""")
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
        self.main_stackedwidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.main_stackedwidget.setCurrentWidget(self.stopwatch_page)
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalenTrack"))
        self.app_title_label.setText(_translate("MainWindow", "CalenTrack"))
        self.stopwatch_btn.setText(_translate("MainWindow", "Timer"))
        self.history_btn.setText(_translate("MainWindow", "History"))
        self.notes_btn.setText(_translate("MainWindow", "Notes"))
        self.calendar_btn.setText(_translate("MainWindow", "Calendar"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.stopwatch_time_label.setText(_translate("MainWindow", "00:00:00, 00"))
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

    def show_page(self, page):
        self.main_stackedwidget.setCurrentWidget(page)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
