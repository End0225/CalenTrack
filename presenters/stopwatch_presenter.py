from PyQt6 import QtCore
from PyQt6.QtCore import QTime, QTimer
from PyQt6 import QtWidgets


class StopwatchPresenter:
    def __init__(self, view: QtWidgets.QWidget, history_view: QtWidgets.QWidget, add_tag_dialog: QtWidgets.QDialog, model):
        self.view: QtWidgets.QWidget = view
        self.history_view: QtWidgets.QWidget = history_view
        self.add_tag_dialog: QtWidgets.QDialog = add_tag_dialog
        self.model = model
        self.view.start_clicked.connect(self._toggle)
        self.view.reset_clicked.connect(self._reset_stopwatch)
        self.view.save_clicked.connect(self._save_to_history)
        self.view.open_combobox_clicked.connect(self._open_combobox)
        self.view.tag_dialog_clicked.connect(self._open_tag_dialog)
        self.add_tag_dialog.color_dialog_clicked.connect(self._open_color_dialog)
        self.add_tag_dialog.apply_clicked.connect(self._save_tag)
        self.view.tag_clicked.connect(self._tag_clicked)
        self.view.del_tag_clicked.connect(self._del_tag)
        self._time_in_ms: int = 0
        self._timer: QTimer = QTimer()
        self._date: QtWidgets.QDateEdit = QtWidgets.QDateEdit()
        self._timer.timeout.connect(self._update_time)
        self._is_running: bool = False

    def _toggle(self) -> None:
        match self._is_running:
            case False:
                self._start_stopwatch()
            case True:
                self._stop_stopwatch()

    def _start_stopwatch(self) -> None:
        self._timer.start(10)
        self.view.set_start_btn_text("Stop")
        self.view.change_start_btn_icon("stop-icon.png")
        self._is_running = True

    def _stop_stopwatch(self) -> None:
        self._timer.stop()
        self.view.set_start_btn_text("Start")
        self.view.change_start_btn_icon("start-icon.png")
        self._is_running = False

    def _reset_stopwatch(self) -> None:
        self._stop_stopwatch()
        self._time_in_ms = 0
        self.view.update_time(self._format_time(self._time_in_ms))

    def _update_time(self) -> None:
        self._time_in_ms += 10
        self.view.update_time(self._format_time(self._time_in_ms))

    def _format_time(self, ms: int) -> str:
        hours = ms // 3600000
        minutes = (ms % 3600000) // 60000
        seconds = (ms % 60000) // 1000
        milliseconds = (ms % 1000)
        return f"{hours:02}:{minutes:02}:{seconds:02}, {(milliseconds // 10):02d}"

    def _save_to_history(self) -> None:
        date: str = self._date.date().currentDate().toString("dd-MM-yyyy")
        real_time: str = QTime.currentTime().toString("hh:mm")
        stopwatch_time: str = self.view.get_time()
        data: str = f"{date}  {real_time} | {stopwatch_time}"
        rowid: int = self.model.add_stopwatch_note(data, stopwatch_time)
        self.history_view.add_item(data, stopwatch_time, rowid)

    def set_time(self, time: str) -> None:
        hh, mm, ss = time.split(":")
        ss, ms = ss.split(", ")
        self._time_in_ms = int(hh) * 3600000 + int(mm) * 60000 + int(ss) * 1000 + int(ms) * 10
        self.view.update_time(self._format_time(self._time_in_ms))        
        self._stop_stopwatch()

    def _open_combobox(self) -> None:
        x, y = self._get_combobox_coordinates()
        width: int = int(self.view.get_page_width() * 0.45)
        spacer_height: int = self.view.get_spacerItem5_height()
        x += (self.view.get_comboBox_label_width() + 12) - width - 12
        y += 5
        self.view.display_listwidget(x, y, width, spacer_height - 6)

    def _get_combobox_coordinates(self) -> tuple[int, int]:
        x: int = int(self.view.get_spacerItem1_width())
        y: int = int(8 + 25 - 1)
        return x, y

    def _open_tag_dialog(self) -> None:
        self.view.show_add_tag_dialog()

    def _open_color_dialog(self) -> None:
        self.add_tag_dialog.open_color_dialog()

    def _save_tag(self, tag_name: str, color: str) -> None:
        id: int = self.model.add_tag(tag_name, color)
        if id == -1:
            self.view.msg_err_name_already_taken(tag_name)
        else:
            self.view.add_tag(tag_name, color, id)

    def load_tags(self) -> None:
        self.view.clear_tags()
        tags: list[int, str, str] = self.model.get_tags()
        for id, name, color in tags:
            self.view.add_tag(name, color, id)

    def _tag_clicked(self, id: int) -> None:
        name, color = self.model.get_tag_by_id(id)
        self.view.set_combobox_title(name, color)

    def _del_tag(self, item: QtWidgets.QListWidgetItem) -> None:
        note_id: int = item.data(QtCore.Qt.ItemDataRole.UserRole)
        row: int = self.view.get_listwidget_row(item)
        self.view.listwidget_takeitem(row)
        self.model.del_tag(note_id)
        if not self.model.check_tag_exists():
            self.model.add_empty_tag()
            self.view.add_btn_create_tag()
            self.load_tags()