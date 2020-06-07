lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Oscar", "Toby"]
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
# friends.clear()
friends.pop()  # removes last item in list
print(friends)
print(friends.index("Oscar"))
print(friends.count("Oscar"))

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Oscar", "Toby"]
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)