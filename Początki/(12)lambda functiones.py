#


def add(x, y):
    return x + y


print(add(5, 7))

add = (lambda x, y: x+ y)

print(f"z funkcja lambda: {add(5, 7)}")

print('*******************************************')


def double(x):
    return x * 2


sequence = (1, 2, 3, 4, 5)

print('pierwsza mozliwosc z rownaniem w srodku')
doubled = [x * 2 for x in sequence]
print(doubled)

print('druga mozliwosc z zdefiniowana funkcja w srodku')

doubled = [double(x) for x in sequence]
print(doubled)

print(' uzycie funkcji map która skraca - uwaga na nawiasy - z innymi wypierdala ')
doubled = map(double, sequence)
print(list(doubled))

print('trzecia mozliwosc z uzyciem lambda')

doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)


print('czwarta mozliwosc z uzyciem lambda i map - musi byc jako lista')

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
