
#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')

Lines = file1.readlines()
#read the data file line by line

pos = 50
counter = 0

def clock(start:int, move:int, lr:str):
    if lr.lower() == "r":
        result = start + move
        while result > 99:
            result = result - 100
    if lr.lower() == "l":
        result = start - move
        while result < 0:
            result = result + 100
    return result

for line in Lines[0:]:
    lr = line[0]
    move = int(line[1:])
    newpos = clock(pos, move, lr)
    print(f"starting at {pos} then lf: {lr} and move: {move} new postion {newpos}")
    pos = newpos
    if pos == 0:
        counter+= 1

print (f"password: {counter}")


