from .window import Window
from tkinter import Tk

def imshow(window, image, time=0):
    if isinstance(window, str):
        if window in Window._active_windows:
            window = Window._active_windows[window]
        else:
            window = Window(window)
    window.set_img(image)

    if time != 0:
        window.after(time, window.close)
    window.mainloop()

def namedWindow(name, *args, **kwargs):
    return Window(name, *args, **kwargs)

def destroyWindow(window):
    if isinstance(window, Window):
        window = window.name
    Window._active_windows[window].destroy()
    Window._active_windows.pop(window)

def destroyAllWindows():
    for _, window in Window._active_windows.items():
        window.destroy()
    Window._active_windows.clear()