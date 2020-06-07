
# Create new file 'employees.txt'
employee_file = open("/Users/richygregwaa/Documents/00 Python/employees.txt", "w") #a = append  w = write(overwrite). r+ = read and write
print(employee_file.write("\nToby - Human Resources"))
employee_file.close()


#Append to existing file
employee_file = open("/Users/richygregwaa/Documents/00 Python/employees.txt", "a") #a = append  w = write(overwrite). r+ = read and write
print(employee_file.write("\nRichy - IT"))
employee_file.close()

# Can create different types of file such as html
employee_file = open("/Users/richygregwaa/Documents/00 Python/index.html", "w") #a = append  w = write. r+ = read and write
print(employee_file.write("<p>This is HTML</p>"))
employee_file.close()

