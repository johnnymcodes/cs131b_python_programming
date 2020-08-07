# reverse string

string = input("Enter a string : " )

i = len(string) - 1
while i > 0:
    char = string[i]
    i = i - 1
    print(char)

#prints a string with for
for char in string:
    print(char)

# string slices
print(string[0:5])
print(string[5:])# no need for len(string)


#python offers char comparison
count = 0
for letter in string:
    if letter == 'a':
      count = count + 1
print(count)

# Excercise 3: Encapsulte this code in a function named count, and generalize it so that it accepts the string and the letter as arguments

def count(target, string):
    count = 0
    for letter in string:
        if letter == target:
            count = count + 1
    return(count)
print(count('l', string))

#show an objects available methods with dir(obj)

string.strip() # removed white spaces before and afte
string.lower() # lowercase for all
if(string.startswith('h')): # returns true or false
    print("string starts with h ! ")

countchar = input("enter a letter to look for : ")
print('there are', string.count(countchar), " occurances of ", countchar)


#string parsing find domain host
data = 'stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
def findhost(data):
    atpos=data.find('@')
    spacepos=data.find(' d
    host = data[apost+1:spacepos]
    print(host)

#ex5  use find and string slicing to extract
string2 = 'X-DSPAM-Confidence:0.8475'
def ex5(string):
    colpos = string.find(':')
    num = string[colpos+1:]
    float(num)
    print(num)
    # string = ' confideince numbe is %g' % num
    # print(string)

ex5(string2)
