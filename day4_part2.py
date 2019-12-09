import re
rangeStart = 136760
rangeEnd = 595730


def getDigits(number):
    return [int(x) for x in str(number)]


def sameAdjecent(number):
    digits = getDigits(number)
    prev = 0
    for digit in digits:
        occurences = digits.count(digit)
        if occurences == 2:
            return True
    return False


def growing(number):
    digits = getDigits(number)
    for i, j in enumerate(digits[:-1]):
        if j > digits[i+1]:
            return False
    return True

result = []
for number in range(rangeStart, rangeEnd):
    if sameAdjecent(number) and growing(number):
        result.append(number)

print(len(result))
