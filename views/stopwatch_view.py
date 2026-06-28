from PyQt6 import QtCore, QtGui, QtWidgets
from utils.button_factory import ButtonFactory


class StopwatchView(QtWidgets.QWidget):
    start_clicked = QtCore.pyqtSignal()
    reset_clicked = QtCore.pyqtSignal()
    save_clicked = QtCore.pyqtSignal()

    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory = ButtonFactory(self.icon_manager)
        self._setup_ui()

    def _setup_ui(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout_17 = QtWidgets.QGridLayout(self)
        self.gridLayout_17.setContentsMargins(36, 120, 36, 192)
        self._frame = QtWidgets.QFrame(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._frame.sizePolicy().hasHeightForWidth())
        self._frame.setSizePolicy(sizePolicy)
        self._frame.setMaximumSize(QtCore.QSize(400, 380))
        self._frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
}""")
        self._frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self._frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(self._frame)
        self.gridLayout_2.setContentsMargins(32, 20, 32, 36)
        self._time_label = QtWidgets.QLabel(parent=self._frame)
        self._time_label.setText("00:00:00, 00")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._time_label.sizePolicy().hasHeightForWidth())
        self._time_label.setSizePolicy(sizePolicy)
        self._time_label.setMinimumSize(QtCore.QSize(242, 117))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self._time_label.setFont(font)
        self._time_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self._time_label.setStyleSheet("""border: none;
font-family: 'Consolas', 'Courier New', monospace;
font-size: 32px;
font-weight: 700;
color: #D4D4D4;""")
        self._time_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2.addWidget(self._time_label, 0, 0, 1, 2)
        self._start_btn = self.factory.get_btn(self._frame, "violet", "Start", [0, 32], QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed, "start-icon.png", [15, 15])
        self.gridLayout_2.addWidget(self._start_btn, 1, 0, 1, 1)
        self._reset_btn = self.factory.get_btn(self._frame, "gray", "Reset", [0, 32], QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed, "reset-icon.png", [12, 12])
        self.gridLayout_2.addWidget(self._reset_btn, 1, 1, 1, 1)
        self._save_btn = self.factory.get_btn(self._frame, "green", "Save", [0, 32], QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed, "save-icon.png", [19, 19])
        self.gridLayout_2.addWidget(self._save_btn, 2, 0, 1, 2)
        self.gridLayout_17.addWidget(self._frame, 1, 0, 1, 1)
        self._start_btn.clicked.connect(self.start_clicked.emit)
        self._reset_btn.clicked.connect(self.reset_clicked.emit)
        self._save_btn.clicked.connect(self.reset_clicked.emit)

    def update_time(self, text: str):
        self._time_label.setText(text)

    def set_start_btn_text(self, text: str):
        self._start_btn.setText(text)

    def change_start_btn_icon(self, icon_name: str):
        self._start_btn.setIcon(self.icon_manager.get_icon(icon_name))