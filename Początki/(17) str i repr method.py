# Możesz mieć tylko jeden z tych 2 str i repr - jakbym probował wydrukować tego obiekt jacek
# bez jednej z tych 2 metod, to mialbym cos takiego <__main__.Student object at 0x7f5dd49ebd90>

# __str__ is used in to show a string representation of your object to be read easily by others.

# __repr__ is used to show a string representation of the object.

class Student:
    def __init__(self, name, grades_2):
        self.name = name
        self.grades2 = grades_2

    def __str__(self):
        return f"Student {self.name} and his grades {self.grades2}"
    # #
    # def __repr__(self):
    #     return f"<Student {self.name} and his grades {self.grades2}>"

jacek = Student(name='Jacek', grades_2=(35, 45, 55))

print(jacek)

