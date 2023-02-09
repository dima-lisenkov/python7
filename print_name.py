import csv


def print_for_name():
    with open("phonebook.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        print("Фамилия".center(10), "Имя".center(20))
        print("-"*25)
        for row in reader:
            print(row["last name"].center(10), row["first name"].center(20))