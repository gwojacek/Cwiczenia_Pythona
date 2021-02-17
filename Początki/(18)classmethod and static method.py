class ClassTest:

    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

#instance_method potrzebuje obiektu, by móc operować na tej metodzie
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method() # python sam doda do środka nawiasu w class_metodzie ClassTest, wiec nie trzeba dopisywać.
# czyli nie trzeba pracować na obiekcie, klasa jest argumentem

ClassTest.static_method() # nie uzywa ani klasy ani obiektów. Jest po prostu funkcją, którą z jakiegoś powodu chcesz wstawić do danej klasy

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self,name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self):
        return f"Ładne pokazanie obiektu książki o nazwie: {self.name}, rodzaju okładki: {self.book_type}, wagi: {self.weight}"

    # print(Book.TYPES)
    #
    # book = Book("Harry Potter", "hardcover", 2)
    # print(book)

    @classmethod
    def hardcover(cls,name,page_weight):
        return cls(name, cls.TYPES[0], page_weight + 15) # cls jako clasa Book

    @classmethod
    def paperback(cls,name,page_weight):
        return Book(name, Book.TYPES[1], page_weight + 5)

book_hard = Book.hardcover('Harry Potter 222', 2)
book_light = Book.paperback('Harry Potter 555', 1)
print(book_hard)
print(book_light)

"***********************88888888**************************************************"

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # return f"{store.name} , total stock price: {int(store.stock_price())}"
        #or
        return '{} , total stock price: {}'.format(store.name, int(store.stock_price()))

        # It should be in the format 'NAME, total stock price: TOTAL'

    def __str__(self):
        return self.name

store = Store("Test")
store2 = Store("Amazon")
store2.add_item('Kebab', 10)
print(store2.items)

print(store.franchise(store))
print(store2.franchise(store2))
print(store2)
print(store2.store_details(store2))
