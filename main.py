from PyQt6 import QtWidgets
import sys
import os
import shutil
from model.database import DatabaseModel
from views.main_window import MainWindowView
from views.stopwatch_view import StopwatchView
from views.history_view import HistoryView
from views.notes_view import NotesView
from views.calendar_view import CalendarView
from views.settings_view import SettingsView
from presenters.stopwatch_presenter import StopwatchPresenter
from presenters.history_presenter import HistoryPresenter
from presenters.notes_presenter import NotesPresenter
from presenters.calendar_presenter import CalendarPresenter
from views.dialogs.calendar_dialog import CalendarDialog
from views.dialogs.color_dialog import ColorDialog
from views.dialogs.date_dialog import DateDialog
from utils.icon_manager import IconManager


class Application:
    def __init__(self):
        self.app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
        self.copy_paths()
        self.setup_icon_manager()
        self.setup_ui()
        self.preload_data()

    def copy_paths(self) -> None:
        if getattr(sys, "frozen", False):
            app_dir: str = os.path.join(os.getenv("APPDATA"), "CalenTrack")
            os.makedirs(app_dir, exist_ok=True)
            self.db_path: str = os.path.join(app_dir, "app_db.db")
            self.icon_path: str = os.path.join(app_dir, "resources", "icons")
            os.makedirs(self.icon_path, exist_ok=True)
            src_icons_dir: str = os.path.join(sys._MEIPASS, "resources", "icons")
            if os.path.exists(src_icons_dir):
                for file in os.listdir(src_icons_dir):
                    src: str = os.path.join(src_icons_dir, file)
                    dst: str = os.path.join(self.icon_path, file)
                    if not os.path.exists(dst):
                        shutil.copyfile(src, dst)
            src_db: str = os.path.join(sys._MEIPASS, "app_db.db")
            if not os.path.exists(self.db_path):
                if os.path.exists(src_db):
                    shutil.copyfile(src_db, self.db_path)
                else:
                    self.model: DatabaseModel = DatabaseModel(self.db_path)
                    self.model.create_tables()
        else:
            self.db_path: str = os.path.join(os.path.dirname(__file__), "app_db.db")
            self.icon_path: str = os.path.join(os.path.dirname(__file__), "resources", "icons")
            self.model: DatabaseModel = DatabaseModel(self.db_path)
        if not os.path.exists(self.db_path) or not self.model.check_database_integrity():
            self.model.create_tables()

    def setup_icon_manager(self) -> None:
        self.icon_manager: IconManager = IconManager(self.icon_path)
        self.icon_manager.copy_all_resources()

    def setup_ui(self) -> None:
        self.view: MainWindowView = MainWindowView(self.icon_manager)
        dialogs: dict[str, QtWidgets.QDialog] = {
            "color_dialog": ColorDialog(self.icon_manager),
            "date_dialog": DateDialog(self.icon_manager)
        }
        dialogs["calendar_dialog"] = CalendarDialog(self.icon_manager, dialogs["color_dialog"])
        view_widgets: dict[str, QtWidgets.QWidget] = {
            "stopwatch_view": StopwatchView(self.icon_manager),
            "history_view": HistoryView(self.icon_manager),
            "notes_view": NotesView(self.icon_manager),
            "calendar_view": CalendarView(self.icon_manager, dialogs["calendar_dialog"], dialogs["date_dialog"]),
            "settings_view": SettingsView(self.icon_manager)
        }
        for name, widget in view_widgets.items():
            self.view.add_page(name, widget)

        self.stopwatch_presenter: StopwatchPresenter = StopwatchPresenter(view_widgets["stopwatch_view"], view_widgets["history_view"], self.model)
        self.history_presenter: HistoryPresenter = HistoryPresenter(view_widgets["history_view"], self.stopwatch_presenter, self.model)
        self.notes_presenter: NotesPresenter = NotesPresenter(view_widgets["notes_view"], self.model)
        self.calendar_presenter: CalendarPresenter = CalendarPresenter(view_widgets["calendar_view"], dialogs["calendar_dialog"], self.model)

        self.view.show_page(view_widgets["stopwatch_view"], self.view.buttons["stopwatch_view"])

    def preload_data(self) -> None:
        self.history_presenter.load_history()
        self.notes_presenter.load_notes()
        self.calendar_presenter.load_dates()

    def run(self) -> None:
        self.view.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    application: Application = Application()
    application.run()