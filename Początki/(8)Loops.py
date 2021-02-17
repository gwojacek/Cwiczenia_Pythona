

magic_number = 7
#WHILE**********************************
while True:
    user_input = input("Do you want to play? (y/n) ").lower()
    if user_input == "n":
        print("End of a game with n")
        break
    user_number = int(input("Please guess my number: "))
    how_far_away = int(abs(magic_number - user_number))
    if user_number == magic_number:
        print(" Zgadłeś elegancko - koniec gry")
        break
    elif abs(magic_number - user_number) != magic_number:
        #abs czyli wartości absolutne pokazujące odległość od danej liczby
        print(f'You were off by {how_far_away}')

#FOR **********************************
friends = ['Anna', 'Kuba', 'Myszka']

for friend in friends:
    print(f'{friend} is my friend')

for friend in range(3):
    print(f'{friend} is my friend')


numbers = [1,2,3,4,5]
total = 0
amount = len(numbers)

for number in numbers:
    total += number

print(total)
print(total/amount)

total = sum(numbers)
print(total)
