from PyQt6 import QtCore, QtWidgets


class NotesPresenter:
    def __init__(self, view: QtWidgets.QWidget, model):
        self.view = view
        self.model = model
        self.view.deleteall_clicked.connect(self._del_notes)
        self.view.save_clicked.connect(self._save_note)
        self.view.clear_clicked.connect(self._clear_note)
        self.view.del_item_clicked.connect(self._del_note)
        self.view.reduct_item_clicked.connect(self._open_note)

    def _del_notes(self) -> None:
        self.model.del_notes()
        self.view.clear_all()

    def _save_note(self) -> None:
        title: str = self.view.get_title() # TODO: add check length
        check_note: bool = self.model.check_title(title)
        text: str = self.view.get_text()
        id: int = self.model.add_note(title, text)
        self.view.add_item(title, id, check_note)

    def _clear_note(self) -> None:
        self.view.clear_note()

    def _del_note(self, item: QtWidgets.QListWidgetItem) -> None:
        note_id: int = item.data(QtCore.Qt.ItemDataRole.UserRole)
        row: int = self.view.get_listwidget_row(item)
        self.view.listwidget_takeitem(row)
        self.model.del_note(note_id)

    def _open_note(self, id: int) -> None:
        note: list[str, str] = self.model.get_note(id)
        title, text = note
        self.view.set_note(title, text)

    def load_notes(self) -> None:
        self.view.clear_all()
        notes: list[int, str] = self.model.get_notes()
        for id, title in notes:
            self.view.add_item(title, id, False)