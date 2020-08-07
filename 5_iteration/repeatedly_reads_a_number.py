#chapter 5 Iteration
#5.1 Updating variables

# take input from the user until they type done
# while True:
#    line = input('> ')
#    if line == 'done':
#        break
#    print(line)
# print('END')


#ex1

#repeatedly reads numbers until the user enters 'done'
lst = list()
while True:
   number = input('Enter a number : ')
   if(number == 'done') : break
   try:
      number = float(number)
      lst.append(number)
      print(lst)
   except:
      print('Numbers only ! ')

count = 0
total = 0
for intervar in lst:
   count = count + 1
   total = total + intervar
average = total / count

print('count : ', count, ' | total : ', total, ' | average : ', average 
   )
# ex 2
print('min = ', min(lst))
print('max = ', max(lst))