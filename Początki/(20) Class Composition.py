# róznica jest taka, że przy inheritance book jest bookshelfem, a przy composition to są bookshelf ma książke
class Bookshelf:
    def __init__(self, *books): # dzięki gwiazdce można dać tyle argumenrów ile chcemy ( patrz na shelf = Bookshelf(book,book2))

        self.books = books
    #
    # def __str__(self):
    #     return f"Bookshelf has {len(self.books)} books"

    def __str__(self):
        book_format_string = "{} ($ {}) "
        book_string = ""
        for book in self.books:
            book_string += book_format_string.format(book.name, book.price)
        return f"Bookshelf with {len(self.books)} books. These are {book_string}."

class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Books {self.name}"

book = Book ("Harry Potter", 10)
book2 = Book ("Python in pants", 15)
shelf = Bookshelf(book,book2)
print(shelf)
# shelf.books(book, book2)

