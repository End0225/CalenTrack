from PyQt6 import QtCore, QtWidgets


class HistoryPresenter:
    def __init__(self, view, stopwatch_presenter, main_view, model):
        self.view = view
        self.stopwatch_presenter = stopwatch_presenter
        self.main_view = main_view
        self.model = model
        self.view.del_item_clicked.connect(self._on_del_item)
        self.view.establish_item_clicked.connect(self._on_establish_item)

    def _on_del_item(self, item: QtWidgets.QListWidgetItem):
        note_id: int = item.data(QtCore.Qt.ItemDataRole.UserRole)
        row: int = self.view.get_listwidget_row(item)
        self.view.listwidget_takeitem(row)
        self.model.delete_stopwatch_record(note_id)

    def _on_establish_item(self, time: str):
        self.stopwatch_presenter.set_time(time)