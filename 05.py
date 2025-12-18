from collections import deque
#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')

lines = file1.readlines()
file1.close()

def check_sample(mylines, number:int):
    result = False
    for line in mylines:
        if line.find("-")>0:
            startstr, endstr = line.split("-")
            if int(startstr) <= number <= int(endstr):
                result = True
    return result

def compare_items(item1, item2):
# simple case char 1a and char 1b are both smaller or both  bigger than char 2a and char 2b
    a1, b1 = item1
    a2, b2 = item2
    # no overlap
    if b1 < a2 or a1 > b2:
        return True, 0, 0

    # overlap cases
    if a1 <= a2 and b1 >= b2:
        c1, c2 = a1, b1
    elif a1 <= a2 and b1 <= b2:
        c1, c2 = a1, b2
    elif a1 >= a2 and b1 <= b2:
        c1, c2 = a2, b2
    else:  # a1 >= a2 and b1 >= b2
        c1, c2 = a2, b1

    return False, c1, c2

def part_1(lines):
    counter = 0
    for line in lines:
        line = line.strip()
        if (line.find("-")<0) and len(line)>0: # if it does not contain "-" and has at least 1 character
            ingredient = int(line)
            if check_sample(lines,ingredient):
                # print(f"Ingredient {ingredient} is fresh")
                counter += 1
    print(f"answer for part 1: {counter}")

def part_2(mylines):
    dq = deque()

    # build deque of (start, end) tuples
    for line in mylines:
        if line.find("-") > 0:
            startstr, endstr = line.split("-")
            interval = (int(startstr), int(endstr))
            dq.append(interval)

    # do the merging 3 times
    for i in range(3):
        count1 = 0
        count2 = 1
        while (count1 < len(dq)-1) or (count2 < len(dq)):
            item1 = dq[count1]
            item2 = dq[count2]
            no_changes, a, b  = compare_items(item1, item2)
            if no_changes:
                count2 += 1
            else:
                dq[count2] = (a,b)
                del dq[count1] # remove item 1
                if count2 > count1 +1:
                    count2 -= 1 # need to count 1 backwards after removing item
            if count2 == len(dq):
                count1 += 1
                count2 = count1 + 1
            #print(f" count1 {count1} and count2 {count2} and item1 {item1} and item2 {item2}")
    counter = 0
    for start, end in dq:
        counter += (end - start + 1)
    print (f"answer for part 2: {counter}")
part_1(lines)
part_2(lines)


# complex: all other cases remove both sets and new set 3:
# if char1a =< char2a and char1b >= char2b   #   char3a = char1a and char3b = char1b
# if char1a =< char2a and char1b =< char2b   #   char3a = char1a and char3b = char2b
# if char1a => char2a and char1b =< char2b   #   char3a = char2a and char3b = char2b
# if char1a => char2a and char1b => char2b   #   char3a = char2a and char3b = char1b

# read set1 and compare with all other sets, so you have set a and b
# if replacement needed, then pop seta and replace set b