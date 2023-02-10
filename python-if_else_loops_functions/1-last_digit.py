#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
firstStr = 'Last digit of'
isStr = 'is'
if number < 0:
    lastDigit = number % -10
else:
    lastDigit = number % 10

if lastDigit > 5:
    finalStr = 'and is greater than 5'
elif lastDigit == 0:
    finalStr = 'and is 0'
elif lastDigit < 6 and lastDigit != 0:
    finalStr = 'and is less than 6 and not 0'
print(firstStr, number, isStr, lastDigit, finalStr)
