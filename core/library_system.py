import csv
from core.book import Book
from core.singly_linked_list import SinglyLinkedList


class LibrarySystem:
    #Инициализирование Хэш-Таблицы с заданным размером size
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    #Хэш-функция
    def hash_func(self, isbn):
        clean_isbn = "".join(c for c in isbn if c.isdigit() or c == "-")
        selected = list(map(int, clean_isbn.split("-")))
        hash_value = (selected[1] << 8) + selected[2] * 31 + selected[3] % 17 + selected[4]
        return hash_value % self.size
    
    #Добавление книги
    def add(self, book):
        ind = self.hash_func(book.isbn)
        if self.table[ind] == None:
            sll = SinglyLinkedList()
            sll.add_to_start(book)
            self.table[ind] = sll
        else:
            self.table[ind].add_to_start(book)
    
    #Удаление книги по ее "ISBN"
    def remove(self, isbn):
        ind = self.hash_func(isbn)
        if self.table[ind] == None:
            return -1
        elif self.table[ind].length > 1:
            self.table[ind].remove(isbn)
        else:
            self.table[ind] = None
    
    #Получение книги по ее "ISBN"
    def get(self, isbn):
        ind = self.hash_func(isbn)
        if self.table[ind] == None:
            return -1
        else:
            return self.table[ind].find(isbn)
    
    
    #Вывод всей Хэш-Таблицы(Library System) для тестов
    def test_show(self):
        for i in range(self.size):
            if self.table[i] == None:
                print(f'{i} : {self.table[i]}')
            else:
                print(f'{i} : {self.table[i].show()}')
    
    #Вывод всех книг в Хэш-Таблице(Library System)
    def show(self):
        for i in range(self.size):
            if self.table[i] != None:
                print(f'{self.table[i].show()}')
    
    #Изменение статуса книги по ее "ISBN"
    def change_status(self, isbn):
        ind = self.hash_func(isbn)
        if self.table[ind] == None:
            return -1
        elif self.table[ind].find(isbn).status == 'Available':
            self.table[ind].find(isbn).status = 'Borrowed'
        else:
            self.table[ind].find(isbn).status = 'Available'

    #Преобразует Хэш-Таблицу(Library System) в двумернай массив
    def library_to_arr(self):
        data = [['ISBN','Name','Author','Year','Genre','Status']]
        for i in range(self.size):
            if self.table[i] != None:
                data.extend(self.table[i].list_to_arr())
        return data
    
    #Сохранение Хэш-Таблицы(Library System) в csv файл
    def save(self, csv_file):
        data = self.library_to_arr()
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    
    #Формирование Library System из csv файла
    def from_csv(self, csv_file):
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) #Пропускаем строчку заголовков
            for arr_book in reader:
                new_book = Book.from_csv(arr_book)
                self.add(new_book)


            


if __name__ == '__main__':
    LS = LibrarySystem(10)
    '''
    Тест на работу цепочек при коллизиях
     ||
     \/
    '''

    '''
    sll = SinglyLinkedList()
    collisia_book = Book('325', 'd', 'd', '4', 'd', 'd')
    sll.add_to_start(collisia_book)
    LS.table[1] = sll
    '''

    
    book1 = Book('123456789012', 'Спокойной ночи малыши', 'Сергей Потапов', '2007', 'Хорор', 'в наличии')
    book2 = Book('929140219324', 'Малышарики', 'Ирина Петрова', '2011', 'Комедия', 'в наличии')
    book3 = Book('342982381031', 'Путь к успеху', 'Николай Соболев', '2001', 'Триллер', 'выдана')
    
    '''
    Придумал и написал Коля
     ||
     ||
     \/
    '''

    book4 = Book('124141414441', 'Пятерочка','Николай Бабушкин','5269', 'Биография','в налачии')
    LS.add(book1)
    LS.add(book2)
    LS.add(book3)
    LS.show()
    print('-' * 150)
    print(LS.get('123456789012'))
    LS.remove('123456789012')
    LS.show()
    print('-' * 150)
    LS.remove('342982381031')
    LS.show()
    #print(LS.get('123456789012'))
    print('-' * 150)
    print(LS.get('929140219324'))
    LS.change_status('929140219324', False)
    print(LS.get('929140219324'))
    print()
    LS.show()
    print(LS.to_arr())

