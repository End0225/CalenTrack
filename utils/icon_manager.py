from PyQt6 import QtGui
import os


class IconManager:
    def __init__(self, icon_path):
        self.icon_folder = {}
        self.icon_path = icon_path

    def get_icon(self, icon_name: str, mode=QtGui.QIcon.Mode.Normal, state=QtGui.QIcon.State.Off) -> QtGui.QIcon:
        if icon_name in self.icon_folder:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.icon_folder[icon_name]), mode, state)
            return icon

    def copy_all_resources(self) -> None:
        for file in os.listdir(self.icon_path):
            self.icon_folder[file] = os.path.join(self.icon_path, file)
