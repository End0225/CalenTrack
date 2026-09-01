from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QPainter, QColor
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

    def _setup_ui(self) -> None:
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self._gridLayout_17 = QtWidgets.QGridLayout(self)
        self._gridLayout_17.setContentsMargins(0, 0, 0, 65)
        self._gridLayout_17.setSpacing(0)
        self._gridLayout_3 = QtWidgets.QGridLayout()
        self._gridLayout_3.setContentsMargins(-1, 8, 12, -1)
        _spacerItem1 = QtWidgets.QSpacerItem(356, 27, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self._gridLayout_3.addItem(_spacerItem1, 0, 1, 2, 1)
        self._comboBox_label = QtWidgets.QLabel(parent=self)
        self._comboBox_label.setMinimumSize(QtCore.QSize(75, 25))
        self._comboBox_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self._comboBox_label.setStyleSheet("""QLabel {
            background-color: #252525;
            border: 1px solid #3e3e42;
            border-radius: 8px;
            color: #d4d4d4;
            font-size: 12px;
            padding-left: 16px;
            font-weight: 700;
        }""")
        self._comboBox_label.setText("Empty")
        self._gridLayout_3.addWidget(self._comboBox_label, 0, 2, 1, 1)
        self._gridLayout_17.addLayout(self._gridLayout_3, 0, 0, 1, 4)
        self._gridLayout_5 = QtWidgets.QGridLayout()
        _spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self._gridLayout_5.addItem(_spacerItem2, 0, 0, 1, 3)
        _spacerItem3 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self._gridLayout_5.addItem(_spacerItem3, 1, 2, 2, 1)
        _spacerItem4 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self._gridLayout_5.addItem(_spacerItem4, 1, 0, 2, 1)
        _spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self._gridLayout_5.addItem(_spacerItem5, 3, 0, 1, 3)
        self._frame = QtWidgets.QFrame(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._frame.sizePolicy().hasHeightForWidth())
        self._frame.setSizePolicy(sizePolicy)
        self._frame.setMinimumSize(QtCore.QSize(242, 270))
        self._frame.setMaximumSize(QtCore.QSize(400, 380))
        self._frame.setStyleSheet("""QFrame {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 15%;
}""")
        self._frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self._frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self._gridLayout_2 = QtWidgets.QGridLayout(self._frame)
        self._gridLayout_2.setContentsMargins(32, 20, 32, 36)
        self._time_label = QtWidgets.QLabel(parent=self._frame)
        self._time_label.setText("00:00:00, 00")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._time_label.sizePolicy().hasHeightForWidth())
        self._time_label.setSizePolicy(sizePolicy)
        self._time_label.setMinimumSize(QtCore.QSize(242, 117))
        font = QtGui.QFont()
        font.setFamily("Consolas,Courier New,monospace")
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
        self._gridLayout_2.addWidget(self._time_label, 1, 1, 1, 2)
        self._start_btn = self.factory.get_btn(self._frame, "violet", "Start", [0, 32], QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed, "start-icon.png", [15, 15])
        self._start_btn.clicked.connect(self.start_clicked.emit)
        self._gridLayout_2.addWidget(self._start_btn, 2, 1, 1, 1)
        self._save_btn = self.factory.get_btn(self._frame, "green", "Save", [0, 32], QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed, "save-icon.png", [19, 19])
        self._save_btn.clicked.connect(self.save_clicked.emit)
        self._gridLayout_2.addWidget(self._save_btn, 3, 1, 1, 2)
        self._reset_btn = self.factory.get_btn(self._frame, "gray", "Reset", [0, 32], QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed, "reset-icon.png", [12, 12])
        self._reset_btn.clicked.connect(self.reset_clicked.emit)
        self._gridLayout_2.addWidget(self._reset_btn, 2, 2, 1, 1)
        self._gridLayout_5.addWidget(self._frame, 1, 1, 2, 1)
        self._gridLayout_5.setRowStretch(0, 1)
        self._gridLayout_5.setRowStretch(1, 1)
        self._gridLayout_5.setRowStretch(2, 2)
        self._gridLayout_5.setRowStretch(3, 1)
        self._gridLayout_17.addLayout(self._gridLayout_5, 1, 0, 1, 1)

    def update_time(self, text: str) -> None:
        self._time_label.setText(text)

    def set_start_btn_text(self, text: str) -> None:
        self._start_btn.setText(text)

    def change_start_btn_icon(self, icon_name: str) -> None:
        self._start_btn.setIcon(self.icon_manager.get_icon(icon_name))

    def get_time(self) -> str:
        return self._time_label.text()

    def add_tag(self, color_hex: str, text: str) -> None:
        # self._comboBox.addItem(self._create_circle_icon(color_hex), text)
        ...

    def _create_circle_icon(self, color_hex: str) -> QtGui.QIcon:
        pixmap: QPixmap = QPixmap(15, 15)
        pixmap.fill(QtCore.Qt.GlobalColor.transparent)
        painter: QPainter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(color_hex))
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, 14, 14)
        painter.end()
        return QtGui.QIcon(pixmap)