#8	Extend last week's program so that it also reports the number
# of times each argument occurred.
counts= dict()

print('this program prints out the number of times an argument occurs')
string = input('enter argument s:')
splitstring = string.split() #creating a list using stirng method split()

for word in splitstring: # for argument in lists
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print("these are the counts of occurances of each argument")

for key in counts:
    print(key, counts[key])
