#dictionaries
#dictionary is like a list, indices can be almost any type

#mapping of indices called keys and a set of values

#example dictionary that maps nglish to spanish words

eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

#order of items in dictionaries in unpredictable
eng2sp = {'one': 'uno', 'two': 'dos'}
print(eng2sp['two'])
len(eng2sp)

# to see if one appears as a key
isin = 'one' in eng2sp
print(isin)

#to see if something appears as a value
vals = list(eng2sp.values())
'uno' in vals
#python uses linear search with in operator for lists


#write  a program that reads the words in words/txt and stores them as keys in a dictionary.
# words = dict()

# fhand = open('r.txt')
# for line in fhand:
#     word = line.split()
#     if len(word) == 0: continue
#     for w in word:
#         words[w] = w
# print(words)
# isin = 'soft' in words
# print(isin)
# isin = 'dog' in words
# print(isin)


#excercise 2
# write  aprogram that categorized each mail message by which day of the week
#the commit was done
import string
fhand = open('Starred.mbox')

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    if words[2] not in counts:
        counts[words[2]] = 1
    else:
        counts[words[2]] += 1
print(counts)

#excercise 3 
''' Write a program to read through a mail log, buil a histogram using dictionary
to pring out how manymessages cae frpm what e,mail address '''


fhand = open('Starred.mbox')

counts = dict()
for line in fhand:
    line = line.rstrip() #rstrip() strips empty space off string
    words = line.split() #split is a list function
    if len(words) == 0 or words[0] != 'From': continue
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1
for count in counts:
    print(count, counts[count])

