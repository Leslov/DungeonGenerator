from LevelInfo import LevelInfo
from ipycanvas import Canvas
# from Tkinter import Tk # вывод на графический интерфейс
# from PIL import ImageGrab  # В формате изображения
# https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image


class LevelGraphics:
    _lvl_info: LevelInfo

    def __init__(self, lvl_info):
        self._lvl_info = lvl_info

    def print_graphics(self):
        boundaries = self._lvl_info.boundaries
        area_size = (
            max([x[0] for x in boundaries]),
            max([y[1] for y in boundaries]),
        )
        canvas = Canvas(width=area_size[0], height=area_size[1])
        canvas.stroke_lines(boundaries)
        canvas
