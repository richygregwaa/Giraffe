def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def no_match(num1, num2):
    if num1 != num2:
        return "no match"
    else:
        return "match"


def dog_ex():
    if "dog" == "dog":
        return "woof"


print(max_num(3, 4, 5))
print(max_num(3, 40, 5))
print(max_num(3, 40, 555))
print(no_match(3,4))
print(no_match(3,3))
print(dog_ex())
