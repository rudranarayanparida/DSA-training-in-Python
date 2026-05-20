# sorting
# insertion sort

# arr=[22,4,55,66,7,5,33,2,44,8,89]
# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


# print(arr)
# insertionSort(arr)
# print("Insertion Sort : ",arr)


#Selection Sort

# def SelectionSort(arr):
#     for i in range(len(arr)):
#         min = i 
#         j = i +1


#         while j<len(arr):
#             if arr[j]<arr[min]:
#                 min = j
#             j = j +1
#         arr[i],arr[min]= arr[min], arr[i]
            
# SelectionSort(arr)
# print("Selection Sort : ",arr)


# sort dictionary by key or value:
# Write a function to sort a dictionary by keys or values in ascending or descending order.

# types of variable static variable

# class New:
#     a =10 

#     def __init__ (self):
#         self.name="Parshant"

# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj4 = New()/

# class college:
#     collegename = "RBU"
#     def __init__ (self):
#         self.studentname = "manohar"

# principal = college()
# teacher = college()
# accountant = college()

# print("Principal : ", principal.collegename, " ..... ", principal.studentname)
# print("Teacher : ", teacher.collegename, " ..... ", teacher.studentname)
# print("Accountant : ", accountant.collegename, " ..... ", accountant.studentname)

# college.collegename="HBD"
# principal.studentname="Manohar Sharnagat"

# print("Principal : ", principal.collegename, " ..... ", principal.studentname)
# print("Teacher : ", teacher.collegename, " ..... ", teacher.studentname)
# print("Accountant : ", accountant.collegename, " ..... ", accountant.studentname)


# # Create Node class
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Create LinkedList class
# class Linkedlist:
#     def __init__(self):
#         self.head = None


# # Create linked list object
# linkedlist = Linkedlist()

# # Create nodes
# linkedlist.head = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)

# # Connect nodes

# linkedlist.head.next  = second
# second.next = third
# third.next = fourth

# while linkedlist.head:
#     print(linkedlist.head.data, "| -> ", end="")
#     linkedlist.head = linkedlist.head.next

# print("None")


# 
class Node:
    def __init__(self,data):
        self.data=data # instance variable(5)
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        self.node = Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.tail.next=self.node
            self.tail =self.node
    
    def addNodeBeginning(self,value):
        print("Add not at beginning:")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node


    def addNodeBetween(self, index, value):

        node = Node(value)

    # If linked list is empty
        if self.head is None:
            self.head = node
            self.tail = node

    # Insert at beginning
        elif index == 0:
            node.next = self.head
            self.head = node

    # Insert in between
        else:
            temp = self.head

            for _ in range(index - 1):
                temp = temp.next

            node.next = temp.next
            temp.next = node

        # If inserted at last position
        if node.next is None:
            self.tail = node

    #displaynode        
    def displayNode(self):
        while self.head is not None:
            print(self.head.data," | ")
            self.head = self.head.next
        print()
if __name__ == '__main__':
    object = linkedlist() #linkedlist object created
    #menu driven options
    while True:
        print('1.Add Node Linkedlist:')
        print('2.Add Node in begning:')
        print('3.Add Node in between:')
        print('4.Add Node in end:')
        print('5. display linked list:')
        print("6.Exit  ")
        ch = int(input("Enter your choice:"))
        if ch==1:
            value = int(input("Enter value for node:"))
            object.addNode(value)
            print('Node added succefully in single linkedlist:')
         
        elif ch==2:
            value = int(input("Enter value for node:"))
            object.addNodeBeginning(value)
            print('Node added succefully in beginning:')    

        elif ch == 3:
            index = int(input("Enter index"))
            value = int(input("Ener value of Node"))  
            object.addNodeBetween(index, value)
        elif ch==5:
            object.displayNode()
            print('Node is displayed:')