import sqlite3
import os


class DatabaseModel:
    def __init__(self, path: str):
        self.path: str = path

    def create_tables(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.executescript("""CREATE TABLE IF NOT EXISTS stopwatch_history
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT NOT NULL,
    time_note TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS notes
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    text TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS calendar
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    stopwatch_note TEXT,
    note_title TEXT,
    note_text TEXT,
    date_color TEXT
);
CREATE TABLE IF NOT EXISTS user_settings
(
    objectName TEXT NOT NULL UNIQUE,
    objectValue BOOL NOT NULL
);""")

    def check_database_integrity(self) -> bool:
        if not os.path.exists(self.path):
            return False
        try:
            with sqlite3.connect(self.path) as conn:
                cursor: sqlite3.Cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = cursor.fetchall()
                print(f"Database valid, tables found: {len(tables)}")
                return True
        except sqlite3.DatabaseError as e:
            print(f"Database corrupted: {e}")
            return False
        except Exception as e:
            print(f"Error checking database: {e}")
            return False

    # ==== Stopwatch =====
    def add_stopwatch_note(self, note_text: str, note_time: str) -> int | None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("INSERT INTO stopwatch_history (note, time_note) VALUES (?, ?)", (note_text, note_time))
            conn.commit()
            return cursor.lastrowid

    # ==== History =====
    def delete_stopwatch_record(self, note_id: int) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM stopwatch_history WHERE id = ?", (note_id,))
            conn.commit()

    def clear_stopwatch_history(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM stopwatch_history")
            conn.commit()

    def get_history(self) -> list[int, str, str]:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, note, time_note FROM stopwatch_history ORDER BY id")
            return cursor.fetchall()

    def get_times(self) -> list[str]:
        history: list[int, str, str] = self.get_history()
        return [i[1] for i in history]

    # ==== Notes =====
    def add_note(self, title: str, text: str) -> int:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT title FROM notes WHERE title = ?", (title,))
            try:
                if cursor.fetchall()[0][0] == title:
                    cursor.execute("UPDATE notes SET text = ? WHERE title = ?", (text, title))
            except:
                cursor.execute("INSERT INTO notes (title, text) VALUES (?, ?)", (title, text))
            conn.commit()
            return cursor.lastrowid

    def check_title(self, title: str) -> bool:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT title FROM notes WHERE title = ?", (title,))
            rows = cursor.fetchall()
            if rows and rows[0][0] == title:
                return True
            else:
                return False

    def del_notes(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM notes")
            conn.commit()

    def del_note(self, id: int) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
            conn.commit()

    def get_note(self, id: int) -> list[str, str]:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT title, text FROM notes WHERE id = ?", (id,))
            return cursor.fetchall()[0]

    def get_notes(self) -> list[int, str]:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, title FROM notes ORDER BY id")
            return cursor.fetchall()

    def get_titles(self) -> list[str]:
        notes = self.get_notes()
        return [i[1] for i in notes]

    # ==== Calendar =====
    def add_date(self, date: str, time: str, note: str, color: str) -> int:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            if note != "None":
                cursor.execute("SELECT text FROM notes WHERE title = ?", (note,))
                text = cursor.fetchone()[0]
            else:
                text = "None"
            cursor.execute("SELECT date FROM calendar WHERE date = ?", (date,))
            rows = cursor.fetchall()
            if rows and rows[0][0] == date:
                cursor.execute("UPDATE calendar SET stopwatch_note = ?, note_title = ?, note_text = ?, date_color = ? WHERE date = ?", (time, note, text, color, date))
            else:
                cursor.execute("INSERT INTO calendar (date, stopwatch_note, note_title, note_text, date_color) VALUES (?, ?, ?, ?, ?)", (date, time, note, text, color))
            conn.commit()
            return cursor.lastrowid

    def check_date(self, date: str) -> bool:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT date FROM calendar WHERE date = ?", (date,))
            rows = cursor.fetchall()
            if rows and rows[0][0] == date:
                return True
            else:
                return False

    def del_date(self, id: int) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM calendar WHERE id = ?", (id, ))
            conn.commit()

    def get_date(self, id: int) -> str:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT date FROM calendar WHERE id = ?", (id, ))
            return cursor.fetchone()[0]

    def get_date_data(self, id: int) -> tuple[str, str, str, str]:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT date, stopwatch_note, note_title, note_text FROM calendar WHERE id = ?", (id, ))
            return cursor.fetchall()[0]

    def get_dates(self) -> list[tuple[int, str, str]]:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT id, date, date_color FROM calendar ORDER BY id")
            return cursor.fetchall()

    def del_dates(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM calendar")
            conn.commit()

    def get_dates_dates(self) -> list[tuple[int, str]]:
        data: list[tuple[int, str, str]] = self.get_dates()
        dates: list[tuple[int, str]] = []
        for id, date, color in data:
            dates.append((id, date))
        return dates

    # ==== Settings =====
    def get_backup(self) -> str:
        with sqlite3.connect(self.path) as conn:
            backup: str = ""
            for sql in conn.iterdump():
                backup += sql
            return backup

    def load_data(self, file_path: tuple[str, str]) -> None:
        with open(file_path, encoding="UTF-8") as file:
            script: str = file.read()
        with open(self.path, "w", encoding="UTF-8") as file:
            file.write("")
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            try:
                cursor.executescript(script)
            except:
                with open(self.path, "w", encoding="UTF-8") as file:
                    file.write("")
                self.create_tables()
            conn.commit()

    def get_settings(self) -> list[tuple[str, bool]]:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT objectName, objectValue FROM user_settings")
            return cursor.fetchall()

    def toggle_setting(self, name: str, status: bool) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO user_settings (objectName, objectValue) VALUES (?, ?)", (name, status))
            conn.commit()

    def reset_settings(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("DELETE FROM user_settings")
            conn.commit()

    def check_parameter_1(self) -> bool:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT objectValue FROM user_settings WHERE objectName = 'parameter_1_checkbox'")
            return bool(cursor.fetchone()[0])

    def check_parameter_2(self) -> bool:
        with sqlite3.connect(self.path) as conn:
            cursor: sqlite3.Cursor = conn.cursor()
            cursor.execute("SELECT objectValue FROM user_settings WHERE objectName = 'parameter_2_checkbox'")
            return bool(cursor.fetchone()[0])