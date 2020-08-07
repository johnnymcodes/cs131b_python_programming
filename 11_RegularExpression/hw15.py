#Finds the largest word in the dictionary that is spelled using only letters A - F
import re #regex library
import time
#dictionary = input('Enter location of dictionary :  ')
hand = open('/users/abrick/resources/english')
longest = ''
for line in hand:
    line = line.rstrip()
    if re.search('^[a-fA-F]*$', line):
        print(line)
        if len(line) > len(longest):
            longest = line
print('Longest word with only the letters A - F is ...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print(longest)
