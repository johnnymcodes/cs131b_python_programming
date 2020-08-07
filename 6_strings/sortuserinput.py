#intro to python
#sort user input
#write a program that prints out the unique command line arguments
#it receives, in alphabetical order

import sys
cmdarg = sys.argv[1:]
cmdarg.sort()
delimiter = ' '
if len(cmdarg) > 1:
    joinstring = delimiter.join(sys.argv[1:])
    print('this is your command argument ', joinstring)
    joinstring = delimiter.join(cmdarg)
    print('this is your command argument sorted ! ', joinstring, '\n')

print('this program prints your string in alphabetical order')
string = input('enter a string :')
splitstring = string.split() #creating a list using stirng method split()
print('this is your split string ', splitstring)

joinstring = delimiter.join(splitstring)
print('this is your split string list joined back ', joinstring)
splitstring.sort() #no return value for sorted, modifies data

joinstring = delimiter.join(splitstring)
print('this is your sorted string ! ', joinstring)
