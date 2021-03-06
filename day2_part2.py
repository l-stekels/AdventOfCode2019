arr = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

def program(arr, start = 0, end = 4):
    tempCopy = arr[start:end]
    if (tempCopy[0] == 99):
        return arr[0]
    if (tempCopy[0] == 1):
        arr[tempCopy[3]] = arr[tempCopy[1]] + arr[tempCopy[2]]
    if (tempCopy[0] == 2):
        arr[tempCopy[3]] = arr[tempCopy[1]] * arr[tempCopy[2]]
    return program(arr, start + 4, end + 4)

def tests():
    if (program([1,0,0,0,99]) != 2):
        print('fail')
        return
    if (program([2,3,0,3,99]) != 2):
        print('fail')
        return
    if (program([2,4,4,5,99,0]) != 2):
        print('fail')
        return
    if (program([1,1,1,4,99,5,6,0,99]) != 30):
        print('fail')
        return
    print('passed')

tests()
for noun in range(0,100):
    for verb in range(0,100):
        copy = list(arr)
        copy[1] = noun
        copy[2] = verb
        if (program(copy) == 19690720):
            print(100 * noun + verb)

