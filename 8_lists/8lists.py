# # #petss
# #
# # pets = ['dog', 'cat', 'fish']
# # favpet= input('whats your fave pet')
# # if favpet in pets:
# #     print(favpet + 'is in pets !')
# # else:
# #     print('no dice')
# #
# # #8.3 Traversing a petss
# # for pet in pets:
# #     print(pet)
# #
# #     #use indices for updating elements
# # numbers = [1, 2, 3, 4, 5, 6]
# # print(numbers)
# # for i in range(len(numbers)):
# #     numbers[i] = numbers[i] * 2
# # print(numbers)
# #
# # petsandnums = pets + numbers
# # print(petsandnums)
# #
# # operandlist = [0] * 4
# # print('this is a list created with a operator')
# # print(operandlist)
# # def slicelist(alist):
# #     print('time to slice this hsit')
# #     slist = alist[1:2]
# #     print(slist)
# # slicelist(operandlist)
# #
# # #append
# # print('append the pets list')
# # newpet = input('whats ypur favorite pet ? ')
# # pets.append(newpet)
# #
# # morepets = ['iguana', 'spider', 'monkey']
# # pets.extend(morepets)
# # print(pets)
# #
# # print('sorting our pets list')
# # pets.sort()
# # print(pets)
# # print('deleting elemts')
# # pets.pop(1)
# # #where 1 is the index
# # print(pets)
# #
# # #pop modifies and returns element removed
# # #delets and returns last elements
# # print(pets.pop())
# # print(pets)
# #
# # #if your know the element use removed
# # remove = input('enter pet to remove : ')
# # if remove in pets:
# #     pets.remove(remove)
# # else:
# #     print('pet not in llist ')
# # print(pets)
# #
# # # to remove more than one lement use del
# # del numbers[1:3]
# # print('deleted numbers')
# # print(numbers)
# #
# #split splits a string into wors
# string = input('enter a string to split ')
# splitstring = string.split()
# print(splitstring)
# s = 'hel-el-eh'
# delimiter = '-'
# delimiter.split(s)
# print(delimiter)
# print(s)
# #
# # joined = delimeter.join(s)
# # print(joined)
# #
# choppedlist = [1, 2, 3, 4]
# print(choppedlist)
# def chop(alist):
#     alist.pop(0) #removed first elements4
#     alist.pop() #deletes and returns last elements
#
# chop(choppedlist)
# print(choppedlist)
#
# #takes a list and returns a new list that contains all but the first and last elements
# middlelist = [1, 2 ,3, 4, 5]
# print(middlelist)
# def middle(alist):
#     newList = alist[1:len(alist) - 1]
#     return newList
#
# newList = middle(middlelist)
# print(newList)
#
# #
#
fhand = open('romeo.txt')
count = 0
words = list()
for line in fhand:
    splitline = line.split()
    for word in splitline:
        if words.count(word) == 0 :
            words.append(word)

delimiter = ' '
joinwords = delimiter.join(words)
print(joinwords)
words.sort()

joinwords = delimiter.join(words)
print(joinwords)


# #excercise 5: write a proram to read throgh the mail bpx data
# #find line that starts with 'from', split lines using splut
# #extract who send the message
#
# fhand = open('Starred.mbox')
# counter = 0
# for line in fhand:
#     words = line.split()
#     #print('Debug: ', words)
#     if len(words) == 0 or words[0] != 'From'  : continue
#     print(words[1])
#     counter = counter + 1
# print(counter, ' number of lines that start with from ')
#
# #ex 6 write a program that prompts the user for a list of numbers and prints out the max and min of the OcSNxm9_FvPcUZIdHmAUXhcLAqwh6sBAaZPS9FEVuTi2BbnZUS7KFR1lCTczR2dc7AsZVfu98IP# at the end when the user enters "done"

numlist = list()
while(True):
    inp = input('Enter a number : ')
    if inp == 'done': break
    try:
        value = int(inp)
        numlist.append(value)
    except ValueError:
        print('Please enter a number ')
maxnum = max(numlist)
minnum = min(numlist)
print (' Max is : ', maxnum)
print(' Min is : ', minnum)
