numbers = [1,2,5]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Jacek", "Jarek", "Janita", "Marek", "Konrad"]
starts_with_j = [name for name in friends if name.startswith("J")]
print(starts_with_j)

#Uwaga! mimo, że 2 listy bedą miały te same wartości
#to nie są te same listy - sa gdzie indziej przechowywane w pamieci
# mają inne id
friends = ["Jacek", "Jarek", "Janita"]
starts_with_j = [name for name in friends if name.startswith("J")]

print("friends id: ", id(friends), "starts_with_j", id(starts_with_j))

# inny przyklad list comprahension


def long_words_1(lst):
    words = []
    for word in lst:
        if len(word) > 5:
           words.append(word)
    return words


print(long_words_1(['blog', 'Treehouse', 'Python', 'hi']))


def long_words_2(lst):
    return [word * 2 for word in lst if len(word) > 5]

print(long_words_2(['blog ', 'Treehouse ', 'Python ', 'hi ']))
