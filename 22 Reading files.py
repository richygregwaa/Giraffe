# Documents / Python / employees.txt (can use file and open to open it as a tab in here)

# employee_file = open("/Users/richygregwaa/Documents/00 Python/employees.txt", "w") #r = read  w = write. r+ = read and write
# print(employee_file.readable())   #FALSE as it's been set to write only "w"
# employee_file.close()

employee_file = open("/Users/richygregwaa/Documents/00 Python/employees.txt", "r") #r = read  w = write. r+ = read and write
print(employee_file.readable())  #TRUE
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines())
#print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()