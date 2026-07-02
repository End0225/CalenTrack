from PyQt6 import QtCore, QtWidgets


class ColorDialog(QtWidgets.QColorDialog):
    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self._setup_ui()

    def _setup_ui(self) -> None:
        self.setOption(QtWidgets.QColorDialog.ColorDialogOption.DontUseNativeDialog)
        self.setWindowIcon(self.icon_manager.get_icon("app-logo.ico"))
        self.setWindowTitle("CalenTrack | Choose color")

    def get_color(self) -> str | None:
        if self.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            return self.currentColor().name() # TODO: maybe throw a signal to calendar_presenter instead of returning data to calendar_dialog?
        return None