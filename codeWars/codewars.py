# def filter_list(l) :
#     nl = []
#     for s in l:
#         if type(s) is int:
#             print(s)
#             nl.append(s)
#     print(nl)
#     return nl
#
#
# l = ['a', 1, 'd', 2]
#
# filter_list(l)
#
# #alternate
# def filter_list2(l):
#     return [x for x in l if type(x) is not str]
# print(filter_list2(l))
#
# #alternate2 highest voted best practice
# def filter_list3(l):
#     return[x for x in l if not isinstance(x, str)]
#
# print(filter_list3(l))
#
#
# #7kyu
# #
# # def handicap(list):
# #     newList = []
# #     for member in list:
# #         if member[0] >= 55 and member[1] > 7:
# #             newList.append("senior")
# #         else:
# #              newList.append("open")
# #     print(newList)
#
# def handicap(data):
#     return["Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data]
#
# print(handicap([[44, 8], [55, 8], [55, 1]]))
#
#
# #7kyu Smallest value of an array
# # def min(array, command):
# #     min = array[0]
# #     index = 0
# #     counter = 0
# #     for value in array :
# #         if value < min:
# #             min = value
# #             index = counter
# #         counter = counter + 1
# #     if command == 'value':
# #         return min
# #     else:
# #         return index
# #
# # print(min([1, 2, 3, 4, 5 , 0], 'value'))
# # print(min([1, 2, 3, 4, 5 , 0], 'index'))
#
# def find_smallest(numbers, to_return):
#     return min(numbers) if to_return == 'value' else numbers.index(min(numbers))
#
# print(find_smallest([1,2, 3, 4, 5, 6], 'index'))
# print(find_smallest([1,2, 3, 4, 5, 6], 'value'))\
#
# #7kyu
#remove all the vowels
#functipon that takes a string and return a new string with all vowels removed
#
# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for letter in string:
#         if letter in vowels:
#             string= string[:string.index(letter)] + string[string.index(letter)+1:]
#             print(string)
#     print(string)

#best practice
# def disemvowel(string):
#     return string.translate(None, 'aeiouAEIOU')


#
# def disemvowel(s):
#     return s.translate(None, "aeiouAEIOU")
#
# # print(disemvowel('This is only a test'))
#
# from string import maketrans   # Required to call maketrans function.
#
# intab = "aeiou"
# outtab = ""
# trantab = maketrans(intab, outtab)
#
# str = "this is string example....wow!!!";
# print(str.translate(trantab))


#spinning words
#write a functuion that takes in a string of one or more words, and returns the same string, but with all fice or more letter words reversed. String passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present
# What I learned -> index(word) returns the first found instance of the word in the array
# def spin_words(sentence):
#     array = sentence.split()
#     s = ""
#     n = 0
#     for word in array:
#         if len(word) >= 5:
#             i = len(word) -1
#             while i >= 0:
#                 s += word[i]
#                 i = i - 1
#             s+= " "
#         else:
#             s += word
#             s+= " "
#         n = n + 1
#     S.rstrip() // removes trailing characters
#     return s
#
#
# # alternate solutions
# def spin_words(sentence)
#     return " ".join[x[::-1] if len(x) >=5 else x for x in sentence.split(" ")]
#
# def spin_words(sentence)
#     words = [word for word in sentence.split(" ")]
#     words = [word if len(word) < 5 else word[::1] for word in words]
#     return " ".join(words)

def member(lst):
    list = []
    for (age, handicap) in lst:
        list.append("Sernior") if age >= 55 and handicap > 7 else list.append("Open")
    return list

print(member([[1, 5], [55, 8]]))
