
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])
print(number_grid[1][0])
print(number_grid[2][1])

print("\nFor loop")
for row in number_grid:
    print(row)

print("\n2nd For loop")
for row in number_grid:
    for col in row:
        print(col)

