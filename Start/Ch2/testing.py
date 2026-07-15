
# Python code​​​​​​‌‌‌​‌‌‌‌‌‌​​​​‌​‌​​​‌​​​‌ below
# Use print("messages...") to debug your solution.

# to solve this challenge we needed to use an if conditional, a loop and the modular operator

# show_expected_result = True
# show_hints = True

# def count_numbers(which, numbers):
# # first to check to see if the function was given a bad value for the which paramater
# # if it is not either even or odd it returns minus one
#   if which != "even" and which != "odd":
#     return -1
#  # then initializes the count numbers function to zero 
#  # Then we have a loop that process each number in the numbers list
#  # then we check to see what result of that number modulo two is
#   result = 0
#   for num in numbers:
#    if which == "even" and num % 2 == 0: # the modulo will give the remainder of the division, 
#                                            #meaning 4/2 = 2.0 has decimal of 0 which is correct
#     result += 1
#    if which == "odd" and num % 2 != 0:
#     result += 1
#   return result


# The % (modulo) operator yields the remainder from the division of the first argument by the second. 
# The numeric arguments are first converted to a common type. A zero right argument raises the ZeroDivisionError exception. 
# The arguments may be floating point numbers, e.g., 3.14%0.7 equals 0.34 (since 3.14 equals 4*0.7 + 0.34.) 
# The modulo operator always yields a result with the same sign as its second operand (or zero); 
# the absolute value of the result is strictly smaller than the absolute value of the second operand [1].

# This is how your code will be called.
# You can edit this code to try different testing cases.
# numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

# # ****** DO NOT CHANGE THIS CODE ******
# result1 = count_numbers("even", numbers)
# result2 = count_numbers("odd", numbers)
# result3 = count_numbers("Blarg", numbers)

# print("Even count: ",result1)
# print("Odd count: ",result2)
# print("Incorrect 'which' parameter count:",result3)

# ---------------------------------------------------------

# Python code​​​​​​‌‌‌‌​​​‌‌​‌​‌​‌​‌​‌‌​​‌‌‌ below
# Use print("messages...") to debug your solution.

# show_expected_result = True
# show_hints = True

# def find_largest(test_strings):
#     # Your code goes here
#     maxlen = 0
#     for s in test_strings:
#         if len(s) > maxlen:
#             maxlen = len(s)
#     return maxlen

# This is how your code will be called.
# Your answer should be the length of the longest string in the list
# You can edit this code to try different testing cases.
# test_strings = [
#     "Hello World!",
#     "And how can this be? For he is the Kwisatz Haderach!",
#     "Four score and seven years ago",
#     "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
# ]
# # result = Answer.find_largest(test_strings)   
# maxlen = find_largest(test_strings)

# print("Largest string: ", maxlen)

# -----------------------------------------------------------------------

# Python code​​​​​​‌‌‌‌​​​‌‌​‌​‌​‌​‌​‌‌​​‌‌‌ below
# Use print("messages...") to debug your solution.

# show_expected_result = True
# show_hints = True

# def is_pallindrome(teststr):
# #     # Your code goes here
# # convert the string to all lower case
#     temp = teststr.lower()

# # strip all the spaces and puncutations from the string
#     newstr = ""
#     for c in temp:
#         if c.isalnum(): # Python checks to see if any given character is alphanumeric
#             newstr += c

# # now calculate the reverse of the string
#     reversestr = ""
#     strindx = len(newstr)-1
#     while (strindx >= 0):
#         reversestr += newstr[strindx]
#         strindx -= 1

#     if newstr == reversestr:
#         return True
#     return False

# # This is how your code will be called.
# # Your answer should determine whether a string is a palindrome.
# # You can edit this code to try different testing cases.

# # test_word = "Madam, I'm Adam."
# # try using some of these other words:
# # test_word = "RACE CAR!"
# # test_word = "Hello, world"
# # test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"

# # result = Answer.is_palindrome(test_word)
# newstr = is_pallindrome(test_word)
# print("Is Palindrome: ", newstr)


# -----------------------------------------------------------------------

# Python code​​​​​​‌‌‌‌​​​‌‌​‌​‌​‌​‌​‌‌​​‌‌‌ below
# Use print("messages...") to debug your solution.

# show_expected_result = True
# show_hints = True

import calendar 

def count_days(year, month, whichday):
    # Your code goes here.
    # use month calender class here
    daycount =  0
    weekslist = calendar.monthcalendar(testyear, testmonth)



    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount



# This is how your code will be called.
# You can edit this code to try different testing cases.
testyear = 2025
testmonth = 12
testday = 0
#result = Answer.count_days(testyear, testmonth, testday)
week = count_days(testyear,testmonth,testday)
print(week)


# -------------------------

# Python code​​​​​​‌‌‌‌​‌​‌‌​‌‌​​‌​​‌​​​‌​‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import os
from os.path import isfile

def file_info():
    # Your code goes here.
    totalbytes = 0
    folder = "deps"
    #get a list of all the files in the current directory
    dirlist = os.listdir(folder)
    for entry in dirlist:
        # make sure it's a file
        if os.path.isfile(folder + "/" + entry) and entry.endswith(".txt"):
            # add the file size to the total
            filesize = os.path.getsize(folder + "/" + entry)
            totalbytes += filesize
    return totalbytes

# This is how your code will be called.
# Your answer should be the total number of bytes of all text files in the "deps" folder.
# result = Answer.file_info()