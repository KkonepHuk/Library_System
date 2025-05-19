import csv
from book import Book
from singly_linked_list import SinglyLinkedList


class LibrarySystem:
    #Инициализирование Хэш-Таблицы с заданным размером size
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.occupancy = 0

    #Хэш-функция
    def hash_func(self, isbn):
        clean_isbn = "".join(c for c in isbn if c.isdigit() or c == "-")
        selected = list(map(int, clean_isbn.split("-")))
        hash_value = (selected[1] << 8) + selected[2] * 31 + selected[3] % 17 + selected[4]
        return hash_value % self.size

    #Увеличение на 1 счётчика заполненных ячеек Хэш-Таблицы
    def incr_occupation(self):
        self.occupancy += 1
    
    #Уменьшение на 1 счётчика заполненных ячеек Хэш-Таблицы
    def decr_occupation(self):
        self.occupancy -= 1
    
    #Вычисление коэффициента заполнения таблицы
    def occupancy_rate(self):
        return self.occupancy / self.size if self.size > 0 else 0
    
    @staticmethod
    def expansion(add_func):
        def wrapper(self, *args):
            if self.occupancy_rate() >= 2 / 3:
                new_size = self.size + int(self.size * 2 / 3)
                new_library_system = LibrarySystem(new_size)
                for sll in self.table:
                    while sll and sll.head:
                        node = sll.remove_from_start()
                        book = node.book
                        new_library_system.add(book)
                self.size = new_library_system.size
                self.table = new_library_system.table
                self.occupancy = new_library_system.occupancy

            return add_func(self, *args)
        return wrapper
    
    #Добавление книги
    @expansion
    def add(self, book):
        ind = self.hash_func(book.isbn)
        if self.table[ind] == None:
            sll = SinglyLinkedList()
            sll.add_to_start(book)
            self.table[ind] = sll
        else:
            self.table[ind].add_to_start(book)
        self.incr_occupation()
    
    #Удаление книги по ее "ISBN"
    def remove(self, isbn):
        ind = self.hash_func(isbn)
        if self.table[ind] == None:
            return -1
        elif self.table[ind].length > 1:
            self.table[ind].remove(isbn)
        else:
            self.table[ind] = None
        self.decr_occupation()
    
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
    LS = LibrarySystem(100)
    '''
    Тест на работу цепочек при коллизиях
     ||
     \/
    '''

    '''
    sll = SinglyLinkedList()
    collisia_book = Book('325234234', 'd', 'd', '4', 'd', 'd')
    sll.add_to_start(collisia_book)
    LS.table[1] = sll
    '''

    
    book1 = Book('978-0-679-72232-8', 'Спокойной ночи малыши', 'Сергей Потапов', '2007', 'Хорор', 'в наличии')
    book2 = Book('978-0-452-28423-4', 'Малышарики', 'Ирина Петрова', '2011', 'Комедия', 'в наличии')
    book3 = Book('978-0-06-112008-4', 'Путь к успеху', 'Николай Соболев', '2001', 'Триллер', 'выдана')

    book4 = Book('978-1-85326-000-1', 'Пятерочка','Николай Бабушкин','5269', 'Биография','в налачии')
    LS.add(book1)
    LS.add(book2)
    LS.add(book3)
    LS.show()
    print('-' * 150)
    print(LS.get('978-0-679-72232-8'))
    LS.remove('978-0-679-72232-8')
    LS.show()
    print('-' * 150)
    LS.remove('978-0-452-28423-4')
    LS.show()
    #print(LS.get('978-0-679-72232-8'))
    print('-' * 150)
    print(LS.get('978-1-85326-000-1'))
    LS.change_status('978-1-85326-000-1')
    print(LS.get('978-1-85326-000-1'))
    print()
    LS.show()
    print(LS.library_to_arr())