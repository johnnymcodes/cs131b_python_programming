

string = input('enter a string ')
print(string)
print(type(string))
backwardsString = ''
def print_backwards(string):
    n = len(string)-1
    while n > -1:
      backwardsString += string[i]
      n = n-1
    print(backwardsString)

print_backwards(string)
