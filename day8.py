# full binary tree

# each node has either 0 or 2 children
# no node has a single child

# complete binary tree
# all levels except possibly the last are completely filled 
# nodes in the last level are filled from left to right


# perfect binary tree
# all internal nodes have extely filled same

# Binary search tree
# Binary search tree

# class BSTNode:
#     def __init__(self,data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

# def insertNode(rootNode, NodeValue):
#     if rootNode.data == None:
#         rootNode.data = NodeValue

#     elif NodeValue <= rootNode.data:
#         if rootNode.leftchild is None:
#             rootNode.leftchild = BSTNode(NodeValue)
#         else:
#             insertNode(rootNode.leftchild, NodeValue)
            
#     else:
    
#         if rootNode.rightchild is None:
#             rootNode.rightchild = BSTNode(NodeValue)
#         else:
#             insertNode(rootNode.rightchild, NodeValue)

# def SearchNode(rootNode, NodeValue):
#     if rootNode is None:
#         print("Value not found")
#         return
    
#     if rootNode.data == NodeValue:
#         print("VAlue found")

#     elif NodeValue < rootNode.data:
#         if rootNode.leftchild.data == NodeValue:
#             print("VAlue found on left side")
#         else:
#             SearchNode(rootNode.leftchild, NodeValue)
#     else:
#         if rootNode.rightchild.data==NodeValue:
#             print("The value is found on Right side")
#         else:
#             SearchNode(rootNode.rightchild, NodeValue)
    


# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
        
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftchild)
#     preOrderTraversal(rootNode.rightchild)


# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
        
#     postOrderTraversal(rootNode.leftchild)
#     postOrderTraversal(rootNode.rightchild)
#     print(rootNode.data)

# def InOrderTraversal(rootNode):
#     if not rootNode:
#         return
        
#     InOrderTraversal(rootNode.leftchild)
#     print(rootNode.data)
#     InOrderTraversal(rootNode.rightchild)


# newBST = BSTNode(None)

# insertNode(newBST,70)
# insertNode(newBST,50)
# insertNode(newBST,90)
# insertNode(newBST,30)
# insertNode(newBST,60)
# insertNode(newBST,80)
# insertNode(newBST,100)
# insertNode(newBST,20)
# insertNode(newBST,40)
# insertNode(newBST,10)

# print("PreOrder Traveral")
# preOrderTraversal(newBST)
# print("PostOrder Traveral")
# postOrderTraversal(newBST)
# print("InOrder Traveral")
# InOrderTraversal(newBST)

# print("Seach Node")
# SearchNode(newBST,100)


# exceptionn handling

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter Second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't devide by zero")
# except ValueError:
#     print("Enter only integer values")
# except:
#     print("Something went wrong")
# else:
#     print("Everthing is Ok")
# finally:
#     print("Program terminated")

# # advance form
# import logging
# logging.basicConfig(filename="newfile.txt", level = logging.DEBUG )
# try:
#     a= int(input("Enter first number : "))
#     b= int(input("Enter second number: "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)
#     logging.exception(msg)
# print("Logging level is set up . check 'newfile.text' for log details " )


import csv
f= open('employee.csv','a')
a = csv.writer(f)
# a.writerow(["EmpID","Emp Name","Emp Age"])
empid=int(input("Enter your empid: "))
empName=input("Enter your Employee Name: ")
Age=int(input("Enter your Employee Age: "))
a.writerow([empid,empName,Age])
print("Files has Created")

import csv
f = open ("classwork.csv",'a')
a = csv.writer(f)
# a.writerow(["studId","StudName","phy","chem","math","total","percentage","Result"])


SId=int(input("Enter your Student ID: "))
SName=input("Enter your Student Name: ")
Mphy=int(input("Enter your marks in Physic: "))
Mchem=int(input("Enter your marks in chem: "))
Mmath=int(input("Enter your marks in math: "))

total = Mphy + Mchem + Mmath
percentage = (total / 300) *100
if Mphy >= 40 and Mchem >= 40 and Mchem >= 40:
    result = "Pass"
else: 
    result= "Fail"

a.writerow([SId,SName,Mphy,Mchem,Mmath,total,percentage,result])
print("Files has Created")
