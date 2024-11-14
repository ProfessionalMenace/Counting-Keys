import time
import keyboard
import tkinter
from variables import firstpression, root, keys
def Bfunc(index1, index2, key = 'b', labletext = None, index3 = '0'): # KEYS = the variable, # index1 and index2 are the index of the matrix, root is the root and function_update is the function which give you the possibility to update the label, key is the key, labletext is the lable text+
    def update():
        labletext[index3].set(f" {key} = {keys[index1][index2]}")
    while True:
        if keyboard.is_pressed(key):
                if firstpression:
                    time.sleep(0.3)
                    firstpression = False
                else:
                   time.sleep(0.1)
                keys[index1][index2] += 1
                
        else:
            firstpression = True
            time.sleep(0.1)
        root.after(0, lambda: update())

