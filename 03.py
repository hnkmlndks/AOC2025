from aifc import Aifc_write

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
    max_attempts = len(joltage)-12
    while len(joltage) > 12 and counter < max_attempts:
        joltage_len = len(joltage)
        for i in range(joltage_len-1):
            char1 = joltage[i]
            char2 = joltage[i + 1]
            if len(joltage.replace("0","")) >12:
                joltage_len = len(joltage.replace("0",""))
                if joltage[i] < joltage[i+1]:
                    newjoltage = joltage[:i] + "0" + joltage[i + 1:]
                    joltage = newjoltage
        result = joltage.replace("0","")
        counter += 1
        joltage  = result
    while len(result) >12:
        result = result[:len(result)-1]
    return result

total = 0
for line in Lines:
    line = line.replace('\n', '')
    result = highNumbers2(line)
    total += int(result)

    print(f"Input {line} with result: {result} to the total output joltage becomes :  {total}.")
