import tkinter as tk
import threading
import KeysFunctions as kys
from PIL import Image, ImageTk
from variables import keys, threads_list, labelLETTER1, labelLETTER, root, img_tk



      
root.title("COUNT THE KEYS")
root.geometry("400x300")
root.configure(bg="#151621")



def listenLETTERS():
    for _ in range(26):
        def counterletter(letterindex=_):
                kys.Bfunc(0, letterindex, f'{chr(letterindex+97)}', labelLETTER, letterindex) # 0 = index(letter_section), letterindex = specific_letter, f'{chr(letterindex+97)}' = letter, LabelLETTER = sentence, letterindex = position_LabelLetter. 
        threadLETTER = threading.Thread(target=counterletter) # THREAD for every letter
        threads_list.append(threadLETTER)
        threadLETTER.daemon = True 
        threadLETTER.start()
        
for _ in range(26):
     labelLETTER1[_] = tk.Label(root, textvariable=labelLETTER[_], font=("arial", 9), image=img_tk, compound="center", fg="black")
     labelLETTER1[_].grid(row=_ // 3, column=_ % 3, padx=10, pady=10)

listenLETTERS()

root.mainloop()
