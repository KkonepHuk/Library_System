import csv
import os


class Book:
    #Инициализирование класса "Book"
    def __init__(self, isbn, name, autor, year, genre, status):
        self.isbn = isbn
        self.name = name
        self.autor = autor
        self.year = year
        self.genre = genre
        self.status = status
    
    def __str__(self):
        s = f'[ISBN: {self.isbn}, Name: {self.name}, Autor: {self.autor}, Year of publication: {self.year}, Genre: {self.genre}, Status: {self.status}]'
        return s
    
    def book_to_arr(self):
        return [self.isbn, self.name, self.autor, self.year, self.genre, self.status]
    
    @classmethod
    def from_csv(cls, arr):
        return cls(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
    

if __name__ == '__main__':
    CSV_FILE = os.path.join('csv_files', 'books2.csv')
    with open(CSV_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            book = Book.from_csv(row)
            print(book)
    print()
    book3 = Book('342982381031', 'Путь к успеху', 'Николай Соболев', '2001', 'Триллер', 'выдана')
    print(book3.book_to_arr())