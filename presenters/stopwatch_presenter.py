from PyQt6.QtCore import QTime, QTimer
from PyQt6 import QtWidgets


class StopwatchPresenter:
    def __init__(self, view: QtWidgets.QWidget, history_view: QtWidgets.QWidget, model):
        self.view: QtWidgets.QWidget = view
        self.history_view: QtWidgets.QWidget = history_view
        self.model = model
        self.view.start_clicked.connect(self._toggle)
        self.view.reset_clicked.connect(self._reset_stopwatch)
        self.view.save_clicked.connect(self._save_to_history)
        self._time: QTime = QTime(0, 0, 0, 0)
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
        self._time = QTime(0, 0, 0, 0)
        self.view.update_time(self._format_time(self._time))

    def _update_time(self) -> None:
        self._time = self._time.addMSecs(10)
        self.view.update_time(self._format_time(self._time))

    def _format_time(self, time: QTime) -> str:
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}, {(time.msec() // 10):02d}"

    def _save_to_history(self) -> None:
        date: str = self._date.date().currentDate().toString("dd-MM-yyyy")
        real_time: str = self._time.currentTime().toString("hh:mm")
        stopwatch_time: str = self.view.get_time()
        data: str = f"{date}  {real_time} | {stopwatch_time}"
        rowid: int = self.model.add_stopwatch_note(data, stopwatch_time)
        self.history_view.add_item(data, stopwatch_time, rowid)

    def set_time(self, time: str) -> None:
        hh, mm, ss = time.split(":")
        ss, ms = ss.split(", ")
        self._time = QTime(int(hh), int(mm), int(ss), int(ms) * 10)
        self.view.update_time(self._format_time(self._time))
        self._stop_stopwatch()