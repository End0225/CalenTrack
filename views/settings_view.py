from PyQt6 import QtCore, QtWidgets
from utils.button_factory import ButtonFactory


class SettingsView(QtWidgets.QWidget):
    save_backup_clicked = QtCore.pyqtSignal()
    load_backup_clicked = QtCore.pyqtSignal()
    deleteall_clicked = QtCore.pyqtSignal()
    checkbox_clicked = QtCore.pyqtSignal(str, bool)

    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory = ButtonFactory(self.icon_manager)
        self.setup_ui()
        
    def setup_ui(self) -> None:
        self.setObjectName("settings_page")
        self.gridLayout_18 = QtWidgets.QGridLayout(self)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.settings_grid = QtWidgets.QGridLayout()
        self.settings_grid.setContentsMargins(12, 10, 12, 60)
        self.settings_grid.setObjectName("settings_grid")
        self.settings_title_label = QtWidgets.QLabel(parent=self)
        self.settings_title_label.setText("Settings")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_title_label.sizePolicy().hasHeightForWidth())
        self.settings_title_label.setSizePolicy(sizePolicy)
        self.settings_title_label.setMinimumSize(QtCore.QSize(0, 20))
        self.settings_title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.settings_title_label.setStyleSheet("""color: white;
font-size: 18px;
font-weight: 700;""")
        self.settings_title_label.setObjectName("settings_title_label")
        self.settings_grid.addWidget(self.settings_title_label, 0, 0, 1, 1)
        self.settings_frame = QtWidgets.QFrame(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_frame.sizePolicy().hasHeightForWidth())
        self.settings_frame.setSizePolicy(sizePolicy)
        self.settings_frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
}""")
        self.settings_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settings_frame)
        self.verticalLayout.setContentsMargins(12, 0, 12, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backup_frame = QtWidgets.QFrame(parent=self.settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_frame.sizePolicy().hasHeightForWidth())
        self.backup_frame.setSizePolicy(sizePolicy)
        self.backup_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.backup_frame.setStyleSheet("border: none;")
        self.backup_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.backup_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.backup_frame.setObjectName("backup_frame")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.backup_frame)
        self.gridLayout_22.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_22.setHorizontalSpacing(0)
        self.gridLayout_22.setVerticalSpacing(10)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.loadbackup_btn = self.factory.get_btn(self.backup_frame, "gray", "Load backup", [0, 20], None, None, "export-icons.png", [14, 14])
        self.loadbackup_btn.clicked.connect(self.load_backup_clicked.emit)
        self.gridLayout_22.addWidget(self.loadbackup_btn, 3, 0, 1, 1)
        self.savebackup_btn = self.factory.get_btn(self.backup_frame, "green", "Save backup", [0, 20], None, None, "import-icon.png", [15, 15])
        self.savebackup_btn.clicked.connect(self.save_backup_clicked.emit)
        self.gridLayout_22.addWidget(self.savebackup_btn, 2, 0, 1, 1)
        self.backup_title_label = QtWidgets.QLabel(parent=self.backup_frame)
        self.backup_title_label.setText("Backup")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_title_label.sizePolicy().hasHeightForWidth())
        self.backup_title_label.setSizePolicy(sizePolicy)
        self.backup_title_label.setMinimumSize(QtCore.QSize(0, 27))
        self.backup_title_label.setStyleSheet("""color: white;
font-size: 15px;
font-weight: 700;
border: none;
margin-bottom: 10%;
""")
        self.backup_title_label.setObjectName("backup_title_label")
        self.gridLayout_22.addWidget(self.backup_title_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.backup_frame)
        self.parameters_frame = QtWidgets.QFrame(parent=self.settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_frame.sizePolicy().hasHeightForWidth())
        self.parameters_frame.setSizePolicy(sizePolicy)
        self.parameters_frame.setMinimumSize(QtCore.QSize(0, 120))
        self.parameters_frame.setStyleSheet("""border: none;
