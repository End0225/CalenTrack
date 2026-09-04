from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QPainter, QColor
from utils.button_factory import ButtonFactory


class StopwatchView(QtWidgets.QWidget):
    start_clicked = QtCore.pyqtSignal()
    reset_clicked = QtCore.pyqtSignal()
    save_clicked = QtCore.pyqtSignal()
    open_combobox_clicked = QtCore.pyqtSignal()

    def __init__(self, icon_manager):
        super().__init__()
        self.icon_manager = icon_manager
        self.factory = ButtonFactory(self.icon_manager)
        self._is_combobox_active = False
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
        self._spacerItem1 = QtWidgets.QSpacerItem(356, 27, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self._gridLayout_3.addItem(self._spacerItem1, 0, 1, 2, 1)
        self._comboBox_label = QtWidgets.QLabel(parent=self)
        self._comboBox_label.mousePressEvent = lambda event: self.open_combobox_clicked.emit()
        self._comboBox_label.setMinimumSize(QtCore.QSize(75, 25))
        self._comboBox_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self._comboBox_label.setStyleSheet("""QLabel {
    background-color: #252525;
    border: 1px solid #3e3e42;
    border-radius: 6px;
    color: #d4d4d4;
    font-size: 12px;
    padding-left: 16px;
    font-weight: 700;
}""")
        self._comboBox_label.setText("Empty")
        self._gridLayout_3.addWidget(self._comboBox_label, 0, 2, 1, 1)
        self._comboBox_listwidget = QtWidgets.QListWidget(parent=self)
        self._comboBox_listwidget.setStyleSheet("""QListWidget {
    background-color: #252525;
    border: 1px solid #3e3e42;
    padding: 4px 8px;
    border-radius: 15%;
}""")
        self._comboBox_listwidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.add_btn_create_tag()
        self._comboBox_listwidget.hide()
        self.add_tag("Empy", "#A2A2A2", 1)  # TODO: when model will work with tags then make 'Empy' tag from model and then show it
        self._gridLayout_17.addLayout(self._gridLayout_3, 0, 0, 1, 4)
        self._gridLayout_5 = QtWidgets.QGridLayout()
        self._spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self._gridLayout_5.addItem(self._spacerItem2, 0, 0, 1, 3)
        self._spacerItem3 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self._gridLayout_5.addItem(self._spacerItem3, 1, 2, 2, 1)
        self._spacerItem4 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self._gridLayout_5.addItem(self._spacerItem4, 1, 0, 2, 1)
        self._spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self._gridLayout_5.addItem(self._spacerItem5, 3, 0, 1, 3)
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

    def get_spacerItem5_height(self) -> int:
        return self._spacerItem5.geometry().height()

    def get_spacerItem1_width(self) -> int:
        return self._spacerItem1.geometry().width()

    def get_page_width(self) -> int:
        return self.geometry().width()

    def get_comboBox_label_width(self) -> int:
        return self._comboBox_label.geometry().width()

    def display_listwidget(self, x: int, y: int, width: int, height: int) -> None:
        if self._is_combobox_active:
            self._comboBox_listwidget.hide()
            self._is_combobox_active = False
        else:
            self._comboBox_listwidget.setFixedSize(width, height)
            self._comboBox_listwidget.move(x, y)
            self._comboBox_listwidget.show()
            self._is_combobox_active = True

    def _create_circle_icon(self, color_hex: str) -> QtGui.QPixmap:
        ratio = self.devicePixelRatioF()
        scaled_size = int(15 * ratio)
        pixmap = QtGui.QPixmap(scaled_size, scaled_size)
        pixmap.fill(QtCore.Qt.GlobalColor.transparent)
        pixmap.setDevicePixelRatio(ratio)
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setBrush(QtGui.QColor(color_hex))
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, 14, 14)
        painter.end()
        return pixmap

    def add_tag(self, tag: str, color_hex: str, tag_id: int) -> None:
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(0, 28))
        self._comboBox_listwidget.addItem(item)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(2, 1, 1, 1)
        widget.setStyleSheet("""QWidget {
    border: none;
    background-color:#252525;
    padding: 0;
}
QWidget:hover {
    background-color: #2d2d2d;
}""")
        icon_label = QtWidgets.QLabel()
        icon_label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
        icon_label.setFixedSize(15, 15)
        icon_label.setPixmap(self._create_circle_icon(color_hex))
        layout.addWidget(icon_label)
        label = QtWidgets.QLabel(tag)
        label.setStyleSheet("padding: 0; color: #D4D4D4; font-weight: 700; font-size: 12px; border-top: none; background-color: none;")
        layout.addWidget(label)
        edit_button = QtWidgets.QPushButton()
        edit_button.setIcon(self.icon_manager.get_icon("edit-tag-icon.png"))
        edit_button.enterEvent = lambda event: edit_button.setIcon(self.icon_manager.get_icon("edit-tag-hover-icon.png"))
        edit_button.leaveEvent = lambda event: edit_button.setIcon(self.icon_manager.get_icon("edit-tag-icon.png"))
        edit_button.setStyleSheet("""QPushButton {
    padding: 0;
    border-top: none;
    background-color: transparent;
    border-radius: 4%;
    color: white;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}""")
        edit_button.setFixedSize(18, 18)
        layout.addWidget(edit_button)
        del_button = QtWidgets.QPushButton()
        del_button.setIcon(self.icon_manager.get_icon("delete-tag-icon.png"))
        del_button.enterEvent = lambda event: del_button.setIcon(self.icon_manager.get_icon("delete-tag-hover-icon.png"))
        del_button.leaveEvent = lambda event: del_button.setIcon(self.icon_manager.get_icon("delete-tag-icon.png"))
        del_button.setStyleSheet("""QPushButton {
    padding: 0;
    border-top: none;
    background-color: transparent;
    border-radius: 4%;
    color: white;
    font-weight: 700;
    font-size: 12px;
}
QPushButton:focus {
    border: none;
    outline: none;
}""")
        del_button.setFixedSize(18, 18)
        layout.addWidget(del_button)
        widget.setLayout(layout)
        self._comboBox_listwidget.setItemWidget(item, widget)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, tag_id)
        self.keep_btn_at_bottom()  # TODO

    def add_btn_create_tag(self) -> None:
        item: QtWidgets.QListWidgetItem = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(0, 28))
        self._comboBox_listwidget.addItem(item)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setStyleSheet("""QWidget {
    border: none;
    background-color: #252525;
    padding: 0;
}
QWidget:hover {
    background-color: #2d2d2d;
}""")
        create_button = QtWidgets.QToolButton()
        create_button.setText("\u00A0New tag")
        create_button.setFixedSize(QtCore.QSize(16777215, 27))
        create_button.setStyleSheet("""QToolButton {
    background-color: transparent;
    color: #48b585;
    font-size: 12px;
    font-weight: 700;
}
QToolButton:focus {
    border: none;
    outline: none;
}""")
        create_button.setIcon(self.icon_manager.get_icon("add-tag-icon.png"))
        create_button.setIconSize(QtCore.QSize(14, 14))
        create_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        layout.addWidget(create_button)
        layout.addStretch(1)
        widget.setLayout(layout)
        self._comboBox_listwidget.setItemWidget(item, widget)
        item.setData(QtCore.Qt.ItemDataRole.UserRole, -1)  # TODO: mb change value
        self.keep_btn_at_bottom()  # TODO

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        global_click_pos = event.globalPosition().toPoint()
        local_pos = self._comboBox_listwidget.mapFromGlobal(global_click_pos)
        if not self._comboBox_listwidget.rect().contains(local_pos):
            self._is_combobox_active = True
            self.open_combobox_clicked.emit()
        super().mousePressEvent(event)

    def keep_btn_at_bottom(self) -> None:
        ...

    def resizeEvent(self, event: QtGui.QResizeEvent):
        if event:
            self._is_combobox_active = True
            self.open_combobox_clicked.emit()
        return super().resizeEvent(event)