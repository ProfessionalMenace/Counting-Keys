import tkinter as tk
import threading
import KeysFunctions as kys
from PIL import Image, ImageTk
from variables import labelCharacter1, labelCharacter, root, keys, frame, img_tk, x
import cProfile


def main():
        root.title("Keys Counter")
        root.configure(bg="#151621")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")


        label1 = tk.Label(root, text = "keys counter ( you can put it even in background!!)")
        label1.pack()
        
        for _ in range(len(keys)):
          offset = _ * 4  
          mcd = len(keys[_]) -1

          while len(keys[_]) % mcd != 0:
            mcd -= 1

          label_width = 125 if len(keys[_]) <= 10 else 75
          for i in range(len(keys[_])):            
            labelCharacter1[_][i] = tk.Label(frame[_], textvariable=labelCharacter[_][i], font=("arial", 9), image=img_tk, compound="center", fg="#151621", bd=1, relief="solid", width = label_width)
            labelCharacter1[_][i].grid(row=i // mcd, column=(i % mcd) + offset)
            frame[_].pack(padx = 3, pady= 10)
 
            
                   
        kys.listenKEYS()
        root.mainloop()

if __name__ == "__main__":
     profiler = cProfile.Profile()
     profiler.enable()
     main()
     profiler.print_stats(sort='time')
