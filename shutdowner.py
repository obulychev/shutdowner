#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import re
import datetime
import os
import sys

def platform_check():
    if sys.platform == ('linux'):
        shutdown_time_linux()
    else:
        shutdown_time_windows()

def shutdown_cancel():
    if sys.platform == ('linux'):
        shutdown_cancel_linux()
    else:
        shutdown_cancel_windows()

def shutdown_time_windows():
    os.system('shutdown -a')
    now = datetime.datetime.now()
    timenow = now.strftime("%H:%M")
    if message.get() == '':
        messagebox.showinfo("Будь внимательнее!", 'Введи время!')
    elif str(re.fullmatch(r'^([01]\d|2[0-3]):([0-5]\d)$', str(message.get()))) == 'None':
        messagebox.showinfo("Будь внимательнее!", 'Проверь введенное время на корректность! Формат таков:\n XX:YY')
    else:
        hours_now = int(str(timenow[0] + timenow[1]))
        hours_shutdown = int(str(message.get()[0] + message.get()[1]))
        min_now = int(str(timenow[-2] + timenow[-1]))
        min_shutdown = int(str(message.get()[-2] + message.get()[-1]))
        if (hours_shutdown <= hours_now) and (min_now >= min_shutdown):
            time_difference = (24-hours_now)+hours_shutdown
            os.system('shutdown -s -t ' + str((time_difference * 3600) + (min_shutdown * 60 - min_now * 60)))
            messagebox.showinfo("Выключение ПК", 'Компьютер будет выключен в ' + str(message.get()))
        else:
            os.system('shutdown -s -t ' + str((hours_shutdown * 3600 + min_shutdown * 60) - (hours_now * 3600 + min_now * 60)))
            messagebox.showinfo("Выключение ПК", 'Компьютер будет выключен в ' + str(message.get()))
        window.destroy()

def shutdown_cancel_windows():
    os.system('shutdown -a')
    messagebox.showinfo("Отмена выключения", 'Автоматическое выключение компьютера отменено')
    window.destroy()

def shutdown_time_linux():
    if message.get() == '':
        messagebox.showinfo("Будь внимательнее!", 'Введи время!')
    elif str(re.fullmatch(r'^([01]\d|2[0-3]):([0-5]\d)$', str(message.get()))) == 'None':
        messagebox.showinfo("Будь внимательнее!", 'Проверь введенное время на корректность! Формат таков:\n XX:YY')
    else:
        os.system('shutdown -h ' + str(message.get()))
        messagebox.showinfo("Выключение ПК",'Компьютер будет выключен в ' + str(message.get()))
        window.destroy()

def shutdown_cancel_linux():
    os.system('shutdown -c')
    messagebox.showinfo("Отмена выключения", 'Автоматическое выключение компьютера отменено')
    window.destroy()

window = Tk()
window.title("PC Shutdowner")

text1 = Label(text="В какое время выключить ПК?")
text1.pack()

message = Entry()
message.pack()

button1 = Button(window, bg="grey", text=u"Выключить пк в заданное время!", command=platform_check)
button1.pack()
button2 = Button(window, bg="grey", text=u"Отменить выключение пк", command=shutdown_cancel)
button2.pack()

window = mainloop()