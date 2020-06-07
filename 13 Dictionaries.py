monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

monthConversions2 = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print("\nFrom first dictionary")
print(monthConversions["Nov"])
print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv","Not a valid key"))
print(monthConversions.get("Jan","Not a valid key"))

print("\nFrom second dictionary")
print(monthConversions2[11])
print(monthConversions2[3])
print(monthConversions2.get(12))
print(monthConversions2.get(13,"Not a valid key"))
print(monthConversions2.get(1,"Not a valid key"))
