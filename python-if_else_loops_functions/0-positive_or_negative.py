#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    str = 'is negative'
elif number > 0:
    str = 'is postive'
else:
    str = 'is zero'
print(number, str)
