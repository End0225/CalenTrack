from PyQt6 import QtCore, QtWidgets, QtGui
from utils.button_factory import ButtonFactory


class CalendarView(QtWidgets.QWidget):
    calendar_clicked = QtCore.pyqtSignal()
    deleteall_clicked = QtCore.pyqtSignal()
    view_date_clicked = QtCore.pyqtSignal(int)
    del_item_clicked = QtCore.pyqtSignal(QtWidgets.QListWidgetItem)

    def __init__(self, icon_manager, calendar_dialog: QtWidgets.QDialog, date_dialog: QtWidgets.QDialog):
        super().__init__()
        self.icon_manager = icon_manager
        self.calendar_dialog = calendar_dialog
        self.date_dialog = date_dialog
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
        self.dates_deleteall_btn.clicked.connect(self.deleteall_clicked.emit)
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
        self.calendarwidget.clicked.connect(self.calendar_clicked.emit)
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

    def add_item(self, date: str, id: int, check_date: bool) -> None:
        item = QtWidgets.QListWidgetItem()
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
        if check_date:
            self.dates_listwidget.takeItem(row)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, id)
        open_btn.clicked.connect(lambda: self.view_date_clicked.emit(id))
        del_button.clicked.connect(lambda: self.del_item_clicked.emit(item))

    def add_date(self, date: QtCore.QDate, color: str) -> None:
        current_formats = self.calendarwidget.dateTextFormat()
        qcolor: QtGui.QColor = QtGui.QColor(color)
        text_format: QtGui.QTextCharFormat = QtGui.QTextCharFormat()
        text_format.setBackground(qcolor)
        current_formats[date] = text_format
        self.calendarwidget.setDateTextFormat(date, text_format)

    def get_listwidget_row(self, item: QtWidgets.QListWidgetItem) -> int:
        return self.dates_listwidget.row(item)

    def listwidget_takeitem(self, item: QtWidgets.QListWidgetItem, date: str) -> None:
        row = self.get_listwidget_row(item)
        self.dates_listwidget.takeItem(row)
        text_format = QtGui.QTextCharFormat()
        text_format.setBackground(QtGui.QColor("#252525"))
        date: QtCore.QDate = QtCore.QDate.fromString(date, "dd-MM-yyyy")
        self.calendarwidget.setDateTextFormat(date, text_format)

    def open_calendar_dialog(self, stopwatch_times: list[str], notes_titles: list[str]) -> None:
        self.calendar_dialog.run(stopwatch_times, notes_titles, self.calendarwidget.selectedDate())

    def open_date_dialog(self, date: str, stopwatch_note: str, note_title: str, note_text: str) -> None:
        self.date_dialog.load_data(date, stopwatch_note, note_title, note_text)
        self.date_dialog.run()

    def clear_all(self) -> None:
        self.dates_listwidget.clear()

    def get_item_by_id(self, target_id: int) -> int:
        for row in range(self.dates_listwidget.count()):
            item = self.dates_listwidget.item(row)
            if item.data(QtCore.Qt.ItemDataRole.UserRole) == target_id:
                return item