
file = open('database_phone.csv', 'w')
newrecord ="id;name;surname;phoneNumber\n"
file.writelines(newrecord)

ls_name = ['Svetlana', 'Olga', 'Anton', 'Anna', 'Inna', 'Viktor', 'Vasilisa', 'Alex', 'Miron', 'Igor', 'Anna']
ls_surname = ['Kovalenko', 'Sidorenko', 'Mironenko', 'Galich', 'Shapiro', 'Duma', 'Duma', 'Shagal', 'Moroz']

import random

def list_of_numbers():
    s = '0'
    randomListPhone = random.randint(54000000000, 55000000000)
    s += str(randomListPhone)
    return s

def string_creation():
    s = ""
    s += random.choice(ls_name) + ';' + random.choice(ls_surname) + ';' + list_of_numbers()
    return s


for i in range(100):
    a = f'{str(i + 1)};{string_creation()}\n'
    file.write(a)
file.close()