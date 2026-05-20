import sys
# =========================================================
#                    LOOPS IN PYTHON
# =========================================================

# ---------------------------------------------------------
# FOR LOOP
# Definition:
# A for loop is used when we know how many times
# we want to repeat a task.
#
# range(start, stop)
# start = starting value
# stop  = loop runs till stop-1
# ---------------------------------------------------------

# i = 1

# for i in range(0, 5):
#     i += 1                 # Increase value of i by 1
#     print(i)               # Print updated value

# print("------------------")


# ---------------------------------------------------------
# WHILE LOOP
# Definition:
# A while loop runs until the given condition becomes False.
# It is mostly used when the number of iterations is unknown.
# ---------------------------------------------------------

# i = 1                      # Initial value

# while i <= 5:              # Condition
#     print(i)               # Print value of i
#     i += 1                 # Increment value of i


# =========================================================
#                  USER DEFINED FUNCTION
# =========================================================

# Definition:
# A function is a block of reusable code that performs
# a specific task.
#
# Syntax:
# def function_name():
#     code
#
# To execute the function, we need to call it.
# ---------------------------------------------------------

# def hello():
#     print("Hello Manohar, you are smart")

# hello()                    # Function call
# hello()                    # Function can be called multiple times


# =========================================================
#        FUNCTION RETURNING MULTIPLE VALUES
# =========================================================

# Definition:
# In Python, a function can return multiple values at once.
# The returned values are stored inside a tuple.
# ---------------------------------------------------------

# def arithmatic():

#     # Taking input from user
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))

#     # Arithmetic operations
#     sum = a + b
#     sub = a - b
#     multi = a * b
#     div = a / b

#     # Returning multiple values
#     return sum, sub, div, multi


# Function call
# R = arithmatic()

# Print returned values
# print(R)


# =========================================================
#      TYPES OF ARGUMENTS IN PYTHON FUNCTIONS
# =========================================================

# 1. Positional Argument
# 2. Keyword Argument
# 3. Default Argument
# 4. Variable Length Argument


# =========================================================
# 1. POSITIONAL ARGUMENT
# =========================================================

# Definition:
# Values are passed according to their position/order.
# The order of arguments is important.
# ---------------------------------------------------------

# def arithmatic(a, b):

#     sum = a + b
#     sub = a - b
#     multi = a * b
#     div = a / b

#     return sum, sub, multi, div


# Function call with positional arguments
# Result = arithmatic(5, 2)

# print(Result)


# =========================================================
# 2. KEYWORD ARGUMENT
# =========================================================

# Definition:
# Arguments are passed using parameter names.
# Order does not matter here.
# ---------------------------------------------------------

# def credential(username, password):

#     if username == password:
#         print("Login Successfully")
#     else:
#         print("Invalid Password")


# Keyword arguments
# Important:
# Parameter names must match correctly.
# credential(username="admin", password="admin")


# =========================================================
# 3. DEFAULT ARGUMENT
# =========================================================

# Definition:
# A default value is automatically used if
# no argument is passed during function call.
# ---------------------------------------------------------

# def cityname(city="Pune"):

#     print(city)


# Passing custom values
# cityname("Nagpur")
# cityname("Mumbai")

# No argument passed,
# so default value "Pune" will be used
# cityname()


# =========================================================
# 4. VARIABLE LENGTH ARGUMENT
# =========================================================

# Definition:
# Used when we do not know how many arguments
# will be passed to the function.
#
# *args collects all values into a tuple.
# ---------------------------------------------------------

# def cityName(*Name):

#     print(Name)


# Passing multiple arguments
# cityName("MP", "Delhi", "Nagpur", "Pune")

# =========================================================
#            MODULARITY APPROACH IN FUNCTION
# =========================================================

# Definition:
# Modularity means dividing a large program into
# smaller independent parts (functions/modules).
#
# Benefits of Modularity:
# 1. Code becomes easy to understand
# 2. Code can be reused
# 3. Debugging becomes simple
# 4. Program looks clean and organized
#
# In this program:
# Each arithmetic operation is created
# as a separate function.
# =========================================================


# ---------------------------------------------------------
# FUNCTION FOR ADDITION
# ---------------------------------------------------------

# def add():

#     # Taking input from user
#     a = int(input("Enter value of A: "))
#     b = int(input("Enter value of B: "))

#     # Performing addition
#     print(a + b)



# ---------------------------------------------------------
# FUNCTION FOR SUBTRACTION
# ---------------------------------------------------------

# def sub():

#     # Taking input from user
#     a = int(input("Enter value of A: "))
#     b = int(input("Enter value of B: "))

#     # Performing subtraction
#     print(a - b)



# ---------------------------------------------------------
# FUNCTION FOR MULTIPLICATION
# ---------------------------------------------------------

# def multi():

#     # Taking input from user
#     a = int(input("Enter value of A: "))
#     b = int(input("Enter value of B: "))

#     # Performing multiplication
#     print(a * b)



# ---------------------------------------------------------
# FUNCTION FOR DIVISION
# ---------------------------------------------------------

# def div():

#     # Taking input from user
#     a = int(input("Enter value of A: "))
#     b = int(input("Enter value of B: "))

#     # Performing division
#     print(a / b)



# =========================================================
#                    MAIN PROGRAM
# =========================================================

# while True:

#     # Displaying menu options
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")


#     # Taking user choice
#     choice = int(input("Enter Your Choice: "))


#     # Calling functions according to user choice

#     if choice == 1:
#         add()

#     elif choice == 2:
#         sub()

#     elif choice == 3:
#         multi()

#     elif choice == 4:
#         div()

#     elif choice == 5:

#         # Exit from program
#         print("Program Terminated")
#         exit()

#     else:

#         # If user enters wrong choice
#         print("Enter Valid Input")

# =========================================================
#                    DSA (DATA STRUCTURES)
# =========================================================

# Definition:
# Data Structures are different ways of organizing
# and storing data in a computer so that it can be
# accessed and used efficiently.
#
# DSA = Data Structures + Algorithms
#
# Examples of Data Structures:
# 1. Array
# 2. Linked List
# 3. Stack
# 4. Queue
# 5. Tree
# 6. Graph
#
# Why DSA is Important?
# 1. Improves problem-solving skills
# 2. Helps write optimized code
# 3. Reduces time and memory usage
# 4. Important for interviews and development
# =========================================================



# =========================================================
#                    TIME COMPLEXITY
# =========================================================

# Definition:
# Time Complexity is used to measure how much time
# an algorithm takes to run as the input size increases.
#
# It is represented using Big O notation.
# =========================================================



# =========================================================
#                    BIG O NOTATION
# =========================================================

# Definition:
# Big O represents the WORST CASE complexity
# of an algorithm.
#
# It tells us the maximum time an algorithm
# can take to execute.
#
# Example:
# Searching an element in an unsorted array.
# Worst case -> element found at last index.
# =========================================================



# =========================================================
#                    BIG OMEGA (Ω)
# =========================================================

# Definition:
# Big Omega represents the BEST CASE complexity
# of an algorithm.
#
# It tells us the minimum time an algorithm
# can take to execute.
#
# Example:
# Searching an element in an array.
# Best case -> element found at first index.
# =========================================================



# =========================================================
#                    BIG THETA (Θ)
# =========================================================

# Definition:
# Big Theta represents the AVERAGE CASE complexity.
#
# It lies between the best case and worst case.
#
# It gives the exact bound of complexity.
# =========================================================



# =========================================================
#              TYPES OF TIME COMPLEXITIES
# =========================================================

# Complexity      Name               Example
# ---------------------------------------------------------
# O(1)            Constant           Accessing array element
# O(N)            Linear             Traversing array
# O(Log N)        Logarithmic        Binary Search
# O(N^2)          Quadratic          Nested loops
# O(2^N)          Exponential        Fibonacci recursion



# =========================================================
#                    O(1) COMPLEXITY
# =========================================================

# Definition:
# O(1) means CONSTANT TIME complexity.
#
# The execution time does not depend
# on the size of input.
#
# Example:
# Accessing an element using index in array.
# =========================================================

# array = [1, 2, 3, 4, 5]

# Accessing first element
# This operation takes constant time
# array[0]

# =========================================================
#              TIME COMPLEXITY EXAMPLES
# =========================================================

# Time Complexity tells us how the execution time
# increases when the input size increases.
#
# Below are some common complexities with examples.
# =========================================================



# =========================================================
#                    O(N) - LINEAR TIME
# =========================================================

# Definition:
# O(N) means the algorithm runs proportional
# to the input size.
#
# If the number of elements increases,
# execution time also increases linearly.
#
# Example:
# Traversing all elements of an array.
# =========================================================

# array = [1, 2, 3, 4, 5]

# Loop through every element
# The loop runs N times
# where N = number of elements in array

# for elements in array:
#     print(elements)



# =========================================================
#              O(Log N) - LOGARITHMIC TIME
# =========================================================

# Definition:
# O(Log N) means the input size decreases
# after every step.
#
# These algorithms are very fast for large data.
#
# Common Example:
# Binary Search Algorithm
#
# Note:
# Your example below skips elements using step = 3.
# It demonstrates fewer operations,
# but Binary Search is the actual
# logarithmic-time algorithm.
# =========================================================

# array = [1, 2, 3, 4, 5]

# Accessing elements with gaps
# Fewer operations compared to linear traversal

# for index in range(0, len(array), 3):
#     print(array[index])
# example binary Search


# =========================================================
#              O(N^2) - QUADRATIC TIME
# =========================================================

# Definition:
# O(N^2) occurs when we use nested loops.
#
# If input increases,
# operations increase very rapidly.
#
# This complexity is mostly avoided
# for large datasets because it is slow.
# =========================================================

# array = [1, 2, 3, 4, 5]

# Outer loop runs N times
# Inner loop also runs N times
#
# Total operations = N * N = N^2

# for x in array:
#     for y in array:
#         print(x, y)



# =========================================================
#            O(2^N) - EXPONENTIAL TIME
# =========================================================

# Definition:
# Exponential complexity grows very fast.
#
# These algorithms become extremely slow
# for large inputs.
#
# Common Example:
# Recursive Fibonacci Series
# =========================================================

# def fibonacci(n):

#     # Base condition
#     if n <= 1:
#         return n

#     # Recursive calls
#     return fibonacci(n - 1) + fibonacci(n - 2)

# =========================================================
#               FIND BIGGEST NUMBER IN ARRAY
# =========================================================

# Problem Statement:
# Find the largest element from the given array.
#
# Example:
# Input  : [5, 7, 9, 2, 3, 4]
# Output : 9
# =========================================================



# =========================================================
#                    FUNCTION DEFINITION
# =========================================================

# Function Name:
# findBggestNumber()
#
# Purpose:
# This function finds the biggest number
# present in the given array.
# =========================================================

# def findBggestNumber(sampleArray):

#     # Assume first element is the biggest
#     biggestNumber = sampleArray[0]

#     # Loop starts from index 1
#     # because index 0 is already stored
#     # in biggestNumber

#     for index in range(1, len(sampleArray)):

#         # Compare current element
#         # with biggestNumber

#         if sampleArray[index] > biggestNumber:

#             # Update biggest number
#             biggestNumber = sampleArray[index]

#     # Print final biggest number
#     print(biggestNumber)



# =========================================================
#                    DRIVER CODE
# =========================================================

# Creating sample array
# sampleArray = [5, 7, 9, 2, 3, 4]

# Function call
# findBggestNumber(sampleArray)



# =========================================================
#                    WORKING OF CODE
# =========================================================

# Step-by-step execution:
#
# Initial:
# biggestNumber = 5
#
# Compare 7 > 5  -> True
# biggestNumber = 7
#
# Compare 9 > 7  -> True
# biggestNumber = 9
#
# Compare 2 > 9  -> False
#
# Compare 3 > 9  -> False
#
# Compare 4 > 9  -> False
#
# Final Output:
# 9
# =========================================================



# =========================================================
#                    TIME COMPLEXITY
# =========================================================

# O(N)
#
# Because the loop traverses
# the entire array once.
# =========================================================



# =========================================================
#                    SPACE COMPLEXITY
# =========================================================

# O(1)
#
# Because no extra array or
# large memory is used.
# =========================================================

# Homework
#Linear Search 

# def linearSerach(array, target):
#     for i in range(0,len(array)):
#         if array[i] == target:
#             return i
#     print("Result not found")

# array =[1,2,3,4,5,6,7,9,33,5,77,8]

# target = 8
# print(linearSerach(array,target))

# removing spaces from thes string 
# 1. rstrip() ==> to remove spaces at right
# 2. lstrip() ==> to remove spaces at left hand side
# 3. strip() ==> to remove spaces both sides

city= input("Enter your city Name:")
scity = city.strip()
if scity =="Hyderabad":
    print("Hello Hyderabadi.. adab")
elif scity =="Chennai":
    print("Hello Madrasi.. adab")
elif scity =="Bangalore":
    print("Hello kannadiga.. adab")
else:
    print("Your Entered city is invalid")