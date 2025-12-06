
#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')
lines = file1.readlines()
file1.close()

import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul} # etc.
matrix = []
line_number  = 0
max_columns = 0

for line in lines:
    if len(line) > max_columns:
        max_columns = len(line) # check max column length

for line in lines:
    line = line.replace("\n", "") # remove end of line char
    #line = line.replace("  ", " ")  # remove end of line char
    #matrix.append([])
    #chars = line.split(" ") # split items on space

    line_matrix = [] # matrix is a list in a list
    columns = 0
    for character in line:
        line_matrix.append(character)
        columns += 1
    while columns < max_columns:
        line_matrix.append(" ")
        columns += 1

    line_number += 1

    print(f"line {line_number} has {columns} columns")
    matrix.append(line_matrix)

print(matrix)
print(f"matrix has {columns} columns")

operator_change = False
first_item = True
grandtotal = 0
for i in range(columns):
    col = [row[i] for row in matrix] # create column of data
    if col[-1] in ops.keys(): # if the last row has character like * +
        operator_char = col[-1] #last element is the operator
    col = col[:-1] # remove the last element: the operator, from the column so it is not included in the count

    item = "".join(col) #join each element of the row into 1 word
    if ''.join(set(item)) == " ": # empty column  means new operator
        if not operator_change:
            print(f"grand total: {grandtotal}")
        operator_change = True
        first_item = True
        grandtotal += result

    else: # if not empty column
        intitem = int(item)
        if first_item:
            if operator_char== "*":
                total = 1
            else:
                total = 0
            first_item = False
        result = ops[operator_char](total, intitem)  # prints 2
        print(f"for column {i} : {total} {operator_char} {intitem} = {result}")
        total = result


        # print(f"total for column {i}: {result}")
        if i == 999:
            print ("stop")
print(f"grand total: {grandtotal}")
