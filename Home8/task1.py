# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных.

# def work_with_phonebook():
#     choice=show_menu()
#     phone_book=read_txt('c:/Users/ASUS/Desktop/Учеба/Python/Домашка/Homework/Home8/phoneb.txt')
#     while (choice!=7):
#         if choice==1:
#             print_result(phone_book)
#         elif choice==2:
#             last_name=input('lastname ')
#             print(find_by_lastname(phone_book,last_name))
#         elif choice==3:
#             last_name=input('lastname ')
#             new_number=input('new number ')
#             print(change_number(phone_book,last_name,new_number))
#         elif choice==4:
#             lastname=input('lastname ')
#             print(delete_by_lastname(phone_book,lastname))
#         elif choice==5:
#             number=input('number ')
#             print(find_by_number(phone_book,number))
#         elif choice==6:
#             user_data=input('new data ')
#             add_user(phone_book,user_data)
#             write_txt('phonebook.txt',phone_book)
#         choice=show_menu()
    

# def show_menu():
#     print('1. Распечатать справочник\n'
#         '2. Найти телефон по фамилии\n'
#         '3. Изменить номер телефона\n'
#         '4. Удалить запись\n'
#         '5. Найти абонента по номеру телефона\n'
#         '6. Добавить абонента в справочник\n'
#         '7. Закончить работу')
#     choice=int(input())
#     return choice

# def read_txt(filename):
#     phone_book=[]
#     fields=['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
#     with open('phoneb.txt','r',encoding='utf-8') as phb:
#         for line in phb:
#             record=dict(zip(fields,line.strip().split(',')))
#             phone_book.append(record)
#     return phone_book

# def write_txt(phon,phone_book):
#     with open('phoneb.txt','w',encoding='utf-8') as phout:
#         for i in range(len(phone_book)):
#             s=''
#             for v in phone_book[i].values():
#                 s+=v+','
#                 phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    #phone_book.readline()'\n'
    for i in phone_book:
        print(f'{i}\n')

phone_book = open(phoneb.txt)

print_result(phone_book)
# work_with_phonebook()
