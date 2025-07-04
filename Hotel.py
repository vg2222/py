from termcolor import cprint, colored
import time
import os

os.system('cls')

def slow_print(text, color_, attrs_=None, time_=0.05):
    for char in text:
        cprint(char, end="", flush=True, color=color_, attrs=attrs_)
        time.sleep(time_)
        
    print("\n\n")
cprint("-- Сценка: Отель --", "yellow", attrs=["bold"])

for _ in range(10):
    print("")

slow_print("*Вы зашли в отель и подошли к ресепшену*", "yellow")

time.sleep(1)
print("\n\n")

def scene_31():
    print("\n")
    cprint("*Терминал*", "black")
    slow_print("Подключение к серверу", "black", attrs_=["reverse"], time_=0.01)
    slow_print(".........", "black", attrs_=["reverse"], time_=0.5)
    print("")
    slow_print("Выполнение транзакции", "black", attrs_=["reverse"], time_=0.01)
    slow_print(".....", "black", attrs_=["reverse"], time_=0.5)
    print("\n")
    slow_print("Успешно", "green", attrs_=["reverse"], time_=0.01)
    print("\n\n")

    w = open("data.txt", "w")
    w.write("12")
    w.close()

    slow_print("Сотрудник: Ваш номер - 305, вот ваша карточка", "blue")
    print("\n\n")
    time.sleep(0.5)
    cprint("1. Спасибо!", "magenta")
    time.sleep(0.5)

    print("\n")

    choose = input(colored("Выберите действие: ", "green"))
    os.system('cls')
    if choose == "1":
        cprint("Конец!", "magenta", attrs=["bold"])
        rating = input(colored("\n\nОценка от 1 до 10: ", "magenta"))

        f = open("rating.txt", "w", encoding="utf-8")
        f.write(f"Оценка: {rating}\n\n")
        f.close()

        os.system('cls')

        cprint("Конец!", "magenta", attrs=["bold"])
        cprint("\n\nОценка от 1 до 10: ", "magenta", end="")
        cprint("10", attrs=["bold"])
    else:
        cprint("Неверный ввод", "red")
        print("\n\n")

        scene_31()

def scene_21():
    slow_print("Сотрудник: Сейчас спрошу у администрации", "blue")
    slow_print("............\n", "blue", time_ = 0.3)

    slow_print("Хорошо, номер будет стоить ", "blue")
    cprint("7500 рублей", "cyan", end="")

    print("\n\n")

    time.sleep(0.5)
    cprint("1. Оплатить картой", "magenta")
    time.sleep(0.5)

    print("\n")

    choose = input(colored("Выберите действие: ", "green"))
    os.system('cls')
    if choose == "1":
        scene_31()
    else:
        cprint("Неверный ввод", "red")
        print("\n\n")

        scene_21()

def scene_11():
    print("\n")
    slow_print("...", "blue", time_=0.5)
    print("\n")

    slow_print("Сотрудник: Хорошо, какой номер вы хотите забронировать?", "blue")
    print("\n\n")
    def select():
        time.sleep(0.5)
        cprint("1. Эконом", "magenta")
        time.sleep(0.5)
        cprint("2. Стандарт", "magenta", attrs=["dark"])
        time.sleep(0.5)
        cprint("3. Комфорт", "magenta")
        time.sleep(0.5)
        cprint("4. Премиум", "magenta", attrs=["dark"])
        time.sleep(0.5)

        print("\n")

        choose = input(colored("Выберите действие: ", "green"))
        os.system('cls')
        if choose == "1":
            scene_12()
        else:
            cprint("У вас не хватает денег!", "red")
            print("\n\n")

            scene_11()
    
    select()

def scene_12():
    print("\n")
    slow_print("...", "blue", time_=0.5)
    print("\n")

    slow_print("Сотрудник: Хорошо, этот номер стоит ", "blue")
    cprint("10000 рублей", "cyan", end="")

    print("\n\n")

    time.sleep(0.5)
    cprint("1. А можно узнать, есть ли скидка 25% на этот номер?", "magenta")

    print("\n")

    choose = input(colored("Выберите действие: ", "green"))
    os.system('cls')
    if choose == "1":
        scene_21()
    else:
        cprint("Неверный ввод", "red")
        print("\n\n")

        scene_12()
        
    
def scene_00():
    cprint("Сотрудник: ", "blue", end="")
    slow_print("Здравствуйте. Чем я могу вам помочь?", "cyan")
    print("\n\n")

    time.sleep(0.5)
    cprint("1. Здравствуйте, я хочу забронировать номер", "magenta")
    time.sleep(0.5)
    cprint("2. Здравствуйте, можно пожалуйста самый дешевый номер?", "magenta", attrs=["dark"])
    print("\n")

    choose = input(colored("Выберите действие: ", "green"))
    os.system('cls')
    if choose == "1":
        scene_11()
    elif choose == "2":
        scene_12()
    else:
        cprint("Неверный ввод", "red")
        print("\n\n")

        scene_00()

scene_00()