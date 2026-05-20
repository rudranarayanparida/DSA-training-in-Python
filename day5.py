# ##parameterised constructor

import sys


# class Queue:
#     def __init__(self, size):
#         self.myQueue = []
#         self.QueueSize = size

#     # Check Queue is Full or Not
#     def isFull(self):
#         if len(self.myQueue) == self.QueueSize:
#             return True
#         else:
#             return False   # Missing return statement fixed

#     # Insert Element in Queue
#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)
#             print("Element Inserted")

#     # Check Queue is Empty or Not
#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False

#     # Delete Element from Queue
#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Deleted Element:", self.myQueue.pop(0))
#             # pop(0) used because Queue follows FIFO

#     # Display Queue
#     def Display(self):
#         print("Queue:", self.myQueue)

#     # Show Front Element
#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Front Element:", self.myQueue[0])


# size = int(input("Enter the size of Queue: "))
# obj = Queue(size)

# print("Queue has been Created")

# while True:
#     print("\n1. Enqueue Operation")
#     print("2. Display Queue")
#     print("3. Delete Operation")
#     print("4. Peek Operation")
#     print("5. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value to insert in Queue: "))
#         obj.enQueue(value)

#     elif choice == 2:
#         obj.Display()

#     elif choice == 3:
#         obj.deQueue()   # pop() method corrected

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         print("Program Exited")
#         sys.exit()

#     else:
#         print("Invalid Choice")


# how to read multiple values from the keyboard in a single line:

# a,b= [int(x) for x in input("Enter 2 numbers :").split()]


# mycart= [10,20,30,40]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everting")


# R = True
# while (R ):
#     username= input("Enter user Name : ")
#     password = input("Enter Password : ")
#     if username == 'admin' and password == 'admin':
#         print("Login successful")
#         R = False
#     else:
#         print("You have Entered wrong usename and password")


import time


class Tower:

    def __init__(self):
        print("Welcome to tower of Hanoi Game")
        print()

        print("given Problem  A=[3,2,1]     B=[]        C=[]")
        print()

        print("Expected Output A=[]         B=[]        C=[3,2,1]")

        self.A = []
        self.B = []
        self.C = []

    # Insert elements in A
    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A = ", self.A)

    # PASS 1
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass One completed ==========================\n")

    # PASS 2
    def pass2(self):
        self.temp = self.A.pop(1)   # self.a corrected to self.A
        self.B.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass Two completed ==========================\n")

    # PASS 3
    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass Three completed ========================\n")

    # PASS 4
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass Four completed =========================\n")

    # PASS 5
    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass Five completed =========================\n")

    # PASS 6
    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass Six completed ==========================\n")

    # PASS 7
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)

        time.sleep(1)

        print("A = ", self.A, "   ", "B = ", self.B, "   ", "C = ", self.C)
        print("Pass Seven completed ========================\n")


# ================= MAIN =================

obj = Tower()

# Insert Disks
obj.tower(3)
obj.tower(2)
obj.tower(1)

print("\nInitial State\n")

# Execute Passes
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

print("Tower of Hanoi Solved Successfully")

