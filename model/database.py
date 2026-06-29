import sqlite3
import os


class DatabaseModel:
    def __init__(self, path):
        self.path = path

    def create_tables(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
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
                cursor = conn.cursor()
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
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stopwatch_history (note, time_note) VALUES (?, ?)", (note_text, note_time))
            conn.commit()
            return cursor.lastrowid

    # ==== History =====
    def delete_stopwatch_record(self, note_id: int) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM stopwatch_history WHERE id = ?", (note_id,))
            conn.commit()

    def clear_stopwatch_history(self) -> None:
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM stopwatch_history")
            conn.commit()

    def get_history(self) -> list[int, str, str]:
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, note, time_note FROM stopwatch_history ORDER BY id")
            return cursor.fetchall()

    # ==== Notes =====
    # ==== Calendar =====
    # ==== Settings =====