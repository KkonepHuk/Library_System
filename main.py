from library_system import LibrarySystem


'''
--1) Добавить чтение из csv файла--
2) Улучшить хэш - функцию
3) Сделать добавление книги в csv файл
'''

if __name__ == '__main__':
    LS = LibrarySystem(10)
    LS.from_csv('books.csv')
    LS.show()