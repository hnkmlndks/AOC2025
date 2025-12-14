#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')

lines = file1.readlines()
file1.close()

def check_char(matrix, x, y, xmax, ymax):
    if 0 <= x <= xmax and 0 <= y <= ymax and matrix[y][x] == "@":
        return True
    return False

def countRolls(matrix, xpos, ypos, xmax, ymax):
    count = 0
    #pos1
    x = xpos -1
    y = ypos -1
    if check_char(matrix,x,y,xmax,ymax):
        count +=1
    #pos 2
    x = xpos
    y = ypos -1
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    #pos 3
    x = xpos +1
    y = ypos -1
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    #pos 4
    x = xpos -1
    y = ypos
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    #pos 5
    x = xpos +1
    y = ypos
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    #pos 6
    x = xpos -1
    y = ypos +1
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    # pos 7
    x = xpos
    y = ypos +1
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    # pos 8
    x = xpos + 1
    y = ypos +1
    if check_char(matrix, x, y, xmax, ymax):
        count +=1
    return count

def set_character(matrix, x, y):
    row = matrix[y]
    matrix[y] = row[:x] + "x" +  row[x+1:]
    return matrix

matrix = []
matrix_copy = []
x = y = maxx = maxy = 0
# populate dictionary with data

# read the data file line by line
counter = 1
for line in lines:
    line = line.strip()
    matrix.append(line)
    matrix_copy.append(line)
    if len(line) > maxx:
        maxx = len(line)
    maxy += 1
maxx -= 1
maxy -= 1
counter = 1
grand_total = 0
while counter > 0:
    counter = 0
    for i in range(maxx+1):
        for j in range(maxy+1):
            if matrix[j][i] == "@":
                result = countRolls(matrix, i, j, maxx, maxy)
                #print(f"position {i} {j}: number of rolls  {result}")
                if result < 4:
                    counter += 1
                    matrix_copy = set_character(matrix_copy, i, j)
    for line in matrix_copy:
        print(line)

    grand_total += counter
    print(f"can move {counter} roles of paper, grand total: {grand_total}")
    matrix = matrix_copy






