list = ["Bob", "Rolf", "Annie"]
#keep in order, can add and remove vars

tuple = ("Bob", "Rolf", "Annie")
#keeps in order, cannot add or remove vars

sets = {"Bob", "Rolf", "Annie"}
#order is no guaranteed, no duplicate elements possible

print(list[0])
print(tuple[0])
#cannot do it with sets

list[0] = "Dupa"
print(list)
#cannot do this changing with either tuples or sets


list.append("Smith")
print(list)
#add to list with append

sets.add("Smith")
print(sets)

sets.add("Smith")
print(sets)
# add to sets with add - no duplicates possible

list.remove("Rolf")
print(list)

sets.remove("Smith")
print(sets)

#not possible in tuples

"*******************************SETS"

friends = {"Bob", "Rolf", "Annie"}
abroad = {"Bob", "Annie"}

local_friends = friends.difference(abroad)
print(local_friends)
#wskaze roznice miedzyu friends a aborad

local_friends = abroad.difference(friends)
print(local_friends)
#odda pusty set, bo usunie Boba i Annie a w abroad nie ma Rolfa


total_friends = friends.union(abroad)
print(total_friends)
#połączy sety, ale nie duplikuje tych samych

art = {"Bob", "Rolf", "Annie"}
science = {"Bob", "Annie", "Margaret"}

attends_both = art.intersection(science)
print(attends_both)
#shows the same vars in both sets

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}

set2.add(9)
set2.add(12)
set2.add(77)
print(set2)
result = set1.intersection(set2)
print(result)