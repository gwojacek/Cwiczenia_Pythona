# ponizej mamy wersje gdzie mamy stala zmienna i zmienna zmienna, dlatego sa 2 takie same funkcje, by pokazac mozliwosci
# istotne jest tworzenie obiektu na podstawie klasy i dopiero na nim możemy operować - czyli ten student = Student()
class Student:
    def __init__(self, name, grades_2):
        self.name = name
        self.grades = (12, 23, 41, 21)
        self.grades2 = grades_2

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def average_grade_2(self):
        return sum(self.grades2) / len(self.grades2)

student = Student(name='Jacek', grades_2='') # ten obiekt student, na podstawie klasy Student tworzymy w stepach w BDD
print(student.average_grade())
print(student.name)

student_2 = Student(name='Jacek22', grades_2=(13, 24, 222, 212)) # tutaj wycuiagamy wypełniamy innit 2 zmiennymi

print(student_2.name)
print(student_2.average_grade_2())


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        items_dictionary = {"name": name, "price": price}
        self.items.append(items_dictionary)

        # Create a dictionary with keys name and price, and append that to self.items.

    # sposob gorszy
    # def stock_price(self):
    #     total = 0
    #     for item in store.items:
    #         total += item["price"]
    #     return total
    #
    # # sposob szybszy
    def stock_price(self):
        return sum(item["price"] for item in store.items)

store = Store(name="Zabka")
store.add_item("Maslo", 2)
store.add_item("Ser", 4)
store.add_item("PRzekaski", 8)
print(store.items)
print(store.stock_price())