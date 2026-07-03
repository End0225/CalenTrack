from PyQt6 import QtCore, QtWidgets


class SettingsPresenter:
    def __init__(self, view: QtWidgets.QWidget, app, model):
        self.view = view
        self.app = app
        self.model = model
        self.view.save_backup_clicked.connect(self._save_backup)
        self.view.load_backup_clicked.connect(self._load_backup)
        self.view.deleteall_clicked.connect(self._deleteall_data)
        self.view.parameter_1_clicked.connect(self._toggle_setting)

    def load_settings(self) -> None:
        settings: list[tuple[str, bool]] = self.model.get_settings()
        for name, value in settings:
            chechbox: QtWidgets.QCheckBox = self.app.view.findChild(QtWidgets.QCheckBox, name)
            chechbox.setChecked(False if value == 0 else True)

    def _save_backup(self) -> None:
        backup: str = self.model.get_backup()
        try:
            file_path = QtWidgets.QFileDialog.getSaveFileName(self.view, "Save file", "", "TXT files (*.txt)")[0]
            with open(file_path, "w", encoding="UTF-8") as file:
                file.write(backup)
        except:
            pass

    def _load_backup(self) -> None:
        file_path: tuple[str, str] = QtWidgets.QFileDialog.getOpenFileName(self.view, "Load file", "", "TXT files (*.txt)")[0]
        if file_path:
            self.app.del_data()
            self.model.load_data(file_path)
            self.app.preload_data()

    def _deleteall_data(self) -> None:
        self.app.del_data()

    def _toggle_setting(self, name: str, status: bool) -> None:
        self.model.toggle_setting(name, status)