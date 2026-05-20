# ---------------- STRING IN PYTHON ----------------

# Definition:
# A string is a sequence of characters enclosed inside
# single quotes (' '), double quotes (" "), or triple quotes.
# Strings are immutable in Python, which means their values
# cannot be changed after creation.

# name = "manoharsharnagat"

# Accessing character using positive indexing
# Index starts from 0 from the left side

# print(name[0])   # Prints first character -> m
# print(name[1])   # Prints second character -> a

# Accessing character using negative indexing
# Negative index starts from -1 from the right side

# print(name[-1])  # Prints last character -> t
# print(name[-1])  # Again prints last character -> t

# ---------------- SLICING ----------------

# Syntax:
# string[start : end]
# Start index is included
# End index is excluded

# print(name[0:5])   # Characters from index 0 to 4 -> manoh
# print(name[5:9])   # Characters from index 5 to 8 -> arsh

# If end index is not given,
# slicing goes till the end of string

# print(name[5:])    # Prints from index 5 till end -> arsharnagat

# If both start and end are omitted,
# complete string is printed

# print(name[:])     # Prints full string -> manoharsharnagat

# ---------------- STEP SLICING ----------------

# Syntax:
# string[start : end : step]

# Here step = 2 means skip one character after each selection

# print(name[1:8:2])   # Prints characters from index 1 to 7 with step 2

# ---------------- IMPORTANT POINTS ----------------

# 1. Strings are immutable in Python.
# 2. Indexing starts from 0.
# 3. Negative indexing starts from -1.
# 4. Slicing does not include the ending index.
# 5. Step value is used to skip characters.
# 6. Time Complexity of indexing = O(1)
# 7. Time Complexity of slicing = O(n)

# Example of Index Positions:
#
#   Character :  m  a  n  o  h  a  r  s  h  a  r  n  a  g  a  t
#   Index     :  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
#
# Negative Index:
#
#  -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


# ---------------- STRING FUNCTIONS IN PYTHON ----------------

# Definition:
# String functions are built-in methods used to perform
# different operations on strings such as changing case,
# formatting text, searching, replacing, etc.

# s = "Python are High level Programing Language"

# ---------------- LOWER FUNCTION ----------------

# lower() converts all characters of the string into lowercase

# print(s.lower())

# Output:
# python are high level programing language


# ---------------- UPPER FUNCTION ----------------

# upper() converts all characters of the string into uppercase

# print(s.upper())

# Output:
# PYTHON ARE HIGH LEVEL PROGRAMING LANGUAGE


# ---------------- SWAPCASE FUNCTION ----------------

# swapcase() converts:
# Uppercase letters -> lowercase
# Lowercase letters -> uppercase

# print(s.swapcase())

# Output:
# pYTHON ARE hIGH LEVEL pROGRAMING lANGUAGE


# ---------------- TITLE FUNCTION ----------------

# title() converts the first letter of every word into uppercase

# print(s.title())

# Output:
# Python Are High Level Programing Language


# ---------------- CAPITALIZE FUNCTION ----------------

# capitalize() converts only the first character of
# the entire string into uppercase and remaining
# characters into lowercase

# print(s.capitalize())

# Output:
# Python are high level programing language


# ---------------- IMPORTANT POINTS ----------------

# 1. Strings are immutable in Python.
#    These functions do not change the original string.
#    They return a new modified string.

# 2. String functions are also called string methods.

# 3. Syntax of string methods:
#    variable.method()

# 4. lower() and upper() are commonly used
#    for case-insensitive comparisons.

# 5. title() capitalizes each word,
#    while capitalize() affects only the first character
#    of the whole sentence.

# 6. swapcase() reverses the case of each character.

# 7. Time Complexity:
#    Most string case conversion functions take O(n)
#    because each character is processed once.
# -----------------------------------------------------------------------------------------------------------------
# # ---------------- FORMAT FUNCTION IN PYTHON ---------------------------------------------------------------------

# # Definition:
# # Formatting is used to insert variables or values
# # inside a string in a clean and readable way.

# name = "manohar"
# sal = 2000
# age = 22


# # ---------------- format() FUNCTION ----------------

# # Syntax:
# # "text {}".format(value)

# # Curly braces {} act as placeholders.
# # Values inside format() are inserted into those placeholders
# # in the same order.

# print("{} sal is {} age is {}".format(name, sal, age))

# # Output:
# # manohar sal is 2000 age is 22


# # ---------------- F-STRING ----------------

# # f-string is a modern and easier way of formatting strings.
# # Introduced in Python 3.6

# # Syntax:
# # f"text {variable}"

# print(f"{name} is a good boy")

# # Output:
# # manohar is a good boy


# # ---------------- IMPORTANT POINTS ----------------

# # 1. format() function is used to insert values into strings.

# # 2. {} are called placeholders.

# # 3. Values are inserted according to their order in format().

# # 4. f-strings are faster and easier to read compared to format().

# # 5. To use f-string, place letter 'f' before the string.

# # 6. Variables can be directly written inside {} in f-strings.

# # 7. String formatting is commonly used in:
# #    - Printing output
# #    - Reports
# #    - Billing software
# #    - User messages
# #    - Dynamic text generation


# # ---------------- DIFFERENCE ----------------

# # format() method:
# # "My name is {}".format(name)

# # f-string:
# # f"My name is {name}"

# # f-string is more readable and mostly preferred in modern Python.

# -----------------------------------------------------------------------------------------------------------------
# # loop in string

# name= "Manohar Sharnagat"
# for i in name:
#     print(i)



# # write a program to remove duplicate charachers form string
# new_name=""
# for i in name:
#     if i not in new_name:
#         new_name += i
# print(new_name)


# Q.reverse the string
# N = len(name)
# reverse_name=""
# for i in range(N-1,-1,-1):
#     reverse_name += name[i]

# print(reverse_name)

# Q. Palindrome

# name="manohar"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")


# # homework
# Name="Manohar"
# N = len(Name)
# output=""
# for i in Name:
#     for j in range(N-1,-1,-1):
#         if Name[i] == Name[j]:
#             output += Name[i]
#         else:
#             print("Not a Palindrome")
#             break


# Q.vowels or constrents

# vowels = ['a','e','i','o','u']
# name="Manohar"
# vow = 0
# con = 0 
# for i in name:
#     if i in vowels:
#         vow += 1

#     else:
#         con += 1
# print("consonent : " , con)
# print("Vowels: ",vow)


# Q. write a program to check if two strings are anagrams of each other

# Q. count words in string
# name="RCB will losses this year too"
# count= 1

    
# for i in name:
#     if i == ' ':
#         count += 1
# print(count)

# work1="Manohar"
# work2="sharnagat"
# -----------------------------------------------------------------------------------------------------------------
# input= "gasgg54@#vscsd!s*"
# count=0
# for i in input:
#     if i in input:
#      (ord(i)> 0 and ord(i) < 48) and ( ord(i)> 57 and ord(i) < 65)  and ( ord(i)> 90 and ord(i) < 97) and ord(i)> 122
#     count += 1



# Q. write a program to conver the first leter of each word in to uppercase in sentence

# sen = "fjldjdo. lldjdl jdlfd jldfjdlf dljfdl"

# print(sen.title())


# # -----------------------------------------------------------------------------------------------------------------
# print("manohar14ms".isalnum())
# print("manoharsharnagat".isalpha())
# print("777f".isdigit())
# print("sdsdsds".islower())
# print(''.islower())
# print('my name is manohar'.istitle())

# print("manohar".find("a"))
# print("manohar".index("r"))
# print("manohar".count("r"))


# for i in range (1,4):
#     for j in range(1,4):
#         print(i,end = " ")
#     print("")

# n = int (input("Enter the number of rows"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(chr(64+i),end=" ")
#     print("\t")

# n = int (input("Enter the number of rows"))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+i),end=" ")
#     print("\t")


# ##homework
# n = int (input("Enter the number of rows"))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         print(chr(64+j),end=" ")
    
#     print("\t")


# import time
# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-1),end = " ")
#     for j in range(1, i+2):
#         time.sleep(3)
#         print("*",end=" ")
#     print()


# mylist= [1,2,3,4]
# newlist=[]
# for i in mylist:
#     D = 1
#     if i == i:
#         continue
#     else:
#         newlist[i]= D*ip
# print(newlist)


# ---------------- TUPLE IN PYTHON ----------------

# Definition:
# A Tuple is a collection data type used to store multiple values
# in a single variable.

# Tuples are:
# 1. Ordered
# 2. Immutable (cannot be changed)
# 3. Allow duplicate values
# 4. Written using round brackets ()

# Creating a tuple

# mytuple = ("manohar", "ashish", "Rudra", "RCB", 47)

# Printing complete tuple

# print(mytuple)

# type() function returns the datatype of variable

# print(type(mytuple))


# ---------------- IMMUTABILITY ----------------

# Tuples are immutable.
# This means we cannot modify, add, or remove elements
# after tuple creation.

# The below line will generate an error because
# tuple elements cannot be changed.

# mytuple[2] = "nihar"

# print(mytuple)


# ---------------- ERROR EXPLANATION ----------------

# Error:
# TypeError: 'tuple' object does not support item assignment

# Reason:
# Python tuples are immutable, so values inside them
# cannot be reassigned.


# ---------------- IMPORTANT POINTS ----------------

# 1. Tuple preserves insertion order.

# 2. Tuple is faster than list because it is immutable.

# 3. Tuple elements can be accessed using indexing.

# 4. Mixed datatype values are allowed inside tuple.

# 5. Parentheses () are used to create tuples.

# 6. Tuple is commonly used when data should remain fixed.

# Example:
# Employee IDs
# Coordinates
# Database records
# Fixed configuration values


# ---------------- DIFFERENCE BETWEEN LIST & TUPLE ----------------

# LIST:
# - Mutable
# - Uses []
# - Slower
# - Can modify elements

# TUPLE:
# - Immutable
# - Uses ()
# - Faster
# - Cannot modify elements


# ---------------- TIME COMPLEXITY ----------------

# Accessing element using index -> O(1)
# Searching element -> O(n)


# ---------------- TUPLE QUESTION ----------------

# Q1:
# What will be the output of the following code?

# init_tuple = ()

# print(init_tuple.__len__())


# ---------------- EXPLANATION ----------------

# () represents an empty tuple.

# __len__() is a special method used to return
# the total number of elements in the tuple.

# Since the tuple is empty,
# the number of elements = 0


# ---------------- OUTPUT ----------------

# 0


# ---------------- CORRECT ANSWER ----------------

# C. 0


# ---------------- IMPORTANT POINTS ----------------

# 1. Empty tuple syntax:
#    ()

# 2. len(tuple_name) and tuple_name.__len__()
#    both return the size of tuple.

# Example:
# len(init_tuple)

# 3. __len__() is called a magic method or dunder method.

# 4. Tuple length operation takes O(1) time complexity
#    because Python stores size internally.


# ---------------- EXTRA EXAMPLES ----------------

# Tuple with elements
# t = (1, 2, 3)

# print(len(t))        -> 3
# print(t.__len__())   -> 3

# ---------------- TUPLE QUESTION 2 ----------------

# Q:
# What will be the output of the following code?

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')

# print(init_tuple_a == init_tuple_b)


# ---------------- EXPLANATION ----------------

# In Python, tuples can be created in two ways:

# 1. Without parentheses
# 2. With parentheses

# Both statements below create the same tuple:

# ('a', 'b')

# So:
# init_tuple_a and init_tuple_b contain identical values.


# ---------------- COMPARISON ----------------

# == operator checks whether both tuples
# have the same elements in the same order.

# Since both tuples are equal,
# the result will be True.


# ---------------- OUTPUT ----------------

# True


# ---------------- IMPORTANT POINTS ----------------

# 1. Parentheses are optional while creating tuples.

# Example:
# t1 = 1, 2, 3
# t2 = (1, 2, 3)

# Both are tuples.

# 2. Comma is the actual tuple operator in Python.

# 3. == compares values, not memory location.

# 4. Tuple comparison checks:
#    - Number of elements
#    - Order of elements
#    - Values of elements


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# a = (1, 2)
# b = (1, 2)

# print(a == b)
# Output: True


# Example 2:
# a = (1, 2)
# b = (2, 1)

# print(a == b)
# Output: False
# Because order is different.


# ---------------- TIME COMPLEXITY ----------------

# Tuple comparison worst case -> O(n)
# because elements are checked one by one.


# ---------------- TUPLE QUESTION 3 ----------------

# Q:
# What will be the output of the following code?

# init_tuple_a = '1', '2'
# init_tuple_b = '3', '4'

# print(init_tuple_a + init_tuple_b)


# ---------------- EXPLANATION ----------------

# Both variables are tuples.

# init_tuple_a = ('1', '2')
# init_tuple_b = ('3', '4')

# The + operator is used for tuple concatenation.

# Concatenation means joining two tuples together
# into a single tuple.


# ---------------- OUTPUT ----------------

# ('1', '2', '3', '4')


# ---------------- WORKING ----------------

# First tuple:
# ('1', '2')

# Second tuple:
# ('3', '4')

# After concatenation:
# ('1', '2', '3', '4')


# ---------------- IMPORTANT POINTS ----------------

# 1. + operator joins tuples.

# 2. Concatenation creates a new tuple.

# 3. Original tuples remain unchanged
#    because tuples are immutable.

# 4. Tuple concatenation works only with tuples.

# Example:
# (1, 2) + (3, 4)   -> Valid

# (1, 2) + [3, 4]   -> Error
# Because tuple and list are different datatypes.


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# a = (10, 20)
# b = (30, 40)

# print(a + b)

# Output:
# (10, 20, 30, 40)


# Example 2:
# x = ('RCB',)
# y = ('WIN',)

# print(x + y)

# Output:
# ('RCB', 'WIN')


# ---------------- TIME COMPLEXITY ----------------

# Tuple concatenation -> O(n + m)

# Because Python creates a new tuple
# and copies elements from both tuples.

# ---------------- TUPLE QUESTION 4 ----------------

# Q:
# What will be the output of the following code?

# l = [1, 2, 3]

# init_tuple = ('python',) * (l.__len__() - l[::-1][0])

# print(init_tuple)


# ---------------- STEP BY STEP EXPLANATION ----------------

# List:
# l = [1, 2, 3]

# ---------------- PART 1 ----------------
# l.__len__()

# __len__() returns the total number of elements in list.

# Total elements = 3

# So:
# l.__len__() = 3


# ---------------- PART 2 ----------------
# l[::-1]

# Syntax:
# list[start : end : step]

# Here step = -1
# It reverses the list.

# Reversed list:
# [3, 2, 1]


# ---------------- PART 3 ----------------
# l[::-1][0]

# First element of reversed list = 3

# So:
# l[::-1][0] = 3


# ---------------- PART 4 ----------------

# Expression:
# (l.__len__() - l[::-1][0])

# = 3 - 3
# = 0


# ---------------- PART 5 ----------------

# ('python',) * 0

# Multiplying tuple by 0 creates an empty tuple.

# Result:
# ()


# ---------------- OUTPUT ----------------

# ()


# ---------------- IMPORTANT POINTS ----------------

# 1. ('python',) is a single-element tuple.

# IMPORTANT:
# Comma is necessary for single-element tuple.

# Correct:
# ('python',)

# Wrong:
# ('python')
# This becomes a string, not tuple.


# 2. Tuple multiplication repeats elements.

# Example:
# ('A',) * 3

# Output:
# ('A', 'A', 'A')


# 3. Negative slicing [::-1] is used to reverse sequence.

# 4. __len__() returns total number of elements.


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# t = ('Hi',) * 2
# Output:
# ('Hi', 'Hi')

# Example 2:
# a = [10, 20, 30]
# print(a[::-1])

# Output:
# [30, 20, 10]


# ---------------- TIME COMPLEXITY ----------------

# Reversing list using slicing -> O(n)

# Tuple multiplication -> O(n)
# depending on repetition count.

# ---------------- TUPLE QUESTION 5 ----------------

# Q:
# What will be the output of the following code?

# init_tuple = ('python',) * 3

# print(type(init_tuple))
# print(init_tuple)


# ---------------- EXPLANATION ----------------

# ('python',) is a single-element tuple.

# IMPORTANT:
# A comma is necessary to create a single-element tuple.

# Example:
# ('python',)  -> Tuple
# ('python')   -> String


# ---------------- TUPLE MULTIPLICATION ----------------

# * operator repeats tuple elements.

# ('python',) * 3 means:
# Repeat the tuple 3 times.


# ---------------- WORKING ----------------

# Original tuple:
# ('python',)

# After multiplication:
# ('python', 'python', 'python')


# ---------------- OUTPUT ----------------

# <class 'tuple'>

# ('python', 'python', 'python')


# ---------------- IMPORTANT POINTS ----------------

# 1. Tuple multiplication is called tuple repetition.

# 2. Multiplication creates a new tuple.

# 3. Tuples are immutable, so original tuple does not change.

# 4. type() function is used to check datatype.

# 5. Single-element tuple MUST contain comma.


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# t = (1,) * 4

# Output:
# (1, 1, 1, 1)


# Example 2:
# x = ('RCB',) * 2

# Output:
# ('RCB', 'RCB')


# Example 3:
# s = ('hello')
# print(type(s))

# Output:
# <class 'str'>

# Because comma is missing.


# ---------------- TIME COMPLEXITY ----------------

# Tuple repetition -> O(n)
# where n = number of repeated elements.

# ---------------- TUPLE QUESTION 6 ----------------

# Q:
# What will be the output of the following code?

# init_tuple = ((1, 2),) * 7

# print(init_tuple)
# print(len(init_tuple[3:8]))


# ---------------- STEP BY STEP EXPLANATION ----------------

# ((1, 2),)

# This is a tuple containing one inner tuple:
# ((1, 2),)

# ---------------- TUPLE MULTIPLICATION ----------------

# * 7 repeats the tuple 7 times.

# So:
# ((1, 2),) * 7

# becomes:

# (
#   (1, 2),
#   (1, 2),
#   (1, 2),
#   (1, 2),
#   (1, 2),
#   (1, 2),
#   (1, 2)
# )


# ---------------- FIRST PRINT ----------------

# print(init_tuple)

# Output:
# ((1, 2), (1, 2), (1, 2), (1, 2),
#  (1, 2), (1, 2), (1, 2))


# ---------------- SLICING ----------------

# init_tuple[3:8]

# Syntax:
# tuple[start : end]

# Start index = 3
# End index = 8 (excluded)

# Tuple contains total 7 elements
# Index positions:

# 0 1 2 3 4 5 6

# Elements selected:
# index 3, 4, 5, 6

# Total selected elements = 4


# ---------------- len() FUNCTION ----------------

# len() returns total number of elements.

# print(len(init_tuple[3:8]))

# Output:
# 4


# ---------------- FINAL OUTPUT ----------------

# ((1, 2), (1, 2), (1, 2), (1, 2),
#  (1, 2), (1, 2), (1, 2))

# 4


# ---------------- IMPORTANT POINTS ----------------

# 1. Tuple multiplication repeats tuple elements.

# 2. Slicing excludes ending index.

# 3. If ending index exceeds tuple size,
#    Python does NOT generate error.

# Example:
# t[3:100]
# Python automatically stops at last element.

# 4. len() returns total number of elements.

# 5. Nested tuple means tuple inside another tuple.


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# t = (1, 2, 3, 4, 5)

# print(t[1:4])

# Output:
# (2, 3, 4)


# Example 2:
# x = ('A',) * 5

# Output:
# ('A', 'A', 'A', 'A', 'A')


# ---------------- TIME COMPLEXITY ----------------

# Tuple slicing -> O(k)
# where k = number of sliced elements.

# len() -> O(1)


# ---------------- DICTIONARY IN PYTHON ----------------

# Definition:
# Dictionary is a collection data type used to store
# data in KEY : VALUE pairs.

# Dictionaries are:
# 1. Mutable
# 2. Ordered (Python 3.7+)
# 3. Do not allow duplicate keys
# 4. Written using curly brackets {}

# ---------------- CREATING DICTIONARY ----------------

# mydict = {
#     101: "manohar",
#     102: "nihar",
#     "103": "shlock",
#     "104": "bhai",
#     101: "Rudra",
#     104: "RCB"
# }

# Printing dictionary

# print(mydict)


# ---------------- IMPORTANT CONCEPT ----------------

# Dictionaries do NOT allow duplicate keys.

# If duplicate keys are present,
# the latest value overwrites the previous value.

# Here:
# 101: "manohar"  -> overwritten by -> 101: "Rudra"
# because key 101 appears again.

# Final dictionary becomes:

# {
#   101: 'Rudra',
#   102: 'nihar',
#   '103': 'shlock',
#   '104': 'bhai',
#   104: 'RCB'
# }

# NOTE:
# "104" (string) and 104 (integer) are different keys.


# ---------------- UPDATING VALUE ----------------

# Dictionary is mutable,
# so values can be changed using key.

# mydict[102] = "peter"

# print(mydict)

# Value of key 102 changes from:
# "nihar" -> "peter"


# ---------------- LOOPING THROUGH DICTIONARY ----------------

# By default, loop iterates through keys.

# for x in mydict:
#     print(x)

# Output:
# Prints all keys


# ---------------- values() METHOD ----------------

# values() returns all values of dictionary.

# for x in mydict.values():
#     print(x)

# Output:
# Prints all values


# ---------------- items() METHOD ----------------

# items() returns both key and value as tuple.

# for x, y in mydict.items():
#     print(x, y)

# Output:
# Prints key-value pairs


# ---------------- IMPORTANT POINTS ----------------

# 1. Dictionary stores data as KEY : VALUE pairs.

# 2. Keys must be unique.

# 3. Duplicate keys overwrite old values.

# 4. Values can be duplicated.

# 5. Dictionaries are mutable.

# 6. Keys can be integer, string, tuple, etc.

# 7. Dictionary indexing is done using keys.

# Example:
# mydict[101]

# 8. values() -> returns values
#    keys()   -> returns keys
#    items()  -> returns key-value pairs


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# student = {
#     "name": "Manohar",
#     "age": 22
# }

# print(student["name"])

# Output:
# Manohar


# Example 2:
# student["age"] = 25

# Output:
# Age value updated


# ---------------- TIME COMPLEXITY ----------------

# Accessing value using key -> O(1)

# Inserting value -> O(1)

# Searching key -> O(1) average case

# Looping through dictionary -> O(n)


# ---------------- DICTIONARY OPERATIONS ----------------

# Existing dictionary

# mydict = {
#     101: "Rudra",
#     102: "peter",
#     "103": "shlock",
#     "104": "bhai",
#     104: "RCB"
# }


# ---------------- ADDING NEW ELEMENT ----------------

# Syntax:
# dictionary[key] = value

# Adding a new key-value pair

# mydict["mobile_no"] = 8767930754

# print(mydict)

# Output:
# {
#   101: 'Rudra',
#   102: 'peter',
#   '103': 'shlock',
#   '104': 'bhai',
#   104: 'RCB',
#   'mobile_no': 8767930754
# }


# ---------------- pop() METHOD ----------------

# pop(key) removes the element using given key.

# Here key 101 will be removed.

# mydict.pop(101)

# print(mydict)

# Output:
# Dictionary without key 101


# ---------------- IMPORTANT ----------------

# If key is not found,
# pop() generates KeyError.

# Example:
# mydict.pop(999)
# -> Error


# ---------------- clear() METHOD ----------------

# clear() removes all elements from dictionary
# and makes dictionary empty.

# mydict.clear()

# print(mydict)

# Output:
# {}


# ---------------- IMPORTANT POINTS ----------------

# 1. Dictionary is mutable,
#    so elements can be added, updated, and deleted.

# 2. New key-value pairs can be inserted dynamically.

# 3. pop(key) removes specific element using key.

# 4. clear() removes all elements from dictionary.

# 5. After clear(), dictionary still exists
#    but becomes empty.


# ---------------- DIFFERENCE ----------------

# pop(key)
# - Removes only one element
# - Requires key

# clear()
# - Removes all elements
# - No argument required


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# student = {
#     "name": "Manohar",
#     "age": 22
# }

# student["city"] = "Nagpur"

# Output:
# New key added


# Example 2:
# student.pop("age")

# Output:
# age key removed


# Example 3:
# student.clear()

# Output:
# {}


# ---------------- TIME COMPLEXITY ----------------

# Adding element -> O(1)

# pop() -> O(1) average case

# clear() -> O(n)
# because all elements are removed.


# ---------------- DICTIONARY QUESTION ----------------

# Q:
# What will be the output of the following code?

# a = {(1,2):1, (2,3):2, (4,5):3}

# print(a[4,5])


# ---------------- EXPLANATION ----------------

# Dictionary keys are tuples.

# Keys:
# (1,2)
# (2,3)
# (4,5)

# In Python:
# a[4,5]

# is automatically treated as:

# a[(4,5)]

# because comma-separated values inside indexing
# become a tuple.


# ---------------- VALUE ACCESS ----------------

# Key:
# (4,5)

# Corresponding value:
# 3


# ---------------- OUTPUT ----------------

# 3


# ---------------- IMPORTANT NOTE ----------------

# The correct output "3" is NOT present in options.

# So, the given options are incorrect.


# ---------------- OPTION ANALYSIS ----------------

# A. KeyError      -> Wrong
# Because key (4,5) exists.

# B. 1             -> Wrong
# Value for key (1,2) is 1.

# C. {(2,3):2}     -> Wrong
# This is dictionary data, not output.

# D. {(1,2):1}     -> Wrong
# Also dictionary data, not output.


# ---------------- CORRECT ANSWER ----------------

# Correct Output = 3
# (Options are incorrect)


# ---------------- IMPORTANT POINTS ----------------

# 1. Tuples can be used as dictionary keys
#    because tuples are immutable.

# 2. Dictionary indexing:
#    dictionary[key]

# 3. Python converts:
#    a[4,5]
# into:
#    a[(4,5)]

# 4. Dictionary keys must be immutable types:
#    - int
#    - str
#    - tuple

# 5. Lists cannot be dictionary keys
#    because lists are mutable.


# ---------------- EXTRA EXAMPLES ----------------

# Example 1:
# d = {(1,1): "RCB"}

# print(d[(1,1)])

# Output:
# RCB


# Example 2:
# d = {[1,2]: "Hello"}

# Output:
# Error
# Because list cannot be key.


# ---------------- TIME COMPLEXITY ----------------

# Dictionary access using key -> O(1) average case

# ---------------- DICTIONARY QUESTION 2 ----------------

# Q2:
# What will be the output of the following code?

# a = {'a':1, 'b':2, 'c':3}

# print(a['a','b'])


# ---------------- EXPLANATION ----------------

# Dictionary keys are:
# 'a'
# 'b'
# 'c'

# In Python:
# a['a','b']

# is treated as:

# a[('a', 'b')]

# because comma-separated values automatically
# form a tuple.


# ---------------- IMPORTANT ----------------

# Dictionary does NOT contain key:
# ('a', 'b')

# Therefore Python generates an error.


# ---------------- OUTPUT ----------------

# KeyError: ('a', 'b')


# ---------------- CORRECT ANSWER ----------------

# KeyError


# ---------------- IMPORTANT POINTS ----------------

# 1. a['a','b'] becomes tuple key access.

# 2. Dictionary raises KeyError
#    when key does not exist.

# 3. Tuples can be dictionary keys.


# =========================================================
# ---------------- DICTIONARY QUESTION 3 ----------------
# =========================================================

# Q3:
# What will be the output of the following code?

# arr = {}

# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1

# print(arr)

# sum = 0

# for k in arr:
#     sum += arr[k]

# print(sum)


# ---------------- STEP BY STEP EXPLANATION ----------------

# Empty dictionary created

# arr = {}


# ---------------- STEP 1 ----------------

# arr[1] = 1

# Dictionary becomes:
# {1: 1}


# ---------------- STEP 2 ----------------

# arr['1'] = 2

# IMPORTANT:
# 1 (integer) and '1' (string) are different keys.

# Dictionary becomes:
# {
#    1: 1,
#   '1': 2
# }


# ---------------- STEP 3 ----------------

# arr[1] += 1

# Existing value of key 1:
# 1

# Updated value:
# 1 + 1 = 2

# Final dictionary:
# {
#    1: 2,
#   '1': 2
# }


# ---------------- FIRST OUTPUT ----------------

# print(arr)

# Output:
# {1: 2, '1': 2}


# ---------------- SUM CALCULATION ----------------

# sum = 0

# Loop iterates through keys:
# 1 and '1'

# for k in arr:
#     sum += arr[k]

# sum = 0 + 2 + 2
# sum = 4


# ---------------- FINAL OUTPUT ----------------

# print(sum)

# Output:
# 4


# ---------------- IMPORTANT POINTS ----------------

# 1. Integer key 1 and string key '1'
#    are completely different.

# 2. Dictionaries allow mixed datatype keys.

# 3. += operator updates existing value.

# 4. Looping through dictionary gives keys by default.

# 5. arr[k] accesses value using key.


# ---------------- FINAL OUTPUT SUMMARY ----------------

# {1: 2, '1': 2}
# 4


# ---------------- TIME COMPLEXITY ----------------

# Dictionary insertion -> O(1)

# Dictionary update -> O(1)

# Dictionary access -> O(1)

# Loop through dictionary -> O(n)

# Q4
 
# my_dict ={}
# my_dict[1] =1
# my_dict['1'] =2
# my_dict[1.0] = 4
# print(my_dict)

# sum=0 
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# # Q5
# my_dict ={}
# my_dict[(1,2,4)]= 8
# my_dict[(4,2,1)]= 10
# my_dict[(1,2)]= 12
# print(my_dict)

# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)
# print(my_dict)

# # Q6
# box ={}
# jars={}
# crates={}
# box['biscuit'] = 1
# box ['cake'] =3
# jars['jam'] =4
# crates['box'] =box
# crates['jars'] = jars

# print(len(crates(box)))

# # Q7
# dict = {'c':97,'a':96,'b':98}

# for _ in sorted(dict):
#     print (dict[_])


# # Q8
# rec = {"Name": "python", "Age":"20"}

# r = rec.copy()
# print(id(r) == id(rec))
# print(id(rec))
# print(id(r))

# Q9
# rec = {"Name": "python", "Age":"20"}
# id1 = id(rec)
# print(id1)
# del rec

# rec = {"Name": "python", "Age":"20"}
# id2 = id(rec)
# print(id2)
# print(id1==id2)

# # homework
# # Q10 find the key with the mazimum value n a dictinary:


# mydict={'A':50,"B":30,'c':70}
# max_key = None
# max = float('-inf')
# for key , value in mydict.items():
#     if value > max:
#         max = value
#         max_key = key

# print(max_key)

# # Q11 find the key with the minimum value in a dictionary:
# mydict={'A':50,"B":30,'c':70}
# max_key = None
# max = float('inf')
# for key , value in mydict.items():
#     if value < max:
#         max = value
#         max_key = key

# print(max_key)

# Q12 count frequency of elements in a list using a dictionary:
# mydict={1,2,2,3,4,3,5}

#homework

#reverse number 
# num = 123
# a = num % 10
# num = num //10
# b = num % 10
# c = num // 10 
# rev = a * 100 + b* 10 +c *1
# print(rev)

# for 123456

# num= 123456
# a = num % 10 #6
# num = num //10 #num1=12345
# b = num % 10 #5
# num = num // 10
# c = num % 10 #4
# num = num // 10
# d = num % 10 #3
# num = num // 10
# e = num % 10 #2
# f = num // 10
# rev1 = a * 100000 + b * 10000 + c * 1000 + d * 100 + e* 10 + f

# print(rev1)

# # Q enter amount for withdraw

# amount = int(input("Enter the Amount for withdraw"))
# print("100 Notes = ", amount // 100)
# print("50 Notes = ", (amount % 100)// 50 )
# print("20 Notes = ", (amount % 100 % 50 )// 20 )
# print("10 Notes = ", (amount % 100 % 50 %20  )// 10 )
# print("5 Notes = ", (amount % 100 % 50 %20 % 10  )// 5)
# print("2 Notes = ", (amount % 100 % 50 %20 % 10 %5 )// 2)
# print("1 Notes = ", (amount % 100 % 50 %20 % 10 %5 % 2)// 1)
