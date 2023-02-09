import csv


def export_data():
    with open("phonebook.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        print("ID".center(5), "Фамилия".center(20), "Имя".center(20),
              "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        for row in reader:
            print(row["ID"].center(5), row["last name"].center(20), row["first name"].center(20),
            row["phone"].center(15), row["note"].center(30))
                  
    