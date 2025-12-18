
#file1 = open('datatest.txt', 'r')
file1 = open('data.txt', 'r')

Lines = file1.readlines()
file1.close()

def highNumbers1(joltage:str):
    num1 = num2 = 0
    result =  "11"
    for char in line:
        num = int(char)
        prop1 = f"{num1}{num}"
        prop2 = f"{num2}{num}"
        if int(prop1)>int(result):
            result = prop1
        if int(prop2)>int(result):
            result = prop2
        num1 = result[0]
        num2 = result[1]
    return result

def removeSmallest(numberstring:str):
    x = 9
    for i in numberstring:
        num = int(i)
        if num < x:
            x = num
    small_index = numberstring.find(str(x))
    newstr = numberstring[:small_index] + numberstring[small_index + 1:]
    return newstr

def highNumbers2(joltage:str):
    counter = 0
    #1 we take the last 12 numbers
    #2 then add the number in front
    #3 if #13 the number is smaller #12, then dump it
    #4 else check if number 12, 11, 10 is smaller. the first smallest gets popped

    while len(joltage) > 12:
        joltage_len = len(joltage)
        joltage_12 = joltage[joltage_len-12:]
        joltage_13 = joltage[joltage_len-13]
        if  joltage_13 < joltage_12[0]: #if new character is smaller,then remove that character
            joltage = joltage[0:joltage_len-13] + joltage_12
        else:
            for i in range(1,12):
                char1 = joltage_12[i - 1]
                char2 = joltage_12[i]
                if joltage_12[i-1] < joltage_12[i]: #if number is in joltage is smallest then remove i-1
                    newjoltage = joltage_12[:i-1] + joltage_12[i:] # remove smallest
                    joltage = joltage[0:joltage_len-12] + newjoltage
                    break
                if int(i) == 11:
                    joltage = joltage[0:joltage_len-1]
        counter += 1

    return joltage

total1 = total2 = 0
for line in Lines:
    line = line.replace('\n', '')

    result1 = highNumbers1(line)
    total1 += int(result1)

    result2 = highNumbers2(line)
    total2 += int(result2)

print(f"Answer part 1:  {total1}.")
print(f"Answer part 2:  {total2}.")