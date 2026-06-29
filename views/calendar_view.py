from PyQt6 import QtCore, QtWidgets
from utils.button_factory import ButtonFactory


class CalendarView(QtWidgets.QWidget):
    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory: ButtonFactory = ButtonFactory(self.icon_manager)
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setObjectName("calendar_page")
        self.gridLayout_15 = QtWidgets.QGridLayout(self)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.calendar_grid = QtWidgets.QGridLayout()
        self.calendar_grid.setContentsMargins(12, 10, 12, 14)
        self.calendar_grid.setVerticalSpacing(4)
        self.calendar_grid.setObjectName("calendar_grid")
        self.dates_frame = QtWidgets.QFrame(parent=self)
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
        self.dates_title.setText("Dates")
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
        self.dates_deleteall_btn = self.factory.get_btn(self.dates_frame, "red", "Delete all", [80, 20], QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred, None, None)
        self.gridLayout_8.addWidget(self.dates_deleteall_btn, 0, 1, 1, 1)
        self.dates_listwidget = QtWidgets.QListWidget(parent=self.dates_frame)
        self.dates_listwidget.setStyleSheet("""QListWidget {
    background-color: #252525;
    border: 1px solid #252525;
}""")
        self.dates_listwidget.setObjectName("dates_listwidget")
        self.gridLayout_8.addWidget(self.dates_listwidget, 1, 0, 1, 2)
        self.calendar_grid.addWidget(self.dates_frame, 5, 1, 1, 1)
        self.calendar_title_label = QtWidgets.QLabel(parent=self)
        self.calendar_title_label.setText("Calendar")
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
        self.calendar_frame = QtWidgets.QFrame(parent=self)
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
        self.calendarwidget.setStyleSheet(f"""QCalendarWidget QToolButton {{
    color: #fff;
    font-size: 15px;
    font-weight: bold;
    margin: 2px 5px 1px 5px;
    background-color: transparent;
}}
QCalendarWidget QToolButton#qt_calendar_prevmonth,
QCalendarWidget QToolButton#qt_calendar_nextmonth {{
        background-color: transparent;
        border-radius: 4px;
}}
QCalendarWidget QAbstractItemView {{
    background-color: #252525;
    selection-background-color: #1a1a1a;
    outline: none;
    font-size: 12px;
    font-weight: 700;
    color: #fff;
    border: none;
}}
QCalendarWidget QWidget#qt_calendar_navigationbar {{
    background-color: #252525;
}}
QCalendarWidget QMenu {{
    background-color: #252525;
    color: white;
    border: 1px solid #3e3e42;
}}
QCalendarWidget QMenu::item {{
    padding: 5px 20px;
}}
QCalendarWidget QMenu::item:selected {{
    background-color: #52525a;
    color: white;
}}
QCalendarWidget QWidget {{
    alternate-background-color: #252525;
}}
QCalendarWidget QAbstractItemView:disabled {{
    color: transparent;
}}
QCalendarWidget QToolButton#qt_calendar_prevmonth {{
    qproperty-icon: url('{self.icon_manager.icon_folder["left-arrow-icon.png"].replace('\\', '/')}');
}}
QCalendarWidget QToolButton#qt_calendar_nextmonth {{
    qproperty-icon: url('{self.icon_manager.icon_folder["right-arrow-icon.png"].replace('\\', '/')}');
}}""")
        self.calendarwidget.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.Germany))
        self.calendarwidget.setObjectName("calendarwidget")
        self.verticalLayout_2.addWidget(self.calendarwidget)
        self.calendar_grid.addWidget(self.calendar_frame, 2, 1, 1, 1)
        self.gridLayout_15.addLayout(self.calendar_grid, 0, 0, 1, 1)