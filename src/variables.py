import tkinter as tk
import threading
from PIL import Image, ImageTk, ImageDraw

keys = [
    [0] * 26,  # Letters
    [0] * 10,  # Numbers
  #  [0] * 31,  # ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ { | } ~ (common symbols)
  #  [0] * 5,   # Arrows and Backspace
    [0] * 12,  # Functional Keys
    [0] * 3,   # Modifier ( Shift, Alt, **Altgr**, Fn, Ctrl )
    [0] * 5,   # Control Keys (Tab, Capslock, Escape, Return, Spacebar )
]

firstpression = True

root = tk.Tk()
labelCharacter = [[tk.StringVar() for x in _] for _ in keys]
labelCharacter1 = [[[None] * x for x in _] for _ in keys ]
frame = [tk.Frame(root, height=20) for sublist in keys]

x = (20, 255, 129, 50)
img = Image.new("RGBA", (125, 15), x)
img_tk = ImageTk.PhotoImage(img)



functionalkey = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"]
modifierkeys = ["shift", "ctrl", "alt"] 
controlkeys = ["esc", "tab", "capslock", "spacebar", "enter"]

current_time  = [[0.0 for x in _] for _ in keys]
lastpression= [[0.0 for x in _] for _ in keys]
lastrepeat= [[0.0 for x in _] for _ in keys]
flag = [[True for x in _] for _ in keys ]

max_cols = max(len(row) for row in keys)