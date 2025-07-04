import urllib.request
from termcolor import colored, cprint
import time
import threading

cprint("Скачивание файлов...", "blue")
urllib.request.urlretrieve("https://raw.githubusercontent.com/vg2222/py/refs/heads/main/hotel.ico", "hotel.ico")
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
root.title("Управление данными")
root.iconbitmap("hotel.ico")

root.configure(bg="#ede8e8") 
label = tk.Label(root, text="Стойка регистрации", font=("Montserrat Bold", 32), bg="#ede8e8")
label.place(x=170, y=15)

label2 = tk.Label(root, text="Паспортные данные", font=("Montserrat Medium", 12), bg="#ede8e8")
label2.place(x=319, y=80)

entry = tk.Entry(root, font=("Montserrat Medium", 12), bg="#ede8e8", width=19)
entry.place(x=300, y=115)

label2 = tk.Label(root, text="Номер клиента", font=("Montserrat Medium", 12), bg="#ede8e8")
label2.place(x=339, y=145)

entry2 = tk.Entry(root, font=("Montserrat Medium", 12), bg="#ede8e8", width=19)
entry2.place(x=300, y=175)

label2 = tk.Label(root, text="Ожидание оплаты от клиента", font=("Montserrat Medium", 32), bg="#ede8e8")
label2.place(x=75, y=260)

label2.config(fg="#c74242")

def register():
    w = open("data.txt", "r")
    data = w.read()
    w.close()

    if "12" in data:
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)

        btn1.config(text="Клиент зарегестрирован")


def update():
    while True:
        time.sleep(0.5)

        w = open("data.txt", "r")
        data = w.read()
        w.close()

        if "12" in data:
            label2.config(text="Оплата получена")
            label2.config(fg="#66d166")
            label2.place(x=200, y=270)
            print("got it")

threading.Thread(target=update, daemon=True).start()

btn1 = customtkinter.CTkButton(
    root,
    text='Заселить в номер 305',
    font=("Montserrat Bold", 16),
    text_color="#1F1F1F",
    fg_color="#c2c2c2",
    hover_color="#929292",
    corner_radius=50,
    command=lambda: register()
    )

btn1.place(x=292, y=470)

root.mainloop()