# Write a program that expects numeric command line arguments and calls 
# functions to print descriptive statistics such as the mean, median, 
# mode, and midpoint. 
# Week 9 : Severance 4

import sys #expects numeric command line arguments 
cmarg  = sys.argv[1:] #returns a list of cmd arguments
numlist = list()
for arg in cmarg:
   try:
      number = float(arg)
      numlist.append(number)
   # except:
   #    continue
   except Exception as err: 
      print(arg, ' is not a number')
      print(err)
      print()
print(numlist)

def mode(numlist):
   mode = 0
   counts = dict()
   for number in numlist:
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

def median(numlist):
   numlist.sort()
   middle = int(len(numlist)/2)
   median = numlist[middle]   
   print('The median is : ', median)
   return median

def midpoint(numlist):
   maxnum = max(numlist)
   minnum = min(numlist)
   midpoint = (maxnum-minnum)/2
   print('The midpoint is : ', midpoint)

def mean(numlist):
   sumnum = sum(numlist)
   mean = sumnum/len(numlist)
   print('The mean is : ', mean)


mode(numlist)
median(numlist)
midpoint(numlist)
mean(numlist)