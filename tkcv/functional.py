from .utils import try_open_img, get_image_filetypes, get_video_filetypes
from .window import Window
import tkinter.filedialog
import tkinter as tk
import cv2

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

def open_image(title="Open Image", parent=None, include_video=False, path_only=False):
    image_formats = get_image_filetypes(to_string=True)
    video_formats = get_video_filetypes(to_string=True)

    formats = [("Image Files", image_formats)]
    if include_video:
        formats = [("Media Files", image_formats+" "+video_formats)] + formats
        formats.append(("Video Files", video_formats))
    formats.append(("All Files", "*.*"))

    if isinstance(parent, str):
        if parent in Window._active_windows:
            parent = Window._active_windows[parent]
        else:
            parent = None
    path = tk.filedialog.askopenfilename(title=title, filetypes=formats, parent=parent)
    if isinstance(path, str):
        if path_only:
            return path
        else:
            return try_open_img(path, try_video=include_video)
    return None

def open_video(title="Open Video", parent=None, path_only=False):
    video_formats = get_video_filetypes(to_string=True)
    formats = [("Video Files", video_formats), ("All Files", "*.*")]
    
    if isinstance(parent, str):
        if parent in Window._active_windows:
            parent = Window._active_windows[parent]
        else:
            parent = None
    path = tk.filedialog.askopenfilename(title=title, filetypes=formats, parent=parent)
    if isinstance(path, str):
        if path_only:
            return path
        else:
            return cv2.VideoCapture(path)
    return None
