from PyQt6 import QtCore, QtWidgets
from typing import Callable


class HistoryPresenter:
    def __init__(self, view: QtWidgets.QWidget, stopwatch_presenter, confirm_dialog: QtWidgets.QDialog, show_stopwatch_page: Callable[[], None], model):
        self.view = view
        self.stopwatch_presenter = stopwatch_presenter
        self.confirm_dialog: QtWidgets.QDialog = confirm_dialog
        self.show_stopwatch_page: Callable[[], None] = show_stopwatch_page
        self.model = model
        self.view.del_item_clicked.connect(self._on_del_item)
        self.view.establish_item_clicked.connect(self._on_establish_item)
        self.view.clear_all_clicked.connect(self._on_del_all_items)
        self.permission: bool
        self.confirm_dialog.confirmation_clicked.connect(self._toggle_permission)

    def load_history(self) -> None:
        self.view.clear_all()
        history: list[int, str, str] = self.model.get_history()
        for row_id, note_text, note_time in history:
            self.view.add_item(note_text, note_time, row_id)

    def _toggle_permission(self, status: bool) -> None:
        self.permission = status

    def _on_del_item(self, item: QtWidgets.QListWidgetItem) -> None:
        self.confirm_dialog.run()
        if self.permission:
            note_id: int = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row: int = self.view.get_listwidget_row(item)
            self.view.listwidget_takeitem(row)
            self.model.delete_stopwatch_record(note_id)

    def _on_establish_item(self, time: str) -> None:
        self.stopwatch_presenter.set_time(time)
        if self.model.check_parameter_1():
            self.show_stopwatch_page()

    def _on_del_all_items(self, show_dialog: bool = True) -> None:
        if show_dialog:
            self.confirm_dialog.run()
            if not self.permission:
                return
        self.model.clear_stopwatch_history()
        self.view.clear_all()