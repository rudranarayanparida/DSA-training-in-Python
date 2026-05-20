# ===================== ARRAY & LIST PRACTICE QUESTIONS ===================== #

# ========================================================================== #
# Q1. FIND THE SECOND LARGEST ELEMENT IN ARRAY
# ========================================================================== #

# Definition:
# Second Largest Element means the number which is smaller than the largest
# number but greater than all remaining numbers in the array.

# Example:
# Array = [7,3,9,2,8]
# Largest Number = 9
# Second Largest = 8

# input =[ 7,3,9,2,8]
# SL=input[0]

# for i in input:
#     if input[i]

# Incomplete Logic
# "bakwas question" because logic is unfinished



# ========================================================================== #
# Q2. LIST SLICING & VALUE REPLACEMENT
# ========================================================================== #

# Definition:
# Slicing is used to access or modify specific portions of a list.

# a= [1,2,3,4,5,6,7,8,9]

# a[0::2] means:
# Start from index 0
# Go till end
# Jump by 2 positions

# So indexes selected are:
# 0,2,4,6,8

# a[0::2]=10,20,30,40,50,60
# print(a)

# Working:
# Even index values are replaced with new values

# NOTE:
# Number of replacement values must match selected positions



# ===================== REVERSE SLICING ===================== #

# a= [1,2,3,4,5]

# print(a[3:0:-1])

# Working:
# Start from index 3 -> value 4
# Stop before index 0
# Move backward by -1

# Output:
# [4,3,2]



# ========================================================================== #
# Q3. POP ELEMENTS FROM 2D ARRAY
# ========================================================================== #

# Definition:
# 2D Array means list inside another list
# Also called Matrix or Nested List

# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]

# for i in range(0,4):
#     print(arr[i].pop())

# Working:
# pop() removes last element from each row

# Iteration Details:
# Row 1 -> removes 4
# Row 2 -> removes 7
# Row 3 -> removes 11
# Row 4 -> removes 15

# Output:
# 4
# 7
# 11
# 15



# ========================================================================== #
# Q4. LEFT SHIFT ARRAY ELEMENTS
# ========================================================================== #

# Definition:
# Left Shift means moving every element one position toward left side.

# arr=[1,2,3,4,5,6]

# for i in range (1,6):

#     # Current value copied into previous position
#     arr[i-1] = arr[i]

# for i in range(0,6):
#     print(arr[i], end =" ")

# Step-by-step Working:
#
# Initial Array:
# [1,2,3,4,5,6]
#
# After shifting:
# [2,3,4,5,6,6]

# Why last 6 repeated?
# Because last index value never changed.
# Only indexes 0 to 4 were modified.



# ========================================================================== #
# Q5. LIST COPYING & ALIASING
# ========================================================================== #

# Definition:
# Aliasing means two variables point to same memory location.
# Copying creates separate memory location.

# Fruit_list1=['apple',berry,'cherry','papaya']

# Fruit_list2 = Fruit_list1

# Working:
# Fruit_list2 is alias of Fruit_list1
# Changes in one list affect another list

# Fruit_list3 = Fruit_list1[:]

# Working:
# [:] creates shallow copy
# Fruit_list3 becomes independent copy



# ========================================================================== #
# Q6. FIND COMMON ELEMENTS IN THREE ARRAYS
# ========================================================================== #

# Definition:
# Common Elements are values present in all arrays.

# A = [1,2,3,4]
# B = [2,3,4]
# C = [3,4,5]

# for i in A:

#     # Check if element exists in all arrays
#     if i in B and i in C:

#         print(i)

# Working:
# Iterates through Array A
# Checks whether element is present in B and C

# Output:
# 3
# 4



# ========================================================================== #
# Q7. SUM OF DISTANCE BETWEEN ADJACENT ELEMENTS
# ========================================================================== #

# Question:
# Write a program to calculate and return the sum of distances
# between adjacent numbers in an array of positive integers.

# Definition:
# Adjacent Elements means neighboring elements in array.

# Example:
# Array = [1,4,7]
#
# Distance Calculation:
# |1-4| = 3
# |4-7| = 3
#
# Total Distance = 6

# ========================================================================== #
# PROGRAM STARTS HERE
# ========================================================================== #

# Taking number of elements from user
N = int(input("Enter the Number of elements: "))

# Empty list created to store user values
mylist = []

# ========================================================================== #
# INPUT SECTION
# ========================================================================== #

# Loop runs N times for taking input
for i in range(N):

    # Taking integer value from user
    val = int(input("Enter the values: "))

    # append() adds value at end of list
    mylist.append(val)

# ========================================================================== #
# DISTANCE CALCULATION
# ========================================================================== #

# Variable to store final answer
total = 0

# len(mylist)-1 because we compare current element with next element
for i in range(len(mylist) - 1):

    # abs() converts negative value into positive
    # Formula:
    # |a-b|

    total += abs(mylist[i] - mylist[i + 1])

# ========================================================================== #
# OUTPUT SECTION
# ========================================================================== #

# Display final total distance
print("Total Distance =", total)



# ========================================================================== #
# EXAMPLE EXECUTION
# ========================================================================== #

# Input:
# 5
# 1
# 3
# 6
# 10
# 15

# Calculation:
# |1-3|  = 2
# |3-6|  = 3
# |6-10| = 4
# |10-15| = 5

# Total:
# 2 + 3 + 4 + 5 = 14

# Output:
# Total Distance = 14