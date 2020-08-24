import cv2
from PIL import Image, ImageTk

image_filetypes = [".jpg", ".jpeg", "jpe", ".jp2", ".png", ".webp", ".pbm", ".pgm", ".ppm",
                   ".pxm", ".pnm", ".pfm", ".sr", ".ras", ".tiff", ".tif", ".exr", ".hdr", ".pic", ".bmp", ".dib"]
video_filetypes = [".avi", ".mp4", ".avchd", ".mkv", ".mov", ".gt", ".flv"]

def get_image_filetypes(to_string=False):
    if to_string:
        image_formats = ""
        for fmt in image_filetypes:
            image_formats += fmt + " "
        return image_formats[:-1]
    else:
        return image_filetypes

def get_video_filetypes(to_string=False):
    if to_string:
        video_formats = ""
        for fmt in video_filetypes:
            video_formats += fmt + " "
        return video_formats[:-1]
    else:
        return video_filetypes

def cv2Tk(image, swapRB=True):
    if len(image.shape) == 3 and swapRB:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        img = image
    img_pil = ImageTk.PhotoImage(Image.fromarray(img))
    return img_pil


def try_open_img(path, try_video=True):
    img = None
    try:
        candidate = cv2.imread(path)
        if candidate is not None and candidate.size != 0:
            img = candidate
    except:
        pass
    # If not image, try opening as video
    if img is None and try_video:
        vs = None
        try:
            vs = cv2.VideoCapture(path)
            _, candidate = vs.read()
            if candidate is not None and candidate.size != 0:
                img = candidate
        except:
            pass
        try:
            vs.close()
        except:
            pass
    return img
