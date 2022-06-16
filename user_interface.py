import data_base_generation

def ls_menu() -> int:
    print('МЕНЮ')
    print('1. Показать все записи.')
    print('2. Найти номер по фамилии.')
    print('3. Найти номер по имени.')
    print('4. Поиск по номеру телефона.')
    print('5. Закрыть программу.')
    n = int(input('Выберите пункт из меню: '))
    return n


def user_choice(n) -> str:
    file = open('database_phone.csv', 'r')
    if n == 1:
        print(data_base_generation)
        ls_menu()
    elif n == 2:
        search = input('Введите фамилию: ')
        for i in file:
            for j in i:
                if j != search:
                    continue
        ls_menu()
    elif n == 3:
        search = input('Введите имя: ')
        for i in file:
            for j in i:
                if j != search:
                    continue
        ls_menu()
    elif n == 4:
        search = input('Введите номер  телефона: ')
        for i in file:
            for j in i:
                if j != search:
                    continue
        ls_menu()
    else:
        file.close()
    return search