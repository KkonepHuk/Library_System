import os
from library_system import LibrarySystem
from book import Book


'''
--1) Добавить чтение из csv файла--
2) Улучшить хэш - функцию
--3) Сделать добавление книги в csv файл--
--4) Сделать основной цикл программы с выбором действия--
--5) Написать функцию для проверки валидности ISBN--
'''

def show_information():
    s = 'Выберите одно из действий:\n'
    s += '1) Посмотреть текущие книги\n'
    s += '2) Найти книгу по её ISBN\n'
    s += '3) Изменить статус книги\n'
    s += '4) Удалить книгу\n'
    s += '5) Добавить книгу\n'
    s += '6) Сохранить изменения\n'
    s += '7) Выход\n'
    print(s)

def do_action(command):
    if command == '1':
        get_list_of_books()
    elif command == '2':
        isbn = input('Введите ISBN искомой книги: ')
        if is_isbn_valid(isbn):
            find_book(isbn)
    elif command == '3':
        isbn = input('Введите ISBN нужной книги: ')
        if is_isbn_valid(isbn):
            change_book_status(isbn)
    elif command == '4':
        isbn = input('Введите ISBN книги, которую хотите удалить: ')
        if is_isbn_valid(isbn):
            remove_book(isbn)
    elif command == '5':
        add_book()
    elif command == '6':
        save_edits()

def get_list_of_books():
    print('Список доступных книг:\n')
    return LS.show()

def find_book(isbn):
    book = LS.get(isbn)
    if book == -1 or book == None:
        print('Книги с данным ISBN не существует')
    else:
        print(book)

def change_book_status(isbn):
    book = LS.get(isbn)
    if book == -1:
        print('Книги с данным ISBN не существует')
    else:
        LS.change_status(isbn)
        print('Статус книги успешно изменен!')

def remove_book(isbn):
    book = LS.get(isbn)
    if book == -1:
        print('Книги с данным ISBN не существует')
    else:
        LS.remove(isbn)
        print('Книга успешно удалена!')

def add_book():
    isbn = input('Введите ISBN новой книги: ')
    if is_isbn_valid(isbn):
        new_book = get_new_book()
        LS.add(new_book)
        print('Книга успешно добавлена!')

def save_edits():
    LS.save(CSV_FILE)
    print('Все изменения успешно сохранены!')

#Проверка корректности ISBN
def is_isbn_valid(isbn):
    isbn = isbn.replace('-', '').replace(' ', '')
    check_digit = -100
    result = False
    if len(isbn) == 13 and isbn.isdigit():
        honest_summ = sum([int(isbn[i]) for i in range(0, 12, 2)])
        odd_summ = sum([int(isbn[i]) * 3 for i in range(1, 12, 2)])
        summ = honest_summ + odd_summ
        check_digit = (10 - summ % 10) % 10
        result = check_digit == int(isbn[-1])
    if result:
        return True
    print('Неверный ISBN')
    return False


def get_new_book(isbn):
    name = input('Введите название: ')
    autor = input('Введите автора: ')
    year = input('Введите год издания: ')
    genre = input('Введите жанр: ')
    status = 'Available'
    return Book(isbn, name, autor, year, genre, status)


def get_input():
    num = input().strip()
    print()
    return num

def command_checker(num):
    return num in '1234567' and len(num) == 1

def main():
    is_launched = True

    while is_launched:
        show_information()
        command = get_input()
        while not(command_checker(command)):
            print('Вам необходимо ввести одну цифру. Например: 1\n')
            show_information()
            command = get_input()
        if command == '7':
            is_launched = False
        else:
            do_action(command)
        print()


if __name__ == '__main__':
    SIZE = 10 #Размер Хэш-Таблицы (Library System)
    CSV_FILE = os.path.join('csv_files', 'books.csv') #CSV файл с базой данных книг

    LS = LibrarySystem(SIZE)
    LS.from_csv(CSV_FILE)
    main()