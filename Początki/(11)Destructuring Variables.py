# python rozumie nawet bez nawiasu jako tuple, rowniez przypisuje wartosci bez nawiasu
x = 3,8
y = [3,8]

a, b = 5, 10
# t = b, c

print(x)
#tak widzi jako podjedyncze wartosci bez tupla
print(a, b)

#python widzi w dictionaries jako tuple
rowery = {'zwykle': 5, 'gorskie': 20, 'elektryczne': 7}
print(list(rowery.items()))

for rower in rowery.items():
    print(rower)

for rower, ilosc in rowery.items():
    print(f"{rower}: {ilosc}")


slodycze_lista_z_tuplami = [("czekolada", 5, "duza"), ("ferrero", 20, "male"), ("czipsy", 7, "srednie")]


for rodzaj,ilosc,wielkosc in slodycze_lista_z_tuplami:
    print(f"Rodzaj {rodzaj}, ilość {ilosc}, wielkosc {wielkosc}")


#pomijanie niektórych variabli z dictionaries

człowiek = ("Jacek", 30, "Przystojny")

imie, rok, wygląd = człowiek

print(imie, wygląd)

#splitowanie listy na 2

head, *tail = [1,2,3,4,5]
print(head)
print(tail)

*head, tail = [1,2,3,4,5]
print(*head)
print(tail)