# # Q. input = aaabbbbccceeeee
#     #  output= a3b4c3e5
import sys

# name= 'aaabbbbccceeeee'
# newname={}
# for i in range(len(name)):
#     key = name[i]
#     count =0 
#     for j in range(len(name)):
#         if key == name [j]:
#             count +=1
#     newname[key] = count

#     print(newname)
#     for i , j in newname.items():
#         print(i,j, sep='',end='')


# # Q.  
# salary = int (input("Enter your salary: "))
# rating = int(input("Enter your perforance appraisal rating : "))
# increment = 0 
# if rating >= 1 and rating <=3:
#     increment = salary*10/100
# elif rating >= 3.1 and rating <=4:
#     increment = salary*30/100
# elif rating >= 4.1 and rating <=5:
#     increment = salary*40/100
# else:
#     print("Invalid Rating")
# print("Incremented salary" , increment + salary)


# #class work
# basciSalary = 20000

# so we have to calculate the 
# HRA of basicSalary = 20 %
# TA of BasicSalary = 30%
# DA of BasicSalary = 45%

# calculate GrossSalary  =?

# def Grossfun(basciSalary):
#     HRA = (basciSalary * 20 )/ 100
#     TA  = (basciSalary * 30 )/100
#     DA  = (basciSalary * 45 )/100

#     return basciSalary + HRA + TA + DA

# basciSalary = int(input ("Enter Salary : "))
# print(Grossfun(basciSalary))



input = input("Enter the Data: ")

def RepeatedDigits(input):

    repeated = set()

    for i in range(len(input)):

        for j in range(i + 1, len(input)):

            if input[i] == input[j]:
                repeated.add(input[i])

    return len(repeated)

print(RepeatedDigits(input))




print("Select any choice")
print("Enter student ID:")
print("Enter Student Roll No:")
print("Enter Student Name:")
print("Enter Student city:")


class CRUD:
    def __init__(self):
        
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
    print("1. ADD Student: ")
    print("2. Show Student : ")
    print("3. Update Student : ")
    print("4. Delete Student: ")
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


# # add student 
# show student 
# update student 
# delete student
# exit


# 572378233 3
