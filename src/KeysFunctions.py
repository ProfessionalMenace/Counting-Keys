import time
import keyboard
import tkinter
import threading
from variables import firstpression, keys, labelCharacter1, labelCharacter, root, lastrepeat, lastpression, functionalkey, modifierkeys, current_time, controlkeys


def Bfunc(index1, index2, key = 'b', labletext = None): # KEYS = the variable, # index1 and index2 are the index of the matrix, root is the root and function_update is the function which give you the possibility to update the label, key is the key, labletext is the lable text+
    def update():
        labletext[index1][index2].set(f" {key} = {keys[index1][index2]}")

    def debounce():
        global lastpression
        current_time[index1][index2] = time.time()
        if (current_time[index1][index2] - lastpression[index1][index2]) > 0.2:
            lastpression[index1][index2] = current_time[index1][index2]
            return True
        return False

    def key_repeat():
        global lastrepeat
        current_time[index1][index2] = time.time()
        if (current_time[index1][index2] - lastpression[index1][index2]) >= 0.5 and \
           (current_time[index1][index2] - lastrepeat[index1][index2]) >= 0.1:
            lastrepeat[index1][index2] = current_time[index1][index2]
            return True
        return False
    while True:
        if keyboard.is_pressed(key):
            if debounce():
                        keys[index1][index2] += 1
                
            if key_repeat():
                 keys[index1][index2] += 1
        else:
            time.sleep(0.01)
        root.after(1500, lambda: update())

def listenKEYS():
        for _ in range(len(keys)):
            for i in range(len(keys[_])):
                def counterletter(index2char=i, index1char=_ ):
                    if _ == 0:
                         Bfunc(index1char, index2char, f'{chr(index2char+97)}', labelCharacter)
                    elif _ == 1:
                         Bfunc(index1char, index2char, f'{chr(index2char+48)}', labelCharacter)
                    elif _ == 2:
                         Bfunc(index1char, index2char, functionalkey[i], labelCharacter)
                    elif _ == 3:
                         Bfunc(index1char, index2char, modifierkeys[i], labelCharacter)
                    elif _ == 4:
                         Bfunc(index1char, index2char, controlkeys[i], labelCharacter)
                             
                         
                         
                threadLETTER = threading.Thread(target=counterletter) # THREAD for every letter
                threadLETTER.daemon = True 
                threadLETTER.start()

