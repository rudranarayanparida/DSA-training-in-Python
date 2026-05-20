import sys
# #  Binary Search

# arr = [ 2,3,4,5,6,7,8,9,10,12,14,16,18,20,22,24,26,28]
# target = 16

# def Binary(arr,target):
#     start = 0
#     end = len(arr)-1
#     while start  <= end:
#         mid = (start + end) // 2

#         if arr[mid] > target:
#             end = mid - 1
#         elif arr[mid] < target:
#             start = mid + 1
#         elif arr[mid] == target:
#             return mid
#         else:
#             print("Target Not Present in Array")

# print(target)
# print(Binary(arr,target))
        

# # Booble Sort
# arr=[ 2,4,45,6,67,3,44,66,33,66,22,66,22,66,22,5,77,875,4]
# passcount = 0

# def bubbleSort(arr):
#     for i in range(len(arr)-1):
      
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1]=temp
#             print(arr)
#         print("")
#     return arr
# print("original array" ,arr)

# print(bubbleSort(arr))   
# print(passcount)

# Q.
# input = input("Enter the Data: ")

# def RepeatedDigits(input):

#     repeated = set()

#     for i in range(len(input)):

#         for j in range(i + 1, len(input)):

#             if input[i] == input[j]:
#                 repeated.add(input[i])

#     return len(repeated)

# print(RepeatedDigits(input))


# # class and object

# class Name:
#     age = 30 
#     def display(self):
#         print("Hello World")
    
# obj = Name()
# print(obj.age)
# obj.display()

# class Message:
#     def __init__(self):
#         print("I am Constructor")

#     def shows(self):
#         print("Class Program")

# obj= Message()
# obj.shows()
# obj2=Message()

# class StudentInfo:
#     def __init__(self, name , age,roll_no):
#         self.Name = name
#         self.age = age
#         self.RollNo = roll_no

#     def DisplayStudentInfo(self):
#         print("Name = ",self.Name)
#         print("Age = ",self.age)

# studentObj= StudentInfo("Manohar",22,1011)
# studentObj.DisplayStudentInfo()


# Stack implelmentation without size limit
# Stack implementation

class Stack:
    def __init__(self,size):
        self.myStack=[]
        self.stackSize= size
    
    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            False
   
    def push(self,value):
        if self.isFull() :
            print("Stack is Full ")
        else:
            self.myStack.append(value)
            print("Element push")

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack.pop())
        
    def Display(self):
        print(self.myStack)

    def peek(self):
        if self.isEmpty():
            print("STack is Empty")
        else:
            print(self.myStack[-1])

size = int(input("Enter the size of stack"))
obj=Stack(size)
print("Stack has Created: ")
while True:
    print("1. Push Operation: ")
    print("2. Display Stack: ")
    print("3. Pop Operation: ")
    print("4. Peek Operation: ")
    print("7. Exit: ")
    choice = int (input("Enter your choice: "))
    if choice ==1 :
        value = int (input("Enter value to push in stack :"))
        obj.push(value)
    elif choice ==2:
        obj.Display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    else:
        sys.exit()


# 572378233 3
