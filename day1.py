# ===================== ADD TWO NUMBERS & PYTHON BASICS ===================== #

# to check DATAtype use -> type(variable_name)
# Example:
# age = 18
# print(type(age))
# Output: <class 'int'>

# To Check Address of Variable use -> id(variable_name)
# id() gives the memory address/reference of variable

# age= 18
# age1=18
# age2=18
# name='Manohar sharnagat'

# print(type(age))      # Checks datatype of variable
# print(id(age))        # Memory address of age
# print(id(age1))       # Memory address of age1
# print(id(age2))       # Memory address of age2

# Working:
# Python stores same immutable values at same memory location sometimes.
# So age, age1 and age2 may have same address.



# ===================== TYPE CASTING ===================== #
# Type Casting means converting one datatype into another datatype.

##--------TypeCasting.------- (int Here)

# print(int(3.14))   # Converts float into integer -> Output: 3
# print(int(True))   # True becomes 1
# print(int(False))  # False becomes 0
# print(int("4"))    # String "4" converts into integer 4

# print(float("Name"))
# Error because alphabet string cannot be converted into float



# ===================== COMPLEX() FUNCTION ===================== #
# complex() is used to convert values into complex numbers.

# print(complex(3))        # Output: (3+0j)
# print(complex(12.5))     # Output: (12.5+0j)
# print(complex(True))     # True = 1 -> (1+0j)
# print(complex(False))    # False = 0 -> (0+0j)
# print(complex("5"))      # Output: (5+0j)
# print(complex("5.6"))    # Output: (5.6+0j)

# print(complex("5,-3"))
# Error because complex number format is wrong



# ===================== BOOL() FUNCTION ===================== #
# bool() converts values into True or False

# print(bool(0))       # False because 0 means empty/zero
# print(bool(15))      # True because non-zero value
# print(bool(3.15))    # True
# print(bool(0.0))     # False
# print(bool(1+2j))    # True
# print(bool(0+0j))    # False
# print(bool(-1))      # True
# print(bool(False))   # False
# print(bool(True))    # True
# print(bool(""))      # Empty string = False



# ===================== ADDITION OF TWO NUMBERS ===================== #
# input() takes data from user as string
# int() converts string into integer

# a = int(input("Enter first Number :"))
# b = int(input("Enter the Second Number"))
# print(a+b)

# Working:
# User enters two numbers
# Both numbers converted into integer
# Then both values are added and printed



# ===================== SIMPLE IF CONDITION ===================== #
# if statement checks condition

# a = int(input("Enter Any single Digit Number:"))

# if a > 0:
#     print("Positive Number")

# if a < 0:
#     print("Negative Number")

# if a == 0:
#     print("Zero")

# Working:
# If number > 0 -> Positive
# If number < 0 -> Negative
# If number == 0 -> Zero



# ===================== IF ELSE CONDITION ===================== #
# Used when only one condition should execute

# day = input("Enter Todays Day").lower()

# if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
#     print("Working Day!! Go to work")
# else:
#     print("NO work Today !!")

# Working:
# lower() converts input into lowercase
# If entered day is weekday -> Working day
# Otherwise -> Holiday



# ===================== CHARACTER CHECK PROGRAM ===================== #
# ord() converts character into ASCII value

# char = ord(input("Enter Any One Character: "))

# if(char >= 65 and char <= 90):
#     print("Upper Case")

# elif(char >= 97 and char <=122):
#     print("Lower Case")

# elif(char >= 48 and char <=57):
#     print("Digits")

# else:
#     print("Special Symbols")

# ASCII Range:
# A-Z = 65 to 90
# a-z = 97 to 122
# 0-9 = 48 to 57



# ===================== MEMBERSHIP OPERATOR ===================== #
# in operator checks whether value exists or not

# name ="Manohar"

# if "a" in name:
#     print("a is Present in Name")
# else:
#     print("A does not Present in Name")

# Working:
# Checks if character 'a' exists inside string



# ===================== IDENTITY OPERATOR ===================== #
# is operator compares memory address

# math = 50
# chem = 50

# print(math is chem)

# Working:
# If both variables point to same memory address -> True



# ===================== FOR LOOP ===================== #
# Loop is used to repeat task multiple times

# R = int(input("Enter how many Digit you want in First block"))

# for A in range(1,11):  # Outer loop runs from 1 to 10

#     for i in range(1,R):   # Inner loop
#         print(i * A , end="\t")

#     print()

# print("------------------------------------------------------------------------------")

# Working:
# Creates multiplication table block
# end="\t" gives tab spacing
# print() moves cursor to next line



# ===================== SECOND TABLE BLOCK ===================== #

# R1 = int(input("Enter how many Digit you want in second block"))

# for A in range(1, 11):

#     for i in range(R,R1):
#         print(i * A , end="\t")

#     print()

# print("-----------------------------------------------------------------")

# Working:
# Generates second multiplication block
# Starts from previous R value till R1



# ===================== BREAK & CONTINUE ===================== #
# break -> stops loop completely
# continue -> skips current iteration

# for i in range(1,15):

#     if i == 3:
#         break

#     print(i)

# Working:
# Loop stops when i becomes 3



# ===================== ZIP FUNCTION ===================== #
# zip() combines multiple iterables together

# for i , j in zip(range(1,6), range(5,0,-1)):

#     if i == 3:
#         continue

#     print(i, " \t ", j)

# Working:
# First range -> 1 to 5
# Second range -> 5 to 1
# Both values printed together



# ===================== LIST ===================== #
# List stores multiple values in single variable
# Lists are mutable (changeable)

# mylist= ["manohar","rudra","Nihar","shlok",49,"RCB"]

# print(mylist)
# print(type(mylist))

# print(mylist[0])     # First element
# print(mylist[1])
# print(mylist[2])

# print(mylist[-1])    # Last element

# print(mylist[2:5])   # Slicing
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

# Working:
# Index starts from 0
# Negative index starts from end



# ===================== CHANGE VALUE IN LIST ===================== #

# mylist[2]="Nigaamon"
# print(mylist)

# Working:
# Replaces old value at index 2



# ===================== CHECK ELEMENT IN LIST ===================== #

# if "manohar" in mylist:
#     print("yes manohar is available")
# else:
#     print("not Available")

# Working:
# Checks whether value exists in list



# ===================== APPEND FUNCTION ===================== #
# append() adds element at end of list

# mylist.append('vidhi')
# mylist.append('Laxman')

# print(mylist)



# ===================== INSERT FUNCTION ===================== #
# insert(index,value) inserts value at specific position

# mylist.insert(3,"Bhai")
# print(mylist)



# ===================== REMOVE FUNCTION ===================== #
# remove() deletes specific value

# mylist.remove("Bhai")
# print(mylist)



# ===================== COPY LIST ===================== #
# copy() creates duplicate list

# newlist = mylist.copy()
# print(newlist)



# ===================== NESTED LIST ===================== #
# List inside another list = Nested list

# mylist = [['Manohar','sharnagat'],['33434'],[440019,'yyyy']]

# print("Example of multidimensional list:")
# print(mylist)

# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][1])

# Working:
# First [] -> row
# Second [] -> column/index inside row



mylist= ["manohar","rudra","Nihar","shlok",49,"RCB"]



# ===================== DELETE ELEMENT ===================== #
# del keyword removes element using index

# del mylist[2]
# print(mylist)



# ===================== CLEAR LIST ===================== #
# clear() removes all elements from list

# mylist.clear()
# print(mylist)



# ===================== TYPECAST STRING INTO LIST ===================== #
# list() converts iterable into list

# name="Manohar"
# print(name)

# myname=list(name)
# print(myname)

# Working:
# Every character becomes separate list element



# ===================== SORTING ===================== #
# sort() arranges values in ascending order by default

# mylist=[33,5,6,66,77,2]

# mylist.sort(reverse=True)

# print(mylist)

# reverse=True -> Descending order



# ===================== ALIASING ===================== #
# Aliasing means assigning same object reference to another variable

# mylist=[33,5,6,66,77,2]

# newlist = mylist

# print(id(mylist))
# print(id(newlist))

# Working:
# Both variables point to same memory location
# Changing one list will also affect another

# Plist=[0,1,4,0,2,5]
# for i in Plist:
#     if i == 0:
#         Plist.remove(i)
#         Plist.append(i)

# print(Plist)
        

