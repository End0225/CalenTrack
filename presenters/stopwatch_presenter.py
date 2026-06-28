from PyQt6.QtCore import QTime, QTimer


class StopwatchPresenter:
    def __init__(self, view, main_view, model):
        self.view = view
        self.main_view = main_view
        self.model = model
        self.view.start_clicked.connect(self._toggle)
        self.view.reset_clicked.connect(self._reset_stopwatch)
        self._time = QTime(0, 0, 0, 0)
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_time)
        self._is_running = False

    def _toggle(self):
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
