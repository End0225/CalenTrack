from PyQt6 import QtWidgets, QtCore


class ButtonFactory:
    def __init__(self, icon_manager):
        self._icon_manager = icon_manager
        self._base_btn_style = """QPushButton {
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
QPushButton:focus {
    border: none;
    outline: none;
}"""
        self.base_tool_btn_style = """QToolButton {
    color: #9E9EA7;
    border: none;
    font-size: 12px;
    font-weight: 700;
}
QToolButton:hover {
    background-color: #252525;
}
"""
        self.checked_tool_btn_style = """QToolButton {
    background-color: #323234;
    color: white;
}"""

    def get_btn(self, parent: QtWidgets.QWidget | QtWidgets.QFrame, btn_color: str, btn_text: str, btn_size: list[int], hsp: QtWidgets.QSizePolicy.Policy | None, vsp: QtWidgets.QSizePolicy.Policy | None, icon_file_name: str | None, icon_size: list[int] | None) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton(parent=parent)
        button.setText(btn_text)
        if hsp and vsp:
            sizePolicy = QtWidgets.QSizePolicy(hsp, vsp)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
        else:
            button.setMaximumSize(QtCore.QSize(16777215, btn_size[1]))
        button.setMinimumSize(QtCore.QSize(*btn_size))
        match btn_color:
            case "gray":
                style = self._get_gray_btn_style()
            case "green":
                style = self._get_green_btn_style()
            case "red":
                style = self._get_red_btn_style()
            case "violet":
                style = self._get_violet_btn_style()
            case _:
                raise ValueError("Don`t correct button color!")
        button.setStyleSheet(style)
        if icon_file_name:
            button.setIcon(self._icon_manager.get_icon(icon_file_name))
            if icon_size:
                button.setIconSize(QtCore.QSize(*icon_size))
        return button

    def _get_gray_btn_style(self) -> str:
        return f"""{self._base_btn_style}
QPushButton {{
    background-color: #52525a;
    border: 1px solid #3e3e42;
    border-radius: 6%;
}}
QPushButton:hover {{
    background-color: #3e3e42;
    border: 1px solid #52525a;
}}"""

    def _get_green_btn_style(self) -> str:
        return f"""{self._base_btn_style}
QPushButton {{
    background-color: #48b585;
    border-radius: 6%;
}}
QPushButton:hover {{
    background-color: #38936c;
}}"""

    def _get_red_btn_style(self) -> str:
        return f"""{self._base_btn_style}
QPushButton {{
    background-color: #d13c30;
    border-radius: 8%;
}}
QPushButton:hover {{
    background-color: #af3025;
}}"""

    def _get_violet_btn_style(self) -> str:
        return f"""{self._base_btn_style}
QPushButton {{
    background-color: #8365ee;
    border-radius: 6%;
}}
QPushButton:hover {{
    background-color: #7349e5;
}}"""

    def get_aside_tool_btn(self, parent: QtWidgets.QWidget | QtWidgets.QFrame, btn_text: str, icon_file_name: str | None, icon_size: list[int] | None) -> QtWidgets.QToolButton:
        button = QtWidgets.QToolButton(parent=parent)
        button.setText(btn_text)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy)
        button.setMinimumSize(QtCore.QSize(93, 14))
        button.setStyleSheet(self.base_tool_btn_style)
        if icon_file_name:
            button.setIcon(self._icon_manager.get_icon(icon_file_name))
            button.setIconSize(QtCore.QSize(*icon_size))
            button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        return button