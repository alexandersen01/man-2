import random
from sudoku import Sudoku

def easypuzzles():
    res = []
    res2 = []
    res3 = []
    res4 = []
    counter = 0

    with open('Dataset.txt') as f:
        lines = f.readlines()
        lines = lines[:1000]

    #remove \n from each line
    lines = [line.strip() for line in lines]

    # convert every element in lines to a 9x9 matrix
    for line in lines:
        res.append([line[i:i+9] for i in range(0, len(line), 9)])

    # convert every element in res to a 9x9 matrix of integers
    for line in res:
        res2.append([[int(i) for i in line[j]] for j in range(0, len(line))])


    # convert every element in res2 to a Sudoku object
    for line in res2:
        res3.append(Sudoku(3, 3, board =line).solve().board)
        counter += 1
        print(f'solutions added: {counter}')

    # join all elements in res3 to a single list with length 81 per element
    res3 = [item for sublist in res3 for item in sublist]
    res3 = [item for sublist in res3 for item in sublist]


    # join all elements in res3
    res3 = ''.join(str(e) for e in res3)

    # add a new line every 81 characters
    res3 = [res3[i:i+81] for i in range(0, len(res3), 81)]

    for i in range(len(res3)):
        for j in range(35):
            index = random.randint(0, len(res3[i])-1)
            res3[i] = res3[i][:index] + '0' + res3[i][index+1:]

    #write each element in res3 to a new line in a new file
    with open('Easy.txt', 'w') as f:
        for item in res3:
            f.write(item + '\n')

    return res3

def mediumpuzzles():

    res = []
    res2 = []
    res3 = []
    res4 = []
    counter = 0

    with open('Dataset.txt') as f:
        lines = f.readlines()
        lines = lines[1001:2000]
        

    #remove \n from each line
    lines = [line.strip() for line in lines]

    # convert every element in lines to a 9x9 matrix
    for line in lines:
        res.append([line[i:i+9] for i in range(0, len(line), 9)])

    # convert every element in res to a 9x9 matrix of integers
    for line in res:
        res2.append([[int(i) for i in line[j]] for j in range(0, len(line))])


    # convert every element in res2 to a Sudoku object
    for line in res2:
        res3.append(Sudoku(3, 3, board =line).solve().board)
        counter += 1
        print(f'solutions added: {counter}')

    # join all elements in res3 to a single list with length 81 per element
    res3 = [item for sublist in res3 for item in sublist]
    res3 = [item for sublist in res3 for item in sublist]


    # join all elements in res3
    res3 = ''.join(str(e) for e in res3)

    # add a new line every 81 characters
    res3 = [res3[i:i+81] for i in range(0, len(res3), 81)]

    for i in range(len(res3)):
        for j in range(27):
            index = random.randint(0, len(res3[i])-1)
            res3[i] = res3[i][:index] + '0' + res3[i][index+1:]

    #write each element in res3 to a new line in a new file
    with open('Medium.txt', 'w') as f:
        for item in res3:
            f.write(item + '\n')

    return res3

def Hardpuzzles():
    res = []
    res2 = []
    res3 = []
    res4 = []
    counter = 0

    with open('Dataset.txt') as f:
        lines = f.readlines()
        lines = lines[2001:3000]

    #remove \n from each line
    lines = [line.strip() for line in lines]

    # convert every element in lines to a 9x9 matrix
    for line in lines:
        res.append([line[i:i+9] for i in range(0, len(line), 9)])

    # convert every element in res to a 9x9 matrix of integers
    for line in res:
        res2.append([[int(i) for i in line[j]] for j in range(0, len(line))])


    # convert every element in res2 to a Sudoku object
    for line in res2:
        res3.append(Sudoku(3, 3, board =line).solve().board)
        counter += 1
        print(f'solutions added: {counter}')

    # join all elements in res3 to a single list with length 81 per element
    res3 = [item for sublist in res3 for item in sublist]
    res3 = [item for sublist in res3 for item in sublist]


    # join all elements in res3
    res3 = ''.join(str(e) for e in res3)

    # add a new line every 81 characters
    res3 = [res3[i:i+81] for i in range(0, len(res3), 81)]

    for i in range(len(res3)):
        for j in range(20):
            index = random.randint(0, len(res3[i])-1)
            res3[i] = res3[i][:index] + '0' + res3[i][index+1:]

    #write each element in res3 to a new line in a new file
    with open('Hard.txt', 'w') as f:
        for item in res3:
            f.write(item + '\n')

    return res3


print(easypuzzles())
print(mediumpuzzles())
print(Hardpuzzles())
