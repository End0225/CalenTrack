import shutil
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTime, QTimer, QDate
from PyQt6.QtWidgets import QDateEdit, QListWidgetItem
from PyQt6.QtWidgets import QMessageBox
import sqlite3
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        if getattr(sys, 'frozen', False):
            app_dir = os.path.join(os.getenv('APPDATA'), "CalenTrack")
            os.makedirs(app_dir, exist_ok=True)
            self.path_to_db = os.path.join(app_dir, "app_db.db")
            self.path_to_icon = os.path.join(app_dir, "icon.jpg")            
            try:
                src_db = os.path.join(sys._MEIPASS, "app_db.db")
                src_icon = os.path.join(sys._MEIPASS, "icon.jpg")
                if os.path.exists(src_db):
                    shutil.copyfile(src_db, self.path_to_db)
                else:
                    print(f"Source database not found at {src_db}")
                if os.path.exists(src_icon):
                    shutil.copyfile(src_icon, self.path_to_icon)
                else:
                    print(f"Source icon not found at {src_icon}")
            except Exception as e:
                print(f"Error copying database: {e}")
                if not os.path.exists(self.path_to_db):
                    self.create_tables()
        else:
            self.path_to_db = os.path.join(os.path.dirname(__file__), "app_db.db")
            self.path_to_icon = os.path.join(os.path.dirname(__file__), "icon.jpg")
            if not os.path.exists(self.path_to_db):
                self.create_tables()        
        if not self.check_database_integrity():
            self.create_tables()       
        self.create_tables()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(self.path_to_icon))
        MainWindow.resize(640, 673)
        MainWindow.setMinimumSize(QtCore.QSize(640, 673))
        MainWindow.setMaximumSize(QtCore.QSize(640, 673))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stopwatch_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopwatch_btn.setGeometry(QtCore.QRect(0, 0, 121, 31))
        self.stopwatch_btn.setObjectName("stopwatch_btn")
        self.notes_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.notes_btn.setGeometry(QtCore.QRect(0, 60, 121, 31))
        self.notes_btn.setObjectName("notes_btn")
        self.calendar_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calendar_btn.setGeometry(QtCore.QRect(0, 90, 121, 31))
        self.calendar_btn.setObjectName("calendar_btn")
        self.history_stopwatch_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.history_stopwatch_btn.setGeometry(QtCore.QRect(0, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.history_stopwatch_btn.setFont(font)
        self.history_stopwatch_btn.setObjectName("history_stopwatch_btn")
        self.settings_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(0, 120, 121, 31))
        self.settings_btn.setObjectName("settings_btn")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 0, 521, 681))
        self.stackedWidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.timer_page = QtWidgets.QWidget()
        self.timer_page.setObjectName("timer_page")
        self.start_stopwatch_btn = QtWidgets.QPushButton(parent=self.timer_page)
        self.start_stopwatch_btn.setGeometry(QtCore.QRect(90, 220, 91, 51))
        self.start_stopwatch_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start_stopwatch_btn.setObjectName("start_stopwatch_btn")
        self.reset_stopwatch_btn = QtWidgets.QPushButton(parent=self.timer_page)
        self.reset_stopwatch_btn.setGeometry(QtCore.QRect(200, 220, 91, 51))
        self.reset_stopwatch_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reset_stopwatch_btn.setObjectName("reset_stopwatch_btn")
        self.stopwatch_text = QtWidgets.QLabel(parent=self.timer_page)
        self.stopwatch_text.setGeometry(QtCore.QRect(130, 80, 241, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stopwatch_text.setFont(font)
        self.stopwatch_text.setStyleSheet("")
        self.stopwatch_text.setObjectName("stopwatch_text")
        self.add_to_history_btn = QtWidgets.QPushButton(parent=self.timer_page)
        self.add_to_history_btn.setGeometry(QtCore.QRect(310, 220, 91, 51))
        self.add_to_history_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_to_history_btn.setObjectName("add_to_history_btn")
        self.stackedWidget.addWidget(self.timer_page)
        self.calendar_page = QtWidgets.QWidget()
        self.calendar_page.setObjectName("calendar_page")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.calendar_page)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 6, 500, 300))
        self.calendarWidget.setStyleSheet("background-color: rgb(255, 255, 255); color: #000000;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.stackedWidget.addWidget(self.calendar_page)
        self.calendar_listwidget = QtWidgets.QListWidget(parent=self.calendar_page)
        self.calendar_listwidget.setGeometry(QtCore.QRect(10, 310, 500, 271))
        self.calendar_listwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calendar_listwidget.setObjectName("listWidget_stopwatch")
        self.del_all_calendar_history_btn = QtWidgets.QPushButton(parent=self.calendar_page)
        self.del_all_calendar_history_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.del_all_calendar_history_btn.setGeometry(QtCore.QRect(10, 596, 115, 45))
        self.del_all_calendar_history_btn.setObjectName("del_all_calendar_history_btn")
        self.del_all_calendar_history_btn.setText("Удалить все записи")
        self.timer_history_page = QtWidgets.QWidget()
        self.timer_history_page.setObjectName("timer_history_page")
        self.listwidget_stopwatch = QtWidgets.QListWidget(parent=self.timer_history_page)
        self.listwidget_stopwatch.setGeometry(QtCore.QRect(10, 6, 500, 575))
        self.listwidget_stopwatch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listwidget_stopwatch.setObjectName("listWidget_stopwatch")
        self.listwidget_del_btn = QtWidgets.QPushButton(parent=self.timer_history_page)
        self.listwidget_del_btn.setGeometry(QtCore.QRect(10, 596, 115, 45))
        self.listwidget_del_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listwidget_del_btn.setObjectName("listWidget_del_btn")
        self.stackedWidget.addWidget(self.timer_history_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.save_backup_db = QtWidgets.QPushButton("Сохранить бекап данных", parent=self.settings_page)
        self.save_backup_db.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.save_backup_db.setGeometry(QtCore.QRect(10, 5, 140, 60))
        self.save_backup_db.setObjectName("save_backup_db_btn")
        self.load_backup_db = QtWidgets.QPushButton("Загрузить бекап данных", parent=self.settings_page)
        self.load_backup_db.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.load_backup_db.setGeometry(QtCore.QRect(170, 5, 140, 60))
        self.load_backup_db.setObjectName("load_backup_db_btn")
        self.setting_1 = QtWidgets.QCheckBox(parent=self.settings_page)
        self.setting_1.setGeometry(QtCore.QRect(10, 70, 501, 40))
        self.setting_1.setObjectName("setting_1")
        self.del_all_datas = QtWidgets.QPushButton("Удалить все данные", parent=self.settings_page)
        self.del_all_datas.setGeometry(QtCore.QRect(10, 596, 115, 45))
        self.del_all_datas.setStyleSheet("background-color: #ffffff")
        self.stackedWidget.addWidget(self.settings_page)
        self.notes_page = QtWidgets.QWidget()
        self.notes_page.setObjectName("notes_page")
        self.stackedWidget.addWidget(self.notes_page)
        self.title_lineedit = QtWidgets.QLineEdit(placeholderText = "Заголовок заметки", parent=self.notes_page)
        self.title_lineedit.setGeometry(QtCore.QRect(250, 6, 260, 26))
        self.title_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.title_lineedit.setObjectName("titlelineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.notes_page)
        self.plainTextEdit.setGeometry(QtCore.QRect(250, 41, 260, 540))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("textplainTextEdit")
        self.btn_save_note = QtWidgets.QPushButton(parent=self.notes_page)
        self.btn_save_note.setGeometry(QtCore.QRect(250, 596, 115, 45))
        self.btn_save_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_save_note.setObjectName("btn_save_note")
        self.btn_save_note.setText("Сохранить")
        self.btn_del_note = QtWidgets.QPushButton(parent=self.notes_page)
        self.btn_del_note.setGeometry(QtCore.QRect(395, 596, 115, 45))
        self.btn_del_note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_del_note.setObjectName("btn_del_note")
        self.btn_del_note.setText("Очистить")
        self.listwidget_notes = QtWidgets.QListWidget(parent=self.notes_page)
        self.listwidget_notes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listwidget_notes.setGeometry(QtCore.QRect(10, 6, 230, 575))
        self.listwidget_notes.setObjectName("notes_listwidget")
        self.del_all_notes_history_btn = QtWidgets.QPushButton(parent=self.notes_page)
        self.del_all_notes_history_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.del_all_notes_history_btn.setGeometry(QtCore.QRect(10, 596, 115, 45))
        self.del_all_notes_history_btn.setObjectName("del_all_notes_history_btn")
        self.del_all_notes_history_btn.setText("Удалить все записи")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 0, 24, 673))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.stackedWidget.raise_()
        self.stopwatch_btn.raise_()
        self.notes_btn.raise_()
        self.calendar_btn.raise_()
        self.history_stopwatch_btn.raise_()
        self.settings_btn.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer()
        self.date_edit = QDateEdit()
        self.user_setting = {self.setting_1.objectName(): self.setting_1.isChecked()}
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_settings")
            rows = cursor.fetchall()
        if rows == []:
            for k, v in self.user_setting.items():
                self.load_setting_to_db(k, v)
        self.load_user_settings()
        self.load_stopwatch_notes()
        self.load_notes_history()
        self.load_calendar_history()
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalenTrack"))
        self.stopwatch_btn.setText(_translate("MainWindow", "Секундомер"))
        self.notes_btn.setText(_translate("MainWindow", "Заметки"))
        self.calendar_btn.setText(_translate("MainWindow", "Календарь"))
        self.history_stopwatch_btn.setText(_translate("MainWindow", "История секундомера"))
        self.settings_btn.setText(_translate("MainWindow", "Настройки"))
        self.start_stopwatch_btn.setText(_translate("MainWindow", "Старт"))
        self.reset_stopwatch_btn.setText(_translate("MainWindow", "Ресет"))
        self.stopwatch_text.setText(_translate("MainWindow", "00:00:00, 00"))
        self.add_to_history_btn.setText(_translate("MainWindow", "Добавить \nв историю"))
        self.setting_1.setText(_translate("MainWindow", "Открывать секундомер при установлении времени в истории секундомера"))
        self.listwidget_del_btn.setText(_translate("MainWindwo", "Удалить все записи"))

    def add_functions(self):
        self.del_all_notes_history_btn.clicked.connect(self.del_all_notes_history)
        self.btn_save_note.clicked.connect(self.save_note)
        self.btn_del_note.clicked.connect(self.del_note)
        self.setting_1.clicked.connect(self.read_user_setting_value)
        self.stopwatch_btn.clicked.connect(self.show_page1)
        self.notes_btn.clicked.connect(self.show_page2)
        self.calendar_btn.clicked.connect(self.show_page3)
        self.history_stopwatch_btn.clicked.connect(self.show_page4)
        self.settings_btn.clicked.connect(self.show_page5)
        self.start_stopwatch_btn.clicked.connect(self.start_stop_stopwatch)
        self.reset_stopwatch_btn.clicked.connect(self.reset_stopwatch)
        self.add_to_history_btn.clicked.connect(self.add_to_history_stopwatch)
        self.listwidget_del_btn.clicked.connect(self.del_all_stopwatch_history)
        self.calendarWidget.clicked.connect(self.calendar_dialog)
        self.del_all_calendar_history_btn.clicked.connect(self.del_all_calendar_history)
        self.save_backup_db.clicked.connect(self.save_backup)
        self.load_backup_db.clicked.connect(self.load_backup)
        self.del_all_datas.clicked.connect(self.del_all_data)
        self.timer.timeout.connect(self.update_time)

    def show_page1(self):
        self.stackedWidget.setCurrentWidget(self.timer_page)

    def show_page2(self):
        self.stackedWidget.setCurrentWidget(self.notes_page)

    def show_page3(self):
        self.stackedWidget.setCurrentWidget(self.calendar_page)

    def show_page4(self):
        self.stackedWidget.setCurrentWidget(self.timer_history_page)
    
    def show_page5(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.stopwatch_text.setText(self.format_time(self.time))
    
    def format_time(self, time):
        """Stopwatch method"""
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}, {f"{miliseconds:03d}".rstrip("0") or "00"}"

    def start_stop_stopwatch(self):
        """Stopwatch method"""
        if self.start_stopwatch_btn.text() == "Старт":
            self.timer.start(10)
            self.start_stopwatch_btn.setText("Стоп")
        else:
            self.timer.stop()
            self.start_stopwatch_btn.setText("Старт")

    def reset_stopwatch(self):
        """Stopwatch method"""
        self.start_stopwatch_btn.setText("Старт")
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.stopwatch_text.setText(self.format_time(self.time))

    def add_to_history_stopwatch(self):
        """Stopwatch method"""
        item = QListWidgetItem()
        self.listwidget_stopwatch.addItem(item)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 8, 1)
        data = self.date_edit.date().currentDate().toString("dd-MM-yyyy")
        note_time = self.stopwatch_text.text()
        note_text = f"{data}  {QTime.currentTime().toString('hh:mm')} | {note_time}"
        label = QtWidgets.QLabel(note_text)
        layout.addWidget(label)
        set_new_stopwatch_btn = QtWidgets.QPushButton("Установить")
        set_new_stopwatch_btn.setStyleSheet("background-color: #A7FC00;")
        set_new_stopwatch_btn.setFixedSize(70, 15)
        del_button = QtWidgets.QPushButton("Удалить")
        del_button.setStyleSheet("background-color: rgb(248,23,62);")
        del_button.setFixedSize(70, 15)
        layout.addWidget(set_new_stopwatch_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.listwidget_stopwatch.setItemWidget(item, widget)
        note_id = self.add_stopwatch_note_to_db(note_text, note_time)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        del_button.clicked.connect(lambda: self.del_history(item))
        set_new_stopwatch_btn.clicked.connect(lambda: self.set_new_time_stopwatch(note_time))

    def del_history(self, item):
        """Stopwatch method"""
        if item is not None:
            note_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row = self.listwidget_stopwatch.row(item)
            self.listwidget_stopwatch.takeItem(row)
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stopwatch_history WHERE id = ?", (note_id,))
                conn.commit()

    def add_stopwatch_note_to_db(self, note, time_note):
        """Stopwatch method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stopwatch_history (note, time_note) VALUES (?, ?)", (note, time_note))
            conn.commit()
            return cursor.lastrowid 

    def load_stopwatch_notes(self):
        """Stopwatch method"""
        self.listwidget_stopwatch.clear()
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, note FROM stopwatch_history ORDER BY id")
            rows = cursor.fetchall()
            for row_id, note_text in rows:
                item = QListWidgetItem()
                item.setData(QtCore.Qt.ItemDataRole.UserRole, row_id)
                self.listwidget_stopwatch.addItem(item)
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(2, 1, 8, 1)
                label = QtWidgets.QLabel(note_text)
                layout.addWidget(label)
                set_new_stopwatch_btn = QtWidgets.QPushButton("Установить")
                set_new_stopwatch_btn.setStyleSheet("background-color: #A7FC00;")
                set_new_stopwatch_btn.setFixedSize(70, 15)
                del_button = QtWidgets.QPushButton("Удалить")
                del_button.setStyleSheet("background-color: rgb(248,23,62);")
                del_button.setFixedSize(70, 15)
                layout.addWidget(set_new_stopwatch_btn)
                layout.addWidget(del_button)
                widget.setLayout(layout)
                self.listwidget_stopwatch.setItemWidget(item, widget)
                del_button.clicked.connect(lambda _, it=item: self.del_history(it))
                with sqlite3.connect(self.path_to_db) as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT time_note FROM stopwatch_history WHERE id = ?", (row_id,))
                    note_time = cursor.fetchone()
                set_new_stopwatch_btn.clicked.connect(lambda _, nt=note_time[0]: self.set_new_time_stopwatch(nt))

    def set_new_time_stopwatch(self, stopwatch_text: str):
        """Stopwatch method"""
        hh, mm, ss, = stopwatch_text.split(":")
        ss, ms = ss.split(", ")
        self.start_stopwatch_btn.setText("Старт")
        self.timer.stop()
        self.time = QTime(int(hh), int(mm), int(ss), int(ms) * 10)
        self.stopwatch_text.setText(stopwatch_text)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT objectValue FROM user_settings WHERE objectName = 'setting_1'")
            row = cursor.fetchall()
        if row[0][0] == 1:
            self.show_page1()

    def del_all_stopwatch_history(self):
        """Stopwatch method"""
        self.listwidget_stopwatch.clear()
        with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stopwatch_history")
                conn.commit()

    def load_setting_to_db(self, k = None, v = None):
        """Settings method"""
        if k is not None and v is not None:
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT OR REPLACE INTO user_settings (objectName, objectValue) VALUES (?, ?)", (k, v))
                conn.commit()
    
    def load_user_settings(self):
        """Settings method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT objectName, objectValue FROM user_settings")
            rows = cursor.fetchall()
        for row in rows:
            eval(f"self.{row[0]}.setChecked(False if row[1] == 0 else True)")

    def read_user_setting_value(self):
        """Settings method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT objectName FROM user_settings")
            rows = cursor.fetchall()
        for row in rows:
            eval(f"self.load_setting_to_db(self.{row[0]}.objectName(), self.{row[0]}.isChecked())")

    def save_note(self):
        """Notes method"""
        if self.title_lineedit.text() == "":
            self.message_error_none_title()
        else:
            self.add_to_history_notes(title=self.title_lineedit.text())

    def del_note(self):
        """Notes method"""
        self.title_lineedit.clear()
        self.plainTextEdit.clear()

    def message_error_none_title(self):
        """Notes method"""
        new_window = QMessageBox()
        new_window.setGeometry(950, 650, 400, 290)
        new_window.setWindowTitle("Ошибка")
        new_window.setText("Ошибка!\nПустой заголовок")
        new_window.setIcon(QMessageBox.Icon.Warning)
        new_window.setStandardButtons(QMessageBox.StandardButton.Ok)
        new_window.exec()

    def add_to_history_notes(self, title):
        """Notes method"""
        if len(title) >= 10:
            self.message_error_len_title()
            return None
        item = QListWidgetItem()
        self.listwidget_notes.addItem(item)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 2, 1)
        label = QtWidgets.QLabel(title)
        layout.addWidget(label)
        reduct_btn = QtWidgets.QPushButton("Редактировать")
        reduct_btn.setStyleSheet("background-color: #FF7F50;")
        reduct_btn.setFixedSize(83, 15)
        del_button = QtWidgets.QPushButton("Удалить")
        del_button.setStyleSheet("background-color: rgb(248,23,62);")
        del_button.setFixedSize(60, 15)
        layout.addWidget(reduct_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.listwidget_notes.setItemWidget(item, widget)
        row = self.listwidget_notes.row(item)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM notes WHERE title = ?", (title,))
            rows = cursor.fetchall()
        if rows and rows[0][0] == title:
            self.listwidget_notes.takeItem(row)
        note_id = self.add_notes_note_to_db(self.plainTextEdit.toPlainText(), self.title_lineedit.text())
        self.title_lineedit.clear()
        self.plainTextEdit.clear()
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        reduct_btn.clicked.connect(lambda: self.reduct_note(item.data(QtCore.Qt.ItemDataRole.UserRole)))
        del_button.clicked.connect(lambda: self.del_note_history(item))

    def del_note_history(self, item):
        """Notes method"""
        if item is not None:
            note_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row = self.listwidget_notes.row(item)
            self.listwidget_notes.takeItem(row)
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                conn.commit()

    def add_notes_note_to_db(self, text, title):
        """Notes method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM notes WHERE title = ?", (title,)) 
            try:
                if cursor.fetchall()[0][0] == title:
                    cursor.execute("UPDATE notes SET text = ? WHERE title = ?", (text, title))
            except:
                cursor.execute("INSERT INTO notes (title, text) VALUES (?, ?)", (title, text))
            conn.commit()
            return cursor.lastrowid

    def reduct_note(self, item):
        """Notes method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT title, text FROM notes WHERE id = ?", (item,))
            rows = cursor.fetchall()
        self.title_lineedit.setText(rows[0][0])
        self.plainTextEdit.setPlainText(rows[0][1])

    def load_notes_history(self):
        """Notes method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title FROM notes ORDER BY id")
            rows = cursor.fetchall()
            for id, note_title in rows:
                item = QListWidgetItem()
                item.setData(QtCore.Qt.ItemDataRole.UserRole, id)
                self.listwidget_notes.addItem(item)
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(2, 1, 2, 1)
                label = QtWidgets.QLabel(note_title)
                layout.addWidget(label)
                reduct_btn = QtWidgets.QPushButton("Редактировать")
                reduct_btn.setStyleSheet("background-color: #FF7F50;")
                reduct_btn.setFixedSize(83, 15)
                del_button = QtWidgets.QPushButton("Удалить")
                del_button.setStyleSheet("background-color: rgb(248,23,62);")
                del_button.setFixedSize(60, 15)
                layout.addWidget(reduct_btn)
                layout.addWidget(del_button)
                widget.setLayout(layout)
                self.listwidget_notes.setItemWidget(item, widget)                
                del_button.clicked.connect(lambda _, it=item: self.del_note_history(it))
                reduct_btn.clicked.connect(lambda _, it=item: self.reduct_note(it.data(QtCore.Qt.ItemDataRole.UserRole)))

    def del_all_notes_history(self):
        """Notes method"""
        self.listwidget_notes.clear()
        with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notes")
                conn.commit()

    def message_error_len_title(self):
        """Notes method"""
        new_window = QMessageBox()
        new_window.setGeometry(950, 650, 400, 290)
        new_window.setWindowTitle("Ошибка")
        new_window.setText("Ошибка!\nМаксимальная длина заголовка\n10 символов")
        new_window.setIcon(QMessageBox.Icon.Warning)
        new_window.setStandardButtons(QMessageBox.StandardButton.Ok)
        new_window.exec()

    def load_calendar_history(self):
        """Calendar Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, date, date_color FROM calendar ORDER BY id")
            rows = cursor.fetchall()
            for id, date, date_color in rows:
                format = QtGui.QTextCharFormat()
                format.setBackground(QtGui.QColor(date_color))
                self.calendarWidget.setDateTextFormat(QDate.fromString(date, "dd-MM-yyyy"), format)
                item = QListWidgetItem()
                self.calendar_listwidget.addItem(item)
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(2, 1, 2, 1)
                label = QtWidgets.QLabel(date)
                layout.addWidget(label)
                reduct_btn = QtWidgets.QPushButton("Просмотреть")
                reduct_btn.setStyleSheet("background-color: #A7FC00;")
                reduct_btn.setFixedSize(83, 15)
                del_button = QtWidgets.QPushButton("Удалить")
                del_button.setStyleSheet("background-color: rgb(248,23,62);")
                del_button.setFixedSize(60, 15)
                layout.addWidget(reduct_btn)
                layout.addWidget(del_button)
                widget.setLayout(layout)
                item.setData(QtCore.Qt.ItemDataRole.UserRole, id)
                self.calendar_listwidget.setItemWidget(item, widget)                
                reduct_btn.clicked.connect(lambda _, it=item:  self.view_calendar_data_date(it.data(QtCore.Qt.ItemDataRole.UserRole)))
                del_button.clicked.connect(lambda _, it=item:  self.del_calendar_history(it))

    def del_all_calendar_history(self):
        """Calendar Method"""
        self.calendar_listwidget.clear()
        with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                color = QtGui.QColor("#FFFFFF")
                text_format = QtGui.QTextCharFormat()
                text_format.setBackground(color)
                cursor.execute("SELECT date FROM calendar")
                rows = cursor.fetchall()
                for row in rows:
                    date = QDate.fromString(*row, "dd-MM-yyyy")
                    self.calendarWidget.setDateTextFormat(date, text_format)
                cursor.execute("DELETE FROM calendar")
                conn.commit()

    def add_date_to_calendar_history(self, date):
        """Calendar Method"""
        item = QListWidgetItem()
        self.calendar_listwidget.addItem(item)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 2, 1)
        label = QtWidgets.QLabel(date)
        layout.addWidget(label)
        reduct_btn = QtWidgets.QPushButton("Просмотреть")
        reduct_btn.setStyleSheet("background-color: #A7FC00;")
        reduct_btn.setFixedSize(83, 15)
        del_button = QtWidgets.QPushButton("Удалить")
        del_button.setStyleSheet("background-color: rgb(248,23,62);")
        del_button.setFixedSize(60, 15)
        layout.addWidget(reduct_btn)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self.calendar_listwidget.setItemWidget(item, widget)
        row = self.calendar_listwidget.row(item)
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT date FROM calendar WHERE date = ?", (date,))
            rows = cursor.fetchall()
        if rows and rows[0][0] == date:
            self.calendar_listwidget.takeItem(row)
        note_id = self.add_date_note_to_db(label.text())
        item.setData(QtCore.Qt.ItemDataRole.UserRole, note_id)
        reduct_btn.clicked.connect(lambda _, id=note_id: self.view_calendar_data_date(id))
        del_button.clicked.connect(lambda: self.del_calendar_history(item))

    def add_date_note_to_db(self, date):
        """Calendar Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            if self.note_combo.currentText() != "None":
                cursor.execute("SELECT text FROM notes WHERE title = ?", (self.note_combo.currentText(),))
                text = cursor.fetchone()[0]
            else: text = "None"    
            cursor.execute("SELECT date FROM calendar WHERE date = ?", (date,))
            rows = cursor.fetchall()
            if rows and rows[0][0] == date:
                cursor.execute("UPDATE calendar SET stopwatch_note = ?, note_title = ?, note_text = ?, date_color = ? WHERE date = ?", (self.time_combo.currentText(), self.note_combo.currentText(), text, self.my_color.text(), date))
            else:
                cursor.execute("INSERT INTO calendar (date, stopwatch_note, note_title, note_text, date_color) VALUES (?, ?, ?, ?, ?)", (date, self.time_combo.currentText(), self.note_combo.currentText(), text, self.my_color.text()))
            conn.commit()
            return cursor.lastrowid

    def del_calendar_history(self, item):
        """Calendar Method"""
        if item is not None:
            note_id = item.data(QtCore.Qt.ItemDataRole.UserRole)
            row = self.calendar_listwidget.row(item)
            self.calendar_listwidget.takeItem(row)
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT date FROM calendar WHERE id = ?", (note_id,))
                row = cursor.fetchone()[0]
                color = QtGui.QColor("#FFFFFF")
                text_format = QtGui.QTextCharFormat()
                text_format.setBackground(color)
                date = QDate.fromString(row, "dd-MM-yyyy")
                self.calendarWidget.setDateTextFormat(date, text_format)
                cursor.execute("DELETE FROM calendar WHERE id = ?", (note_id,))
                conn.commit()

    def view_calendar_data_date(self, id):
        """Calendar Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT date, stopwatch_note, note_title, note_text FROM calendar WHERE id = ?", (id,))
            rows = cursor.fetchall()
        date, stopwatch_note, note_title, note_text = rows[0]
        self.dialog_window_datas = QtWidgets.QDialog()
        self.dialog_window_datas.setWindowTitle(date)
        self.dialog_window_datas.setFixedSize(400, 300)
        time_label = QtWidgets.QLineEdit(stopwatch_note, parent=self.dialog_window_datas)
        time_label.setGeometry(QtCore.QRect(10, 6, 190, 25))
        time_label.setReadOnly(True)
        note_title_label = QtWidgets.QLineEdit(note_title, parent=self.dialog_window_datas)
        note_title_label.setGeometry(QtCore.QRect(210, 6, 180, 25))
        note_title_label.setReadOnly(True)
        note_label = QtWidgets.QTextEdit(note_text,  parent=self.dialog_window_datas)
        note_label.setGeometry(QtCore.QRect(10, 38, 380, 198))
        note_label.setReadOnly(True)
        btn_close = QtWidgets.QPushButton("Закрыть", parent=self.dialog_window_datas)
        btn_close.setGeometry(QtCore.QRect(10, 245, 80, 45))
        btn_close.clicked.connect(lambda _: self.dialog_window_datas.close())
        self.dialog_window_datas.show()

    def calendar_dialog(self):
        """Calendar Method"""
        self.dialog_window_choose_datas = QtWidgets.QDialog()
        self.dialog_window_choose_datas.setWindowTitle("Выберите записи")
        self.dialog_window_choose_datas.setFixedSize(400, 300)
        time_label = QtWidgets.QLabel("Выберите время:", parent=self.dialog_window_choose_datas)
        time_label.setGeometry(QtCore.QRect(10, 6, 280, 40))
        self.time_combo = QtWidgets.QComboBox(parent=self.dialog_window_choose_datas)
        self.time_combo.setGeometry(QtCore.QRect(110, 13, 280, 30))
        note_label = QtWidgets.QLabel("Выберите заметку:", parent=self.dialog_window_choose_datas)
        note_label.setGeometry(QtCore.QRect(10, 56, 280, 40))
        self.note_combo = QtWidgets.QComboBox(parent=self.dialog_window_choose_datas)
        self.note_combo.setGeometry(QtCore.QRect(120, 63, 270, 30))

        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT note FROM stopwatch_history")
            stopwatch_times = cursor.fetchall()
            cursor.execute("SELECT title FROM notes")
            notes_title = cursor.fetchall()
        self.time_combo.addItems(["None"])
        self.note_combo.addItems(["None"])
        try:
            for i in stopwatch_times:
                self.time_combo.addItems([i[0]])
            for i in notes_title:
                self.note_combo.addItems([i][0])
        except:  pass
        note_label = QtWidgets.QPushButton("Выберите цвет даты:", parent=self.dialog_window_choose_datas)
        note_label.setGeometry(QtCore.QRect(10, 106, 220, 40))
        note_label.clicked.connect(self.color_dialog)
        my_color_info = QtWidgets.QLabel("Цвет даты:", parent=self.dialog_window_choose_datas)
        my_color_info.setGeometry(QtCore.QRect(240, 109, 60, 30))
        self.my_color = QtWidgets.QLabel(f"#ffffff", parent=self.dialog_window_choose_datas)
        self.my_color.setGeometry(QtCore.QRect(305, 109, 60, 30))
        self.btn_apply = QtWidgets.QPushButton("Принять",parent=self.dialog_window_choose_datas)
        self.btn_apply.setGeometry(QtCore.QRect(10, 180, 130, 80))
        self.btn_apply.clicked.connect(self.set_date)
        self.dialog_window_choose_datas.show()

    def color_dialog(self):
        """Calendar Method"""
        color = QtWidgets.QColorDialog.getColor()
        self.my_color.setText(color.name())

    def set_date(self):
        """Calendar Method"""
        selected_date = self.calendarWidget.selectedDate()
        date_str = selected_date.toString("dd-MM-yyyy")
        current_formats = self.calendarWidget.dateTextFormat()
        color = QtGui.QColor(self.my_color.text())
        text_format = QtGui.QTextCharFormat()
        text_format.setBackground(color)
        current_formats[selected_date] = text_format
        self.calendarWidget.setDateTextFormat(selected_date, text_format)
        self.add_date_to_calendar_history(date=date_str)
        self.dialog_window_choose_datas.close()

    def save_backup(self):
        """Settings Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            backup = ""
            for sql in conn.iterdump():
                backup += sql
        try:
            file_path = QtWidgets.QFileDialog.getSaveFileName(self.settings_page, "Save file", "", "TXT files (*.txt)")[0]
            with open(file_path, "w", encoding="UTF-8") as file:
                file.write(backup)
        except: pass

    def load_backup(self):
        """Settings Method"""
        file_path = QtWidgets.QFileDialog.getOpenFileName(self.settings_page, "Load file", "", "TXT files (*.txt)")[0]
        if file_path != "":
            self.del_all_data()
            with open(file_path, encoding="UTF-8") as file:
                script = file.read()
            with open(self.path_to_db, "w", encoding="UTF-8") as file:
                file.write("")
            with sqlite3.connect(self.path_to_db) as conn:
                cursor = conn.cursor()
                cursor.executescript(script)
                conn.commit()
            self.load_user_settings()
            self.load_stopwatch_notes()
            self.load_notes_history()
            self.load_calendar_history()            
        else: return

    def create_tables(self):
        """Database Method"""
        with sqlite3.connect(self.path_to_db) as conn:
            cursor = conn.cursor()
            cursor.executescript("""CREATE TABLE IF NOT EXISTS stopwatch_history
                            (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            note TEXT NOT NULL,
                            time_note TEXT NOT NULL
                            );
                            CREATE TABLE IF NOT EXISTS user_settings
                            (
                            objectName TEXT NOT NULL UNIQUE,
                            objectValue BOOL NOT NULL
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
                            );""")

    def check_database_integrity(self):
        """Database Method"""
        if not os.path.exists(self.path_to_db):
            return False
        try:
            with sqlite3.connect(self.path_to_db) as conn:
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

    def del_all_data(self):
        """Settings Method"""
        self.del_all_calendar_history()
        self.del_all_stopwatch_history()
        self.del_all_notes_history()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