border-radius: 0;
border-top: 1px solid #3e3e42;
""")
        self.parameters_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.parameters_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.parameters_frame.setObjectName("parameters_frame")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.parameters_frame)
        self.gridLayout_23.setContentsMargins(0, -1, 0, 8)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.parameter_1_chechbox = QtWidgets.QCheckBox(parent=self.parameters_frame)
        self.parameter_1_chechbox.clicked.connect(lambda: self.checkbox_clicked.emit(self.parameter_1_chechbox.objectName(), self.parameter_1_chechbox.isChecked()))
        self.parameter_1_chechbox.setText("Open stopwatch when you establish time from history")
        self.parameter_1_chechbox.setStyleSheet("""QCheckBox {
    border: none;
    background-color: none;
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
QCheckBox::indicator {
    width: 12px;
    height: 12px;
    border: 1px solid #858585;
    border-radius: 4%;
    background: #3b3b3b;
}
QCheckBox::indicator:checked {
    background-color: #48b585;
}
QCheckBox::indicator:hover {
    border-color: #acacac;
}""")
        self.parameter_1_chechbox.setObjectName("parameter_1_chechbox")
        self.gridLayout_23.addWidget(self.parameter_1_chechbox, 2, 0, 1, 1)
        self.parameters_title_label = QtWidgets.QLabel(parent=self.parameters_frame)
        self.parameters_title_label.setText("Parameters")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters_title_label.sizePolicy().hasHeightForWidth())
        self.parameters_title_label.setSizePolicy(sizePolicy)
        self.parameters_title_label.setMinimumSize(QtCore.QSize(0, 30))
        self.parameters_title_label.setStyleSheet("""border: none;
color: white;
font-size: 15px;
font-weight: 700;""")
        self.parameters_title_label.setObjectName("parameters_title_label")
        self.gridLayout_23.addWidget(self.parameters_title_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.parameters_frame)
        self.dangerzone_frame = QtWidgets.QFrame(parent=self.settings_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dangerzone_frame.sizePolicy().hasHeightForWidth())
        self.dangerzone_frame.setSizePolicy(sizePolicy)
        self.dangerzone_frame.setStyleSheet("""border: none;
border-radius: 0;
border-top: 1px solid #3e3e42;""")
        self.dangerzone_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dangerzone_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dangerzone_frame.setObjectName("dangerzone_frame")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.dangerzone_frame)
        self.gridLayout_24.setContentsMargins(0, -1, 0, 12)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.dangerzone_title_label = QtWidgets.QLabel(parent=self.dangerzone_frame)
        self.dangerzone_title_label.setText("Danger zone")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dangerzone_title_label.sizePolicy().hasHeightForWidth())
        self.dangerzone_title_label.setSizePolicy(sizePolicy)
        self.dangerzone_title_label.setMinimumSize(QtCore.QSize(0, 30))
        self.dangerzone_title_label.setStyleSheet("""border: none;
font-size: 15px;
font-weight: 700;
color: #DC2626;""")
        self.dangerzone_title_label.setObjectName("dangerzone_title_label")
        self.gridLayout_24.addWidget(self.dangerzone_title_label, 0, 0, 1, 1)
        self.dangerzone_deleteall_btn = self.factory.get_btn(self.dangerzone_frame, "red", "Delete all data", [0, 20], QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed, "delete-icon.png", [14, 14])
        self.dangerzone_deleteall_btn.clicked.connect(self.deleteall_clicked.emit)
        self.gridLayout_24.addWidget(self.dangerzone_deleteall_btn, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.dangerzone_frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.settings_grid.addWidget(self.settings_frame, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.settings_grid.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_18.addLayout(self.settings_grid, 0, 0, 1, 1)

    def reset_settings(self) -> None:
        for checkbox in self.findChildren(QtWidgets.QCheckBox):
            checkbox.setChecked(False)