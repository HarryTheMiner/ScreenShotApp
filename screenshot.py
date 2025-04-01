import os 
import time 
import pyautogui
import tkinter as tk

os.environ['TCL_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"


def screenshot():
    name = int(round(time.time()*1000))
    name = 'C:/Users/HP/Desktop/ProjectsForGit/Learn Python With 20+ Real World Projects/screenshotsdata/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

 
 
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take Screen-Shot",
    command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="Quit",
    command=quit)

close.pack(side=tk.LEFT)

root.mainloop()