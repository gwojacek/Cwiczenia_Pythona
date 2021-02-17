#*args daje nam mozliwosc wpakowania tak wielu variabli jako tuple
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 2, 3))

#rozbija to też listy, ilosc argumentow w funckji musi sie zgadzac z iloscia w listach
def add(x, y):
    return x + y

nums = (3,5)

print(add(*nums))

#jako dictionary - jezeli nazwy w dictionary są zbieżne z nazwami argumentów funkcji, to można skorzystać z tego myczka
nums = {'x': 3, 'y': 5}
print(add(**nums))

# w tym przyadku nie zadziala bo sa rozne nazwy
# nums = {'a': 3, 'b': 5}
# print(add(**nums))
#
def calculator(*args, opertator):
    if opertator == "+":
        return sum(*args)
    elif opertator == "*":
        # musi być gwiazdka(asterisk) bo wyciagamy dany z tupla z ponizszego printu
        return multiply(*args)
    else:
        print('no valid operator')


print(calculator(1,2,3,4, opertator='*'))
