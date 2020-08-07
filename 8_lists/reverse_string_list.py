import sys
# string = sys.argv
if len(sys.argv) > 1: #checks for sys argument
    print('this program prints your string in reverse order')
    #using list methods
    index = len(sys.argv)-1
    reverse = list()# intialize reverse list
    while(index > 0) :
        reverse.append(sys.argv[index]) #fill the list from last index to 0
        index = index - 1
    #use delimiter ,
    delimiter = ', '
    print('\nReversed : ', delimiter.join(reverse))
    print('')
print('\n now using a string method string[::-1]')
string = input('enter a string : ')
print(string[::-1])
