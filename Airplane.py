import urllib.request
from termcolor import colored, cprint
import time

cprint("Скачивание файлов...", "blue")
urllib.request.urlretrieve("https://raw.githubusercontent.com/vg2222/py/refs/heads/main/air.ico", "air.ico")
cprint("Успешно", "green")

cprint("Инициалилизация...", "blue")
w = open("data.txt", "w")
w.write("")
w.close()
cprint("Готово...", "green")

import tkinter as tk
import customtkinter

fullscreen = False
root = tk.Tk()

root.geometry("820x520")
root.title("Управление")
root.iconbitmap("air.ico")

root.configure(bg="#ede8e8") 
label = tk.Label(root, text="Управление клиентами", font=("Montserrat Bold", 32), bg="#ede8e8")
label.place(x=140, y=22)

label2 = tk.Label(root, text="Паспортные данные", font=("Montserrat Medium", 12), bg="#ede8e8")
label2.place(x=319, y=110)

entry = tk.Entry(root, font=("Montserrat Medium", 12), bg="#ede8e8", width=19)
entry.place(x=300, y=145)

label2 = tk.Label(root, text="Номер клиента", font=("Montserrat Medium", 12), bg="#ede8e8")
label2.place(x=339, y=175)

entry2 = tk.Entry(root, font=("Montserrat Medium", 12), bg="#ede8e8", width=19)
entry2.place(x=300, y=205)


def register():
    if entry.get() != "" and entry2.get() != "":
        btn1.configure(text="Печать билета...")
        btn1.place(x=320, y=470)

btn1 = customtkinter.CTkButton(
    root,
    text='Напечатать билет',
    font=("Montserrat Bold", 16),
    text_color="#1F1F1F",
    fg_color="#c2c2c2",
    hover_color="#929292",
    corner_radius=50,
    command=lambda: register()
    )

btn1.place(x=310, y=470)

root.mainloop()