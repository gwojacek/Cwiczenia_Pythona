from typing import List

# możemy określć czym będzie dany argument (intem, floatem, lista, tuple, setem) i czym ma być output ( -> float)

#
# def list_avg(sequence: List) -> float:
#     return sum(sequence) / len(sequence)


class Book:
    def __init__(self, name):
        self.name = name

#bez repr drukowało jako object Main xxxxx
    def __repr__(self) -> str:
        return self.name

book = Book("Harry Potter")
book2 = Book("Second Book")

print(book)
print(book2)


class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        book_format_string = "{} "
        book_string = ""
        for book in self.books:
            book_string += book_format_string.format(book.name)
        return f"Bookshelf with {len(self.books)} {book_string} books"


print(Bookshelf([book, book2]))


class BookCover:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self) -> str:
        return f"Ładne pokazanie obiektu książki o nazwie: {self.name}, rodzaju okładki: {self.book_type}, wagi: {self.weight}g"

    @classmethod
    def hardcover(cls, name: str, page_weight: int):
        return cls(name, cls.TYPES[0], page_weight + 15) # cls jako clasa Book

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "BookCover":
        return cls(name, cls.TYPES[1], page_weight + 5)

book3 = BookCover.hardcover("Trzecia ksiazka z okladka", 100)
print(book3)
