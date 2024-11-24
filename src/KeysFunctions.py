import time
import keyboard
import tkinter
import threading
from variables import keys, labelCharacter, root, lastrepeat, lastpression, flag, functionalkey, modifierkeys, current_time, controlkeys


def Bfunc(index1, index2, key = 'b', labletext = None): # KEYS = the variable, # index1 and index2 are the index of the matrix, root is the root and function_update is the function which give you the possibility to update the label, key is the key, labletext is the lable text+
    def update():
        labletext[index1][index2].set(f" {key} = {keys[index1][index2]}")

    def debounce():
        global lastpression
        current_time[index1][index2] = time.time()
        if (current_time[index1][index2] - lastpression[index1][index2]) > 0.05 and flag[index1][index2]:
            lastpression[index1][index2] = current_time[index1][index2] 
            flag[index1][index2] = False
            print(flag[index1][index2])
            return True
        return False

    def key_repeat():
        global lastrepeat
        current_time[index1][index2] = time.time()
        if (current_time[index1][index2] - lastpression[index1][index2]) >= 0.25 and \
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
def check(index1, index2, key = "b"):
    while True:
        if not keyboard.is_pressed(key):
            if flag[index1][index2] != True:
                time.sleep(0.2)
                flag[index1][index2] = True
                print("CHECK")
     
def listenKEYS():
    for j in range(len(keys)):
        for i in range(len(keys[j])):
            def counterletter(index1char = j, index2char = i):
                if j == 0:
                    Bfunc(index1char, index2char, f'{chr(index2char+97)}', labelCharacter)
                elif j == 1:
                    Bfunc(index1char, index2char, f'{chr(index2char+48)}', labelCharacter)
                    check(index1char, index2char, f'{chr(index2char+48)}')
                elif j == 2:
                    Bfunc(index1char, index2char, functionalkey[i], labelCharacter)
                    check(index1char, index2char, functionalkey[i])
                elif j == 3:
                    Bfunc(index1char, index2char, modifierkeys[i], labelCharacter)
                    check(index1char, index2char, functionalkey[i])
                elif j == 4:
                    Bfunc(index1char, index2char, controlkeys[i], labelCharacter)
                    check(index1char, index2char, functionalkey[i])
            def checking(index1char = j, index2char = i):
                if j == 0:
                    check(index1char, index2char, f'{chr(index2char+97)}')
                elif j == 1:
                    check(index1char, index2char, f'{chr(index2char+48)}')
                elif j == 2:
                    check(index1char, index2char, functionalkey[i])
                elif j == 3:
                    check(index1char, index2char, functionalkey[i])
                elif j == 4:
                    check(index1char, index2char, functionalkey[i])
                

                             
                         
            threadCHECK = threading.Thread(target=checking)
            threadLETTER = threading.Thread(target=counterletter) # THREAD for every letter
            threadLETTER.daemon = True
            threadCHECK.daemon = True 
            threadLETTER.start()
            threadCHECK.start()