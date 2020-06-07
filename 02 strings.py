# Following Giraffe Academy on YouTube
# 21/04/2020
# NOTES
# A hash is done by Alt+3

phrase = "Giraffe\nAcademy" # can also use \" if you wanted a quote in your string
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper()) # False
print(phrase.upper().isupper()) #True
print(phrase.lower().islower()) #True

print(len(phrase))
print(phrase[0])  # G
print(phrase.index("Acad"))  #8 (starts at 8)
print(phrase.replace("Giraffe","Elephant"))

