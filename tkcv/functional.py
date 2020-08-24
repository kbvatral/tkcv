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
        window.after(time, window.destroy)
    window.mainloop()