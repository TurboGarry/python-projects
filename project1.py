import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = 'C:/Users/Bennabi/Desktop/udemy-python-course/Screenshot data/{}.png'.format(name)
    # time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#  two buttons
button1 = tk.Button(
    frame,
    text = "Take Sreenshot",
    command = screenshot
)
button1.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text = "Close",
    command = quit
)
close.pack(side=tk.RIGHT)

root.mainloop()