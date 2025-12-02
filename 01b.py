from email.charset import add_codec

file1 = open('data.txt', 'r')
#file1 = open('datatest.txt', 'r')
Lines = file1.readlines()
#read the data file line by line

prev_pos = 50
counter = 0

print(f"- The dial starts by pointing at {prev_pos}.")

for line in Lines[0:]:
    lr = line[0]
    move = int(line[1:])
    step = move
    pos = prev_pos

    if lr.lower() == "r":
        add = 1
    if lr.lower() == "l":
        add = -1

    rotations = 0
    while step >= 1:
        step -= 1
        pos += add
        if pos == 100:
            pos = 0
        if pos == 0:
            counter += 1
            rotations += 1
        if pos == -1:
            pos = 99

    if rotations == 0 :
        print(f"- The dial is rotated {lr}{move} to point at {pos}")
    else:
        print(f"- The dial is rotated {lr}{move} to point at {pos}, during this rotation it points at 0 {rotations} time")

    prev_pos = pos

print (f"password: {counter}")


