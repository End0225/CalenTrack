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
from utils.icon_manager import IconManager


class Application:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.copy_paths()
        self.setup_icon_manager()
        self.setup_ui()
        self.preload_history()

    def copy_paths(self) -> None:
        if getattr(sys, "frozen", False):
            app_dir = os.path.join(os.getenv("APPDATA"), "CalenTrack")
            os.makedirs(app_dir, exist_ok=True)
            self.db_path = os.path.join(app_dir, "app_db.db")
            self.icon_path = os.path.join(app_dir, "resources", "icons")
            os.makedirs(self.icon_path, exist_ok=True)
            src_icons_dir = os.path.join(sys._MEIPASS, "resources", "icons")
            if os.path.exists(src_icons_dir):
                for file in os.listdir(src_icons_dir):
                    src = os.path.join(src_icons_dir, file)
                    dst = os.path.join(self.icon_path, file)
                    if not os.path.exists(dst):
                        shutil.copyfile(src, dst)
            src_db = os.path.join(sys._MEIPASS, "app_db.db")
            if not os.path.exists(self.db_path):
                if os.path.exists(src_db):
                    shutil.copyfile(src_db, self.db_path)
                else:
                    self.model = DatabaseModel(self.db_path)
                    self.model.create_tables()
        else:
            self.db_path = os.path.join(os.path.dirname(__file__), "app_db.db")
            self.icon_path = os.path.join(os.path.dirname(__file__), "resources", "icons")
            self.model = DatabaseModel(self.db_path)
        if not os.path.exists(self.db_path) or not self.model.check_database_integrity():
            self.model.create_tables()

    def setup_icon_manager(self) -> None:
        self.icon_manager = IconManager(self.icon_path)
        self.icon_manager.copy_all_resources()

    def setup_ui(self) -> None:
        self.view = MainWindowView(self.icon_manager)
        view_widgets = {
            "stopwatch_view": StopwatchView(self.icon_manager),
            "history_view": HistoryView(self.icon_manager),
            "notes_view": NotesView(self.icon_manager),
            "calendar_view": CalendarView(self.icon_manager),
            "settings_view": SettingsView(self.icon_manager)
        }
        for name, widget in view_widgets.items():
            self.view.add_page(name, widget)

        self.stopwatch_presenter = StopwatchPresenter(view_widgets["stopwatch_view"], view_widgets["history_view"], self.view, self.model)
        self.history_presenter = HistoryPresenter(view_widgets["history_view"], self.stopwatch_presenter, self.view, self.model)

        self.view.show_page(view_widgets["stopwatch_view"], self.view.buttons["stopwatch_view"])

    def preload_history(self) -> None:
        pass

    def run(self) -> None:
        self.view.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    application = Application()
    application.run()