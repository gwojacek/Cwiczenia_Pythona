name = 'Bob'

greeting = f'Hello, {name}'

print(greeting)

name = 'Robler'

greeting = f'Hello, {name}'

print(greeting)


"*****************************************"

name = 'Bob'

greeting = 'Hello, {}'
with_name = greeting.format(name)
with_name_two = greeting.format('Rolf')

print(with_name)
print(with_name_two)

"*****************************************"

longer_phraze = 'Hello, {}. Today is {}.'

formatted = longer_phraze.format('Rolf', 'Monday')
print(formatted)