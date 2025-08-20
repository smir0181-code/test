from tkinter import*
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

window = Tk()
window.title("Напоминание")
window.geometry("300x250")
label= Label(text="Установите напоминание")
label.pack(pady=10)
set_button = Button(text="Установить", command=set_reminder)
set_button.pack(pady=10)


window.mainloop()