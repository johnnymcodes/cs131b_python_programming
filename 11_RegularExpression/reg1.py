import re # regular expression library
hand = open('Starred.mbox')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line): #simplest use of regular expression library
        print(line)

#equivalent
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
