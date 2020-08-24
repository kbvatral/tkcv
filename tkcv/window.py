from tkinter import Frame, Label
from .utils import cv2Tk

class Window(Frame):
    _active_windows = {}
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.master.title(name)
        self.impanel = Label()
        self.impanel.pack()

        Window._active_windows[name] = self
        self.master.protocol("WM_DELETE_WINDOW", self.close)

    def set_img(self, image):
        img = cv2Tk(image)
        self.active = img
        self.impanel.configure(image=img)

    def close(self):
        self.master.quit()
        self.master.withdraw()

    def mainloop(self, *args, **kwargs):
        self.master.deiconify()
        super().mainloop(*args, **kwargs)
    