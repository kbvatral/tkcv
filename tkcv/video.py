import cv2
import tkinter.ttk
import tkinter as tk
from .window import Window

def count_frames(video):
    release = False
    if not isinstance(video, cv2.VideoCapture):
        video = cv2.VideoCapture(video)
        release = True
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    try:
        total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    except:
        total = 0
        while True:
            (grabbed, frame) = video.read()
            if not grabbed:
                break
            total += 1

    if release:
        video.release()
    else:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    return total


class VideoPlayer(tk.Frame):
    def __init__(self, stream, override_fps=None, **kwargs):
        super().__init__(**kwargs)
        self.vs = stream
        if override_fps is None:
            self.fps = max(1, self.vs.get(cv2.CAP_PROP_FPS))
        else:
            self.fps = override_fps
        self.frame_time = int(1000 // self.fps)
        self.frame_total = count_frames(self.vs)
        self.frame_counter = 0

        self.main_window = Window("")
        self.main_window.pack()
        self.progress_bar = tk.ttk.Progressbar(mode='determinate', length=int(0.95*self.vs.get(cv2.CAP_PROP_FRAME_WIDTH)))
        self.progress_bar.pack(pady=10)
        self.progress_bar.bind("<Button-1>", self._seekProgressbarCallback)
        self.ctrl_bar = tk.Frame()
        self.ctrl_bar.pack(pady=10)
        
        self.btn_prev = tk.Button(text="<<", master=self.ctrl_bar, command=lambda: self._seekFrame(self.frame_counter-1))
        self.btn_prev.grid(row=1, column=1, padx=5)
        self.btn_play = tk.Button(text="Play/Pause", master=self.ctrl_bar, command=self._playPauseCallback)
        self.btn_play.grid(row=1, column=2, padx=5)
        self.btn_next = tk.Button(text=">>", master=self.ctrl_bar, command=lambda: self._nextFrame(no_after=True))
        self.btn_next.grid(row=1, column=3, padx=5)

        self.playing = False
        self.after(0, self._nextFrame)

    def get_frame(self):
        ret, frame = self.vs.read()
        return frame

    def _playPauseCallback(self):
        self.playing = not self.playing
        if self.playing:
            self._nextFrame()

    def _nextFrame(self, no_after=False):
        self.frame_counter += 1
        if self.frame_counter <= self.frame_total:
            self.progress_bar['value'] = 100*self.frame_counter/self.frame_total
            frame = self.get_frame()
            self.main_window.set_img(frame)
        else:
            self.frame_counter = self.frame_total
            self.playing = False
        if self.playing and not no_after:
            self.after(self.frame_time, self._nextFrame)

    def _seekFrame(self, frame_num):
        self.frame_counter = frame_num-1
        self.vs.set(cv2.CAP_PROP_POS_FRAMES, self.frame_counter)
        self._nextFrame(no_after=True)

    def _seekProgressbarCallback(self, event):
        width = event.widget.winfo_width()
        percent = event.x / width
        frame_num = int(percent * self.frame_total)
        self._seekFrame(frame_num)