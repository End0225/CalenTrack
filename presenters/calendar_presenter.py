from PyQt6 import QtCore, QtWidgets


class CalendarPresenter:
    def __init__(self, view: QtWidgets.QWidget, calendar_dialog: QtWidgets.QDialog, confirm_dialog: QtWidgets.QDialog, model):
        self.view: QtWidgets.QWidget = view
        self.model = model
        self.calendar_dialog: QtWidgets.QDialog = calendar_dialog
        self.confirm_dialog: QtWidgets.QDialog = confirm_dialog
        self.view.calendar_clicked.connect(self._open_calendar_dialog)
        self.view.deleteall_clicked.connect(self._del_dates)
        self.view.del_item_clicked.connect(self._del_date)
        self.view.view_date_clicked.connect(self._open_date_dialog)
        self.calendar_dialog.color_dialog_clicked.connect(self._open_color_dialog)
        self.calendar_dialog.apply_clicked.connect(self._save_date)
        self.permission: bool
        self.confirm_dialog.confirmation_clicked.connect(self._toggle_permission)

    def load_dates(self) -> None:
        self.view.clear_all()
        dates: list[tuple[int, str, str]] = self.model.get_dates()
        for id, date, date_color in dates:
            self.view.add_item(date, id, False)
            self.view.add_date(QtCore.QDate.fromString(date, "dd-MM-yyyy"), date_color)

    def _open_calendar_dialog(self) -> None:
        stopwatch_times: list[str] = self.model.get_times()
        notes_titles: list[str] = self.model.get_titles()
        self.view.open_calendar_dialog(stopwatch_times, notes_titles)

    def _open_color_dialog(self) -> None:
        self.calendar_dialog.open_color_dialog()

    def _toggle_permission(self, status: bool) -> None:
        self.permission = status

    def _del_dates(self, show_dialog: bool = True) -> None:
        if show_dialog:
            self.confirm_dialog.run()
            if not self.permission:
                return
        dates: list[tuple[int, str]] = self.model.get_dates_dates()
        for id, date in dates:
            item: QtWidgets.QListWidgetItem = self.view.get_item_by_id(id)
            self.view.listwidget_takeitem(item, date)
        self.model.del_dates()
        self.view.clear_all()

    def _save_date(self, date: QtCore.QDate, time: str, note: str, color: str) -> None:
        str_date: str = date.toString("dd-MM-yyyy")
        check_date: bool = self.model.check_date(str_date)
        id: int = self.model.add_date(str_date, time, note, color)
        self.view.add_item(str_date, id, check_date)
        self.view.add_date(date, color)

    def _del_date(self, item: QtWidgets.QListWidgetItem) -> None:
        self.confirm_dialog.run()
        if self.permission:
            date_id: int = item.data(QtCore.Qt.ItemDataRole.UserRole)
            date: str = self.model.get_date(date_id)
            self.view.listwidget_takeitem(item, date)
            self.model.del_date(date_id)

    def _open_date_dialog(self, id: int) -> None:
        date_data: tuple[str, str, str, str] = self.model.get_date_data(id)
        date, stopwatch_note, note_title, note_text = date_data
        self.view.open_date_dialog(date, stopwatch_note, note_title, note_text)