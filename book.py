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