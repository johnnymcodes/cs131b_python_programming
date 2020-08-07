# Write a program that expects numeric command line arguments and calls 
# functions to print descriptive statistics such as the mean, median, 
# mode, and midpoint. 
# Week 9 : Severance 4

import sys #expects numeric command line arguments 
cmarg  = sys.argv[1:] #returns a list of cmd arguments
def isint(lst):
   for string in lst:
      try:
         int(string)
         return True
      except valueError:
         return False
         break

for arg in cmarg:
   if not isint(cmarg):
      sys.exit('All arguments must be integers. Exit')

numbers = [int(arg) for arg in sys.argv[1:]]

print(numbers)

def mode(numbers):
   mode = 0
   counts = dict()
   for number in numbers:
      if number not in counts:
         counts[number] = 1
      else:
         counts[number] += 1
   lst = list()
   for number, count in list(counts.items()):
      lst.append((count, number))
   lst.sort(reverse=1)

   for count, number in lst[:1]:
      mode = number;
   
   print(mode, " is the mode appearing ", count, " times")
   return mode;

def median(numbers):
   numbers.sort()
   middle = int(len(numbers)/2)
   median = numbers[middle]   
   print('The median is : ', median)
   return median

def midpoint(numbers):
   maxnum = max(numbers)
   minnum = min(numbers)
   midpoint = (maxnum-minnum)/2
   print('The midpoint is : ', midpoint)

def mean(numbers):
   sumnum = sum(numbers)
   mean = sumnum/len(numbers)
   print('The mean is : ', mean)


mode(numbers)
median(numbers)
midpoint(numbers)
mean(numbers)