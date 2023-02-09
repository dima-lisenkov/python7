def creating ():
    file = 'phonebook.csv'
    with open (file, 'w') as data:
        data.write(f'ID;last name;first name;phone;note\n')