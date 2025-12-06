
#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')
lines = file1.readlines()
file1.close()

import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul} # etc.

matrix = []
line_number  = 0
for line in lines:
    line = line.replace("\n", "") # remove end of line char
    line = line.replace("  ", " ")  # remove end of line char
    #matrix.append([])
    chars = line.split(" ") # split items on space
    line_matrix = [] # matrix is a list in a list
    columns = 0
    for character in chars:
        if character != " " and character != "":
            line_matrix.append(character)
            columns += 1
    line_number += 1
    print(f"line {line_number} has {columns} columns")
    matrix.append(line_matrix)

print(matrix)
print(f"matrix has {columns} columns")

grandtotal = 0
for i in range(columns):
    col = [row[i] for row in matrix]
    operator_char = col[-1]
    col = col[:-1] # remove the last element from the column

    first_item = True
    for item in col:
        intitem = int(item)
        if first_item:
            if operator_char== "*":
                total = 1
            else:
                total = 0
        first_item = False
        result = ops[operator_char](total, intitem)  # prints 2
        # print(f"for column {i} : {total} {operator_char} {intitem} = {result}")
        total = result

    grandtotal += result
    print(f"total for column {i}: {result}")
    if i == 999:
        print ("stop")
print(f"grand total: {grandtotal}")
