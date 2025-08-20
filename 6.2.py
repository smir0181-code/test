from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None
music = False  # Переменная для отслеживания проигрывания музыки

def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24 формат)")
    if rem:
        try:
            
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                raise ValueError
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            t = dt.timestamp()
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")

def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
    window.after(10000, check)
def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()