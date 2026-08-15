from PyQt6 import QtGui
import os
import sys


class IconManager:
    def __init__(self, icon_path: str):
        self.icon_folder: dict[str, str] = {}
        self.icon_path: str = icon_path
        self._platform = sys.platform
        print(self._platform)

    def get_icon(self, icon_name: str, mode=QtGui.QIcon.Mode.Normal, state=QtGui.QIcon.State.Off) -> QtGui.QIcon | None:
        if icon_name in self.icon_folder:
            icon: QtGui.QIcon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.icon_folder[icon_name]), mode, state)
            return icon

    def get_app_icon(self) -> QtGui.QIcon:
        icon: QtGui.QIcon = QtGui.QIcon()
        match self._platform:
            case "darwin":
                icon.addPixmap(QtGui.QPixmap(self.icon_folder["app-logo.icns"]), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            case "win32":
                icon.addPixmap(QtGui.QPixmap(self.icon_folder["app-logo.ico"]), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        return icon

    def copy_all_resources(self) -> None:
        for file in os.listdir(self.icon_path):
            self.icon_folder[file] = os.path.join(self.icon_path, file)
