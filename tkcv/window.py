import tkinter as tk
from .utils import cv2Tk

class Window(tk.Frame):
    _active_windows = {}
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        Window._active_windows[name] = self
        self.impanel = tk.Label()
        self.impanel.pack()

        if isinstance(self.master, tk.Tk):
            self.master.title(name)
            self.master.protocol("WM_DELETE_WINDOW", self.close)

    def set_img(self, image):
        img = cv2Tk(image)
        self.active = img
        self.impanel.configure(image=img)

    def close(self):
        self.master.quit()
        if isinstance(self.master, tk.Tk):
            self.master.withdraw()

    def mainloop(self, *args, **kwargs):
        if isinstance(self.master, tk.Tk):
            self.master.deiconify()
        super().mainloop(*args, **kwargs)
    