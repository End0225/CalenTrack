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
from utils.icon_manager import IconManager


def main():
    app = QtWidgets.QApplication(sys.argv)

    if getattr(sys, "frozen", False):
        app_dir = os.path.join(os.getenv("APPDATA"), "CalenTrack")
        os.makedirs(app_dir, exist_ok=True)
        db_path = os.path.join(app_dir, "app_db.db")
        icon_path = os.path.join(app_dir, "resources", "icons")
        os.makedirs(icon_path, exist_ok=True)
        src_icons_dir = os.path.join(sys._MEIPASS, "resources", "icons")
        if os.path.exists(src_icons_dir):
            for file in os.listdir(src_icons_dir):
                src = os.path.join(src_icons_dir, file)
                dst = os.path.join(icon_path, file)
                if not os.path.exists(dst):
                    shutil.copyfile(src, dst)
        src_db = os.path.join(sys._MEIPASS, "app_db.db")
        if not os.path.exists(db_path):
            if os.path.exists(src_db):
                shutil.copyfile(src_db, db_path)
            else:
                model = DatabaseModel(db_path)
                model.create_tables()
    else:
        db_path = os.path.join(os.path.dirname(__file__), "app_db.db")
        icon_path = os.path.join(os.path.dirname(__file__), "resources", "icons")
        model = DatabaseModel(db_path)
    if not os.path.exists(db_path) or not model.check_database_integrity():
        model.create_tables()
    icon_manager = IconManager(icon_path)
    icon_manager.copy_all_resources()

    view = MainWindowView(icon_manager)
    view_widgets = {
        "stopwatch_view": StopwatchView(icon_manager),
        "history_view": HistoryView(icon_manager),
        "notes_view": NotesView(icon_manager),
        "calendar_view": CalendarView(icon_manager)
    }
    for name, widget in view_widgets.items():
        view.add_page(name, widget)

    view.show_page(view_widgets["stopwatch_view"], view.buttons["stopwatch_view"])
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()