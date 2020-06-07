# Tuples - store values like list but can't modify. Use brackets instead of [] like you use for lists

coordinates = (4,5)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

#this would give error - TypeError: 'tuple' object does not support item assignment
# coordinates[1] = 10

# You can create a List of Tuples so that additional Tuples could be added or removed to that List
coordinates2 = [(4,5),(6,7),(80,34)]
print(coordinates2)
coordinates2.append("Creed")
print(coordinates2)
coordinates2.remove((6,7))
print(coordinates2)
