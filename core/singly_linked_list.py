from book import Book


class Node:
    def __init__(self, book):
        self.key = book.isbn
        self.book = book
        self.next = None

class SinglyLinkedList:

    #Инициализация односвязного списка
    def __init__(self):
        self.head = None
        self.length = 0

    #Строковый формат
    def __str__(self):
        current = self.head
        s = ''
        while current:
            s += f'{str(current.book)}->'
            current = current.next
        return s[:-2]

    #Добавление в начало списка
    def add_to_start(self, book):
        new_node = Node(book)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    #Удаление узла
    def remove(self, key):
        current = self.head
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    #Удаление головы
                    self.head = current.next
                else:
                    prev.next = current.next

                self.length -= 1
                return
            prev = current
            current = current.next

    
    #Удаление узла из начала
    def remove_from_start(self):
        if self.head:
            removed = self.head
            self.head = self.head.next
            self.length -= 1
            return removed
    
    
    #Наглядный вывод списка на экран для тестов
    def test_show(self):
        return self.__str__()
    
    def show(self):
        current = self.head
        s = ''
        while current:
            s += f'{str(current.book)}\n'
            current = current.next
        return s[:-2]

    #Поиск в списке значения по ключу
    def find(self, isbn):
        current = self.head
        while current:
            if current.key == isbn:
                return current.book
            current = current.next
        return -1
    
    #Односвязный список в двумерный массив
    def list_to_arr(self):
        data = []
        current = self.head
        while current:
            data.append(current.book.book_to_arr())
            current = current.next
        return data


if __name__ == '__main__':
    sll = SinglyLinkedList()
    book1 = Book('123456789012', 'Спокойной ночи малыши', 'Сергей Потапов', '2007', 'Хорор', 'в наличии')
    book2 = Book('929140219324', 'Малышарики', 'Ирина Петрова', '2011', 'Комедия', 'в наличии')
    book3 = Book('342982381031', 'Путь к успеху', 'Николай Соболев', '2001', 'Триллер', 'выдана')
    sll.add_to_start(book1)
    sll.add_to_start(book2)
    sll.add_to_start(book3)
    print(sll)
    print('Поиск:')
    print(sll.find('123456789012'))
    print('-' * 75)
    sll.remove_from_start()
    print(sll)
    print('-' * 75)
    sll.remove('123456789012')
    print(sll)
    print()
    print(sll.show())

