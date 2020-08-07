# Severance Chapter 4 Functions
#4.2 Built-in Functions
# Fundamentals of working with functions
lst = [1, 2, 3, 4, 5, 6, 7]

print(max(lst))
print(min(lst))
length = len(lst)

import random 

for i in range(10):
    x = random.random() * 10
    x = int(x)

print(random.randint(5, 10)) #low, high

randochoice = random.choice(lst)
print('random.choice(lst) = ', randochoice)

#4.5 Math Functions
import math
print(math)
print('model object math has functions')

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
#trig
print(math.sqrt(2) / 2.0)

def computepay():
    pay = 0
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if hours > 40:
        overtime = hours - 40
        overtimepay = overtime *(rate * 1.5)
        pay = 40 * rate + overtimepay
    else :
        pay = hours * rate
    print(pay)

