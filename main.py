import pyautogui
import tkinter as tk
from tkinter.filedialog import *
import time

screen = tk.Tk()
screen.title('Capturador de pantalla')

canvas1 = tk.Canvas(screen, width = 240, height = 60)
canvas1.pack()

def takeScreenshot():
    screen.withdraw()
    screen.update()
    time.sleep(1)
    my_screenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    my_screenshot.save(save_path + '.png')

button1 = tk.Button(text = 'Capturar pantalla', command = takeScreenshot, font = 10)
canvas1.create_window(120, 30, window = button1)

screen.mainloop()