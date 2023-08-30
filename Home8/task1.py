# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных.

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия ')
            print(*find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('Фамилия ')
            new_number=input('Новый номер телефона ')
            change_number(phone_book,last_name,new_number)
        elif choice==4:
            lastname=input('Фамилия ')
            delete_by_lastname(phone_book,lastname)
        elif choice==5:
            number=input('Номер ')
            find_by_number(phone_book,number)
        elif choice==6:
            user_data=input('Новая запись (Введите Фамилию, Имя, Телефон, Описание): ')
            add_user(phone_book,user_data)
        choice=show_menu()
    f = input('Хотите сохранить изменения? да/нет ').lower()
    if f == 'да':
        write_txt('phonebook.txt',phone_book)
        print('Изменения сохранены')
    
# меню запрос для пользователя
def show_menu():
    print('1. Распечатать справочник\n'
        '2. Найти телефон по фамилии\n'
        '3. Изменить номер телефона\n'
        '4. Удалить запись\n'
        '5. Найти абонента по номеру телефона\n'
        '6. Добавить абонента в справочник\n'
        '7. Закончить работу')
    choice=int(input())
    return choice

# создаем список из словарей для работы
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    # fields = ['lastname ', 'name ', 'number ', 'comment']
    with open('phonebook.txt','r',encoding='utf-8') as phb:
        for line in phb:
            record=dict(zip(fields,line.strip().split(',')))
            phone_book.append(record)
    return phone_book

# 1. Распечатать телефонный справочник
def print_result(phone_book):
    for i in phone_book:
        print(i)   #(f'{i}\n')
             

# 2. Найти телефон по фамилии
def find_by_lastname(phone_book,last_name):
    name = last_name.strip()
    fio = []
    for i in phone_book:
        if i['Фамилия'] == name:
            fio.append(i)
    if len(fio)==0: print('Абонента в справочнике нет')
    return fio

# 3. Изменить номер телефона
def change_number(phone_book,last_name,new_number):
    name = last_name.strip()
    number = new_number.strip()
    fio = []
    for i in phone_book:
        if i['Фамилия'] == name:
            print(i)
            f = input('Хотите изменить этот номер телефона? да/нет ').lower()
            if f == 'да':
                i['Телефон'] = number
                fio.append(i)
                print('Номер изменен ')
        return phone_book

# 4. Удалить запись
def delete_by_lastname(phone_book,lastname):
    name = lastname.strip()
    fio = []
    for i in phone_book:
        if i['Фамилия'] == name:
            print(i)
            f = input('Хотите удалить эту запись? да/нет ').lower()
            if f == 'да':
                fio.append(i)
                phone_book.remove(i)
                print('Запись удалена')
    return phone_book
    
# 5. Найти абонента по номеру телефона
def find_by_number(phone_book,number):
    number = number.strip()
    count = 0
    for i in phone_book:
        if i['Телефон'] == number:
            print(i)
            count +=1
    if count == 0: print('Абонента с таким номером телефона нет')
    else: print(f'Найдено {count} абонентов')

# 6. Добавить абонента в справочник
def add_user(phone_book,user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    n = dict(zip(fields,user_data.strip().split(',')))
    print(n)
    phone_book.append(n)
    return phone_book

def write_txt(filename,phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as fio:
        
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            fio.write(f'{s[:-1]}\n')
    return fio

work_with_phonebook()
