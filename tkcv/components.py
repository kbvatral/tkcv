import tkinter as tk
from .utils import cv2Tk

class ImageFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.impanel = tk.Label(master=self)
        self.impanel.pack()

    def set_img(self, image):
        img = cv2Tk(image)
        self.active = img
        self.impanel.configure(image=img)

    def set_LBCallback(self, func):
        self.set_callback("<Button-1>", func)
    def set_RBCallback(self, func):
        self.set_callback("<Button-3>", func)
    def set_MouseMoveCallback(self, func):
        self.set_callback("<Motion>", func)
    def set_callback(self, event, func):
        self.impanel.unbind(event)
        self.impanel.bind(event, func)