import csv


def import_data(data):
    with open("phonebook.csv", "a+", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(data)