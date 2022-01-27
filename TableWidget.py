from PyQt5.QtWidgets import QTableWidget
from TableWidgetStyle import *


class PyTableWidget(QTableWidget):
    def __init__(
            self,
            radius=8,
            color="#8a95aa",
            bg_color="#1e2229",
            selection_color="#111",
            header_horizontal_color="#1b1e23",
            header_vertical_color="#21252d",
            bottom_line_color="2c313c",
            grid_line_color="#2c313c",
            scroll_bar_bg_color="#2c313c",
            scroll_bar_btn_color="#272c36",
            context_color="#568af2"
    ):
        super().__init__()

        # PARAMETERS

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
            self,
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius=radius,
            _color=color,
            _bg_color=bg_color,
            _header_horizontal_color=header_horizontal_color,
            _header_vertical_color=header_vertical_color,
            _selection_color=selection_color,
            _bottom_line_color=bottom_line_color,
            _grid_line_color=grid_line_color,
            _scroll_bar_bg_color=scroll_bar_bg_color,
            _scroll_bar_btn_color=scroll_bar_btn_color,
            _context_color=context_color
        )
        self.setStyleSheet(style_format)



