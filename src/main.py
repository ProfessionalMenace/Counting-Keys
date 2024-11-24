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
        
        for j in range(len(keys)):
          offset = j * 4  
          mcd = len(keys[j]) -1

          while len(keys[j]) % mcd != 0:
            mcd -= 1

          label_width = 125 if len(keys[j]) <= 10 else 75
          for i in range(len(keys[j])):            
            labelCharacter1[j][i] = tk.Label(frame[j], textvariable=labelCharacter[j][i], font=("arial", 9), image=img_tk, compound="center", fg="#151621", bd=1, relief="solid", width = label_width)
            labelCharacter1[j][i].grid(row=i // mcd, column=(i % mcd) + offset)
            frame[j].pack(padx = 3, pady= 10)
 
            
                   
        kys.listenKEYS()
        root.mainloop()

if __name__ == "__main__":
     profiler = cProfile.Profile()
     profiler.enable()
     main()
     profiler.print_stats(sort='time')
