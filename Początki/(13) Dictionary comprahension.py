#
#
# users = [
#     (0, "Jacek", "password1"),
#     (1, "Placek", "password12"),
#     (2, "Jose", "password13"),
#     (3, "Armando", "password14")
# ]
#
# #zwykły sposób z for
#
# for user in users:
#     if user[1] == "Jacek":
#         print(user)
#
# #sposob z mappingiem pamietaj o dwukropku
#
# username_mapping = {user[1]: user for user in users}
# print(username_mapping["Jacek"])

# przykład zastosowania z inputem
#
# user_input = input("Enter Username: ")
# user_pass = input("Enter Password: ")
#
# _, username, password = username_mapping[user_input]
#
# if user_pass == password:
#     print("logged")
# else:
#     print("incorrect values")


"*************************************************"

STUDENTS = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}


def avarege_grades(student_list):
    grades = student_list['grades']
    return grades

print(avarege_grades(STUDENTS))

STUDENTS = [{'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)},
           {'name': 'Amando', 'school': 'Computing', 'grades': (77, 88, 99)},
           {'name': 'Cezare', 'school': 'Computing', 'grades': (55, 66, 77)}]

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count

print(average_grade_all_students(STUDENTS))
