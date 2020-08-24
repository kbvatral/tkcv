import cv2
from PIL import Image, ImageTk

def cv2Tk(image, swapRB=True):
    if len(image.shape) == 3 and swapRB:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        img = image
    img_pil = ImageTk.PhotoImage(Image.fromarray(img))
    return img_pil