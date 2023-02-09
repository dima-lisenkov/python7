import csv
import operator


def sorting_for_ID():
    data = csv.reader(open('phonebook.csv'), delimiter=';')
    data = sorted(data, key=operator.itemgetter(0))
    for row in data:
        print(row[0].center(5), row[1].center(20), row[2].center(20),
              row[3].center(15), row[4].center(30))


def sorting_for_name():
    data = csv.reader(open('phonebook.csv'), delimiter=';')
    data = sorted(data, key=operator.itemgetter(2))
    for row in data:
        print(row[0].center(5), row[1].center(20), row[2].center(20),
              row[3].center(15), row[4].center(30))