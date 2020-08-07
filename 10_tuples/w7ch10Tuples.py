# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:

#    t.append((len(word), word)) #builes a list of tuples, where each tuple is a word preceded by its length

# t.sort(reverse=True) # tells sort to go in decreasing order
# print(t)
# res = list()
# for length, word in t:
#    res.append(word) # tracerses the list of tuples and builds a list of words in descending order
# print(res)
# 
# d = dict()
# d = {'a':10, 'b':1, 'c':22}
# t = list(d.items())
# t.sort()
# print(t)
# #two itertation variables key, val because items retirns a list of tupes and key, va is a tuple assignment
# for key, val in list(d.items()):
#    print(val, key)

# l = list()
# for key, val in d.items() :
#    l.append((val, key))
# print(l)
# l.sort(reverse=True)
# print(l)

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
   line = line.translate(str.maketrans('', '', string.punctuation))
   line = line.lower()
   words = line.split()

   for word in words:
      letters = tuple(word)
      for letter in letters:
         if letter not in counts:
            counts[letter] = 1
         else:
            counts[letter] += 1

lst = list()
for key, val in list(counts.items()):
   lst.append((val, key))
lst.sort(reverse=1)

for key, val in lst[:10]:
   print(key, val)

# last= 'martinez'
# first = 'johnny'
# number = '718-918-4354'
# directory = dict()
# directory[last, first] = number
# directory['weaver', 'erin'] = '707-774-2220'

# for last, first in directory:
#    print(first, last, directory[last, first])


# fhand = open('Starred.mbox')
# counts = dict()
# for line in fhand:
#    line = line.rstrip() #eliminates right white space 
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    if words[1] not in counts:
#       counts[words[1]] = 1
#    else:
#       counts[words[1]] += 1

# lst = list()
# for email, count in list(counts.items()):
#    lst.append((email, count))
# lst.sort(reverse=True)

# for email, count in lst:
#    print(email, count)

