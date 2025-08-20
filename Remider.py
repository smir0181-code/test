from tkinter import*
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame
t=0
music = False

def set():
    global t
    rem=sd.askstring("Время напоминания","Введите время напоминания в формате ЧЧ:ММ(в 24  формате)")
    if rem:
        try:
            hour=int(rem.split(":")[0])
            minute=int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute,second=0)
            print(dt)
            t=dt.timestamp()
            print(t)
            text=sd.askstring("Текст напоминания", "Введите текст напоминания")
            label.config(text=text)
            label.config(text=f"Напоминание установлено на {hour:02}:{minute:02} с текстом {text}")
            check()
        except Exception as e:
            mb.showerror("Ошибка",f"Некорректное время{e}")
def check():
    global t
    if t:
        now=time.time()
        if now>=t:
            play_snd()
            t=0
    window.after(10000, check) 
def play_snd():
 
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()
    global music
    music = True
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)
def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")
        


window = Tk()
window.title("Напоминание")
window.geometry("450x150")

label= Label(text="Установите напоминание",font=("Arial", 14))
label.pack(pady=10)


set_button = Button(text="Установить",font=("Arial", 11), command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку",font=("Arial", 11), command=stop_music)
stop_button.pack(pady=5)

window.mainloop()