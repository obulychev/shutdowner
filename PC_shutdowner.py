#!/usr/bin/python3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
import sys
import datetime

def platform_check():
    if sys.platform == ('linux'):
        shutdown_time_linux()
    elif sys.platform == ('win32'):
        shutdown_time_windows()
    else:
        messagebox.showinfo('ОС не поддерживается','Ваша операционная система не поддерживается')
        window.destroy()

def shutdown_time_linux():
    if str(hours_menu.get()) == '' or str(minutes_menu.get()) == '':
        messagebox.showinfo("Будь внимательнее!", 'Введи время!')
    else:
        os.system('shutdown -h ' + str(hours_menu.get()) + ':' + str(minutes_menu.get()))
        messagebox.showinfo("Выключение ПК",'Компьютер будет выключен в ' + str(hours_menu.get()) + ':' + str(minutes_menu.get()))
        window.destroy()

def shutdown_time_windows():
    os.system('shutdown -a')
    now = datetime.datetime.now()
    timenow = now.strftime("%H:%M")
    if str(hours_menu.get()) == '' or str(minutes_menu.get()) == '':
        messagebox.showinfo("Будь внимательнее!", 'Введи время!')
    else:
        hours_now = int(str(timenow[0] + timenow[1]))
        min_now = int(str(timenow[-2] + timenow[-1]))
        if (int(hours_menu.get()) <= hours_now) and (min_now >= int(minutes_menu.get())):
            time_difference = (24-hours_now)+int(hours_menu.get())
            os.system('shutdown -s -t ' + str((time_difference * 3600) + (int(minutes_menu.get()) * 60 - min_now * 60)))
            messagebox.showinfo("Выключение ПК",'Компьютер будет выключен в ' + str(hours_menu.get()) + ':' + str(minutes_menu.get()))
        else:
            os.system('shutdown -s -t ' + str((int(hours_menu.get()) * 3600 + int(minutes_menu.get()) * 60) - (hours_now * 3600 + min_now * 60)))
            messagebox.showinfo("Выключение ПК",'Компьютер будет выключен в ' + str(hours_menu.get()) + ':' + str(minutes_menu.get()))
        window.destroy()

def shutdown_cancel():
    if sys.platform == ('linux'):
        shutdown_cancel_linux()
    elif sys.platform == ('win32'):
        shutdown_cancel_windows()
    else:
        messagebox.showinfo('ОС не поддерживается', 'Ваша операционная система не поддерживается')
        window.destroy()

def shutdown_cancel_linux():
    os.system('shutdown -c')
    messagebox.showinfo("Отмена выключения", 'Автоматическое выключение компьютера отменено')
    window.destroy()

def shutdown_cancel_windows():
    os.system('shutdown -a')
    messagebox.showinfo("Отмена выключения", 'Автоматическое выключение компьютера отменено')
    window.destroy()

window=Tk()
window.title("PC Shutdowner")
text1 = Label(text="В какое время выключить ПК? \n")
text1.pack()
f_top = Frame(window)
f_bot = Frame(window)



hours_menu=ttk.Combobox(f_top,values = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"])

minutes_menu=ttk.Combobox(f_top, values = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20", \
    "21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50", \
    "51", "52", "53", "54", "55", "56", "57", "58", "59"])


button1 = Button(f_bot, bg="grey", text=u"Выключить пк в заданное время!", command=platform_check)
button2 = Button(f_bot, bg="grey", text=u"Отменить выключение пк", command=shutdown_cancel)
f_top.pack()
f_bot.pack()
hours_menu.pack(side=LEFT)
minutes_menu.pack(side=LEFT)
button1.pack()
button2.pack()
window.mainloop()