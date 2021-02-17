# movie_characters = {'kapitan bomba', 'kapitan torpeda', 'chorąży Głuś'}
# user_char= input('Enter your best movie character: ').lower()
#
# if user_char in movie_characters:
#     print(f'Wiadomo, że {user_char} tempy chuju')
# else:
#     print('Ale walaszka to szanuj')
#

"************************"

magic_number = 7
user_input = input("Enter 'y' if you want to try your luck: ").lower()
if user_input == "y":
    user_number = int(input("Please guess my number: "))
    how_far_away = int(abs(magic_number - user_number))
    if user_number == magic_number:
        print(" Zgadłeś elegancko")
    elif abs(magic_number - user_number) != magic_number:
        #abs czyli wartości absolutne pokazujące odległość od danej liczby
        print(f'You were off by {how_far_away}')
    elif user_number == 0:
        print("no its not 0")

