# Exercise 3: Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctua
# tion, or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.

import string
#reads a file
fhand = open('romeo-full.txt')
counts = dict() #dictionary to hold frequency
for line in fhand:
   #doesn't count spaces, digits, punctuation or anything other than a-z
   line = line.translate(str.maketrans('', '', string.punctuation))
   # Converts all the input to lower case
   line = line.lower()
   words = line.split()
   for word in words:
      letters = tuple(word) #returns word as a list of letters eg ['a', 'b', 'c']
      for letter in letters:
         if letter not in counts:
            counts[letter] = 1
         else:
            counts[letter] += 1 # doy had it =+ and everything was equal to 1
lst = list()
for letter, count in list(counts.items()): # .items() returns a list of tupeles and key value pairs
   lst.append((count, letter))
#in decreasing order of frequency.
lst.sort(reverse=True)
#prints the letters 
for letter, count in lst[:10]:
   print(letter, count)