slodycze = {'czekolada': 5, 'ferrero': 20, 'czipsy': 7}

#proste wyciagniecie wartosci jednego wpisu
print(slodycze['czipsy'])
print('***************************************************')

#proste dodanie wpisu do dictionary
slodycze['ciasteczka'] = 32

print(slodycze)
print('***************************************************')

#prosta podmiana wartosci w dictionary
slodycze['czekolada'] = 10
print(slodycze)
print('***************************************************')

#wpisy list dictionariów
slodycze = [{'nazwa': 'czekolada', 'rodzaj': 'biała'},
           {'nazwa': 'ferrero', 'rodzaj': 'orzechowe'},
           {'nazwa': 'czipsy', 'rodzaj': 'paprykowe'}]

print(slodycze)
print('***************************************************')

print(slodycze[2])
print('***************************************************')

print(slodycze[2]['rodzaj'])

print('***************************************************')
rowery = {'zwykle': 5, 'gorskie': 20, 'elektryczne': 7}

print(rowery)
print('***************************************************')

for rodzaj in rowery:
    print(rodzaj)
print('***************************************************')

for rodzaj in rowery:
    print(f"{rodzaj}: {rowery[rodzaj]}")
print('***************************************************')

print(rowery.items())
print('***************************************************')

print(rowery.values())
print('***************************************************')

#najlepszy sposób
for rodzaj, ilosc in rowery.items():
    print(f"{rodzaj}: {ilosc}")
print('***************************************************')

#wyciaganie samym values
ilosc_rowerow = rowery.values()
print(sum(ilosc_rowerow))
print(sum(ilosc_rowerow)/len(ilosc_rowerow))

