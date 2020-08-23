import cv2
from PIL import Image, ImageTk
from tkinter import Tk, Label

def cv2Tk(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_pil = ImageTk.PhotoImage(Image.fromarray(img))
    return img_pil

def imshow(title, image, time=0):
    window = Tk()
    window.title(title)
    img = cv2Tk(image)
    panel = Label(window, image=img)
    panel.pack()
    if time != 0:
        window.after(time, window.destroy)
    window.mainloop()