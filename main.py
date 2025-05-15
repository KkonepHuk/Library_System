from library_system import LibrarySystem
from book import Book


'''
--1) Добавить чтение из csv файла--
2) Улучшить хэш - функцию
3) Сделать добавление книги в csv файл
4) Сделать основной цикл программы с выбором действия
'''

def show_information():
    s = 'Выберите одно из действий:\n'
    s += '1) Посмотреть текущие книги\n'
    s += '2) Найти книгу по её ISBN\n'
    s += '3) Удалить книгу\n'
    s += '4) Добавить книгу\n'
    s += '5) Сохранить изменения\n'
    s += '6) Выход\n'
    print(s)

def do_action(command):
    if command == '1':
        print('Список доступных книг:\n')
        return LS.show()
    elif command == '2':
        isbn = input('Введите ISBN искомой книги: ') #нужно написать функцию для проверки валидности ISBN
        book = LS.get(isbn)
        if book == -1 or book == None:
            print('Книги с данным ISBN не существует')
        else:
            print(book)
    elif command == '3':
        isbn = input('Введите ISBN книги, которую хотите удалить: ') #нужно написать функцию для проверки валидности ISBN
        book = LS.get(isbn)
        if book == -1 or book == None:
            print('Книги с данным ISBN не существует')
        else:
            LS.remove(isbn)
            print('Книга успешно удалена!')
    elif command == '4':
        new_book = get_new_book()
        LS.add(new_book)
        print('Книга успешно добавлена!')
    elif command == '5':
        LS.save(CSV_FILE)

def get_new_book():
    isbn = input('Введите ISBN новой книги: ') #нужно написать функцию для проверки валидности ISBN
    name = input('Введите её название: ')
    autor = input('Введите её автора: ')
    year = input('Введите год её издания: ')
    genre = input('Введите её жанр: ')
    status = 'Available'
    return Book(isbn, name, autor, year, genre, status)


def get_input():
    num = input().strip()
    print()
    return num

def command_checker(num):
    return num in '123456' and len(num) == 1

def main():
    is_launched = True

    while is_launched:
        show_information()
        command = get_input()
        while not(command_checker(command)):
            print('Вам необходимо ввести одну цифру. Например: 1\n')
            show_information()
            command = get_input()
        if command == '6':
            is_launched = False
        else:
            do_action(command)
        print()


if __name__ == '__main__':
    SIZE = 10 #Размер Хэш-Таблицы (Library System)
    CSV_FILE = 'books.csv' #CSV файл с базой данных книг

    LS = LibrarySystem(SIZE)
    LS.from_csv(CSV_FILE)
    main()