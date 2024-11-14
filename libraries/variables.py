import tkinter as tk
import threading
from PIL import Image, ImageTk, ImageDraw

keys = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0]]

firstpression = True

root = tk.Tk()

threads_list = []
labelLETTER = [tk.StringVar() for _ in range(26)]

labelLETTER1 = [None] * 26

transparent_img = Image.new("RGBA", (40, 15), (255, 255, 129, 50))
img_tk = ImageTk.PhotoImage(transparent_img)