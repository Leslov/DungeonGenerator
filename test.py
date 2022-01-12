import tkinter

from polygon_generator import to_convex_contour
class LvInfo:
    boundaries: list  # лист поинтов(x, y)


def get_lv_info()->LvInfo:
    scale = 1000  # Он же максимальный размер
    edges_count = 4
    lv_info = LvInfo()
    contour = to_convex_contour(edges_count)
    lv_info.boundaries = [(x * scale, y * scale) for x, y in contour]
    return lv_info


def draw_graphics(lvl_info: LvInfo, canvas: tkinter.Canvas, size: tuple[int]):
    def tr(x, y):
        nonlocal modifiers
        return (
            x * modifiers[0] + 5,
            y * modifiers[1] + 5,
        )
    boundaries = lvl_info.boundaries
    actual_size = (
        max([x[0] for x in boundaries]),
        max([y[1] for y in boundaries]),
    )
    modifiers = ((size[0] - 10) / actual_size[0], (size[1] - 10) / actual_size[1])

    # 0) Окраска рабочей области
    canvas.create_rectangle(*tr(0, 0), *size, fill="#fb0")
    # 1) Границы
    for i in range(len(boundaries)):
        coords = (*tr(*boundaries[i - 1]), *tr(*boundaries[i]))
        canvas.create_line(*coords)
    # 2) Комнаты

    # 3) Выходы

    canvas.pack()


root = tkinter.Tk()
root['bg'] = '#fafafa'
root.title('Название проги')
# root.wm_attributes('-alpha', 0.7) #Прозрачность
root.geometry('1600x900')
w = 1024
h = 768
canvas = tkinter.Canvas(root, width=w, height=h)
canvas.pack()


lv_info = get_lv_info()
draw_graphics(lv_info, canvas, (w, h))
root.mainloop()
