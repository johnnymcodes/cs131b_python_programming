#!/usr/local/bin/python3

# CS131A final exam: Send in a plain text file that describes how and why
# this program produces the output that it does.
#
# about Counter: https://docs.python.org/3/library/collections.html
# about Urantia: https://en.wikipedia.org/wiki/The_Urantia_Book
#


#
# 0. tools
from re import split
from urllib.request import urlopen as access
from collections import Counter


#
# 1. resources
# terms = set(open('/users/abrick/resources/english').read().split('\n'))
terms = set(open('words.txt').read().split('\n'))


# material is being assigned the value of the url retreiving using urllib.request.urlopen() as access()
# material = access('http://hills.ccsf.edu/~abrick/urantia').read().decode()
material = access('http://data.pr4e.org/romeo.txt').read().decode()
print(material)
parts = Counter(split(r',?[\s.:¼°"-]+',material))

#
# 2. interpretations
#Returns any numbers in the text
def digits(text):
    try:
        return int(text.strip().replace(',',''))
    except ValueError:
        return 0


#returns word with most appearances
def appearance(text):
    #returns the counter value using the word as the argument
    return parts.get(text)

#returns position of word that is not in the dictionary and appears the most or returns 0
def surprise_appearance(text):
    return 0 if digits(text) or text.lower() in terms else parts.get(text)

print(parts)

# 3. analysis
findings = []
for concern in [appearance,len,digits,str,surprise_appearance]:
    print(concern)
    #cycles through words passing each word as a parameter for the list of functions as 'concern'
    print(max(parts,key=concern))
    # casts the value returned by max as a string then adds the word with the highest count
    findings.append(str(max(parts,key=concern)))
    print(findings)
print(' '.join(findings)+'.')

#str returns the word with the highest string value
