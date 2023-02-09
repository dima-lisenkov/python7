from print_name import print_for_name as printname
from import_data import import_data as im_data
from sort_data import sorting_for_ID as sortID
from sort_data import sorting_for_name as sortName
from export_data import export_data as ex_data
from csv_create import creating
import os
import time

def button_push():
    print("Что будем делать?\n"
          "1. - создать новый телефонный справочник\n"
          "2. - добавить контакт в существующий файл\n"
          "3. - экспортировать файл в программу\n"
          "4. - отсортировать файл\n"
          "5. - печать файла в консоли\n"
          "0. - для выхода из программы\n")
    opp_type = int(input("->> "))
    os.system('cls')
    if opp_type == 1:
        os.system('cls')
        creating()
        print("Новая база создана... хозяин)")
        time.sleep(2)
        button_push()
    elif opp_type == 2:
        os.system('cls')
        im_data(input_data())
        print("Добавляем новый контакт")
        time.sleep(2)
        button_push()
    elif opp_type == 3:
        os.system('cls')
        print("Экспортирую данные...")
        ex_data()
        continue_d = input("Нажмите любую клавишу для продолжения работы... ")
        os.system('cls')
        button_push()
    elif opp_type == 4:
        os.system('cls')
        print("Выберите тип сортировки:\n"
              "1 - сортировать по ID\n"
              "2 - сортировать по имени\n")
        type_sort = int(input("->> "))
        if type_sort == 1:
            sortID()
            continue_d = input("Нажмите любую клавишу для продолжения работы... ")
            os.system('cls')
            button_push()
        elif type_sort == 2:
            sortName()
            continue_d = input("Нажмите любую клавишу для продолжения работы... ")
            os.system('cls')
            button_push()
        else:
            print("Выбор не верный ... сынок!")
            time.sleep(2)
            button_push()
    elif opp_type == 5:
        os.system('cls')
        print("Печать файла...")
        printname()
        continue_d = input("Нажмите любую клавишу для продолжения работы... ")
        os.system('cls')
        button_push()
    else: pass


def input_data():
    data = []
    item_data = input("Введите индификационыый номер: ")
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    data = [item_data, last_name, first_name, phone_number, note]
    return data