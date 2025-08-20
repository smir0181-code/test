from tkinter import*
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame
t=0

def set():
    global t
    rem=sd.askstring("Время напоминания","Введите время напоминания в формате ЧЧ:ММ(в 24 часовом формате)")
    if rem:
        try:
            hour=int(rem.split(":")[0])
            minute=int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute)
            print(dt)
            t=dt.timestamp
            print(t)
        except Exception as e:
            mb.showerror("Ошибка",f"Некорректное время{e}")
def check():
    global t
    if t:
        now=time.time()
        if now>=t:
            play_snd()
            t=0
    window.after(1000, check)         


window = Tk()
window.title("Напоминание")
window.geometry("300x250")
label= Label(text="Установите напоминание",font=23)
label.pack(pady=10)
set_button = Button(text="Установить", command=set)
set_button.pack(pady=10)


window.mainloop()