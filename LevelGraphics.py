from LevelInfo import LevelInfo
import tkinter


# from PIL import ImageGrab  # В формате изображения
# https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-to-an-image


class LevelGraphics:
    _lvl_info: LevelInfo

    def __init__(self, lvl_info):
        self._lvl_info = lvl_info

    def draw_graphics(self, canvas: tkinter.Canvas, size: tuple[int]):
        def tr(x, y):
            nonlocal modifiers
            return (
                x * modifiers[0] + 5,
                y * modifiers[1] + 5,
            )

        boundaries = self._lvl_info.boundaries
        actual_size = (
            max([x[0] for x in boundaries]),
            max([y[1] for y in boundaries]),
        )
        modifiers = ((size[0] - 10) / actual_size[0], (size[1] - 10) / actual_size[1])

        # 0) Окраска рабочей области
        canvas.create_rectangle(*tr(0, 0), *size, fill="#fb0")
        # 1) Отрисовка границ
        for i in range(len(boundaries)):
            coords = (*tr(*boundaries[i - 1]), *tr(*boundaries[i]))
            canvas.create_line(*coords)
        # 2) Выходы
        
        # 3) Дороги
        # 4) Комнаты
        # 5) Двери
        # 6) Ловушки
        # 7) Враги
        # 8) Свет
        # 9) Лут
        # 10) Статик Окружение
        canvas.pack()
