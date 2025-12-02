import math
#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')

Lines = file1.readlines()
file1.close()

line = Lines[0]
lijst = line.split(",")

def is_valid1(test_str:str):
    length = int(len(test_str))
    if length % 2 == 0: # try to split the string in 2 equal parts
        middle = int(length/2)
        item1 = test_str[0:middle]
        item2 = test_str[middle:]
        if item1 == item2:
            return False
    return True

def is_valid2(test_str:str):
    length = len(test_str) #length of the ID

    valid = True
    root = int(round(length/2,0))+1 # half of the length to be used as the max for in how many ways it can be split

    for i in range(1, root): #first we split in characters of length 1, then length 2 .. up to length root
        lijst = []
        if length % i == 0: # does i fit exactly i times in length? if so, then continue

            for j in range(0,length, i): #split up the ID in equal parts of i letters
                endchar = j + i
                lijst.append(test_str[j:endchar])
            if len(set(lijst)) == 1: # if all the elements of the list are identical, then it is an invalid ID
                return False
    return True


counter1 = 0
counter2 = 0
for item in lijst:
    #print(f"item: {item}")
    startend =item.split("-")
    start = int(startend [0])
    end = int(startend [1])
    for i in range(start, end+1):
        #if i == 2121212121:
        #    print("hello")
        result = is_valid1(str(i))
        if result == False:
            print(f"- {item}: has invalid ID, {i}")
            counter1 +=  int(i)
        result = is_valid2(str(i))
        if result == False:
            print(f"- {item}: has invalid ID, {i}")
            counter2 +=  int(i)

print(f"exercise 1: Adding up all the invalid IDs in this example produces {counter1}.")
print(f"exercise 2: Adding up all the invalid IDs in this example produces {counter2}.")