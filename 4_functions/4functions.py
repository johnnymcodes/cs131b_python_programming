type(32)

#built in functions

max("Hello ooaoafo")
min("Yow yo where my dogs at ")

len(" helaoo asdow")

#typ function converstion
int('232')
int(3.145689)
str(123)

#random numbes
import random

for i in range(10):
    x = random.random()
    print("this is a random number : ", x)

randoint = random.randint(5, 10) # returns an integer between (low, high)
print(randoint)

#choose an element form a sequence
t = ['one', 'two', 'three']
randochoice = random.choice(t)
print("this is a random choice ", randochoice)

# adding new functions
def print_lyrics():
    print("loddy doddy we like to party")
    print("we dont start shit we don't bother nobody")
