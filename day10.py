# # # # # # # # # # # # # # import re #re module for performing all the regular expression based operation
# # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # pattern=re.compile("function")


# # # # # # # # # # # # # # matcher=pattern.finditer("A function in python is defined by  def statementin python The general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists. ")

# # # # # # # # # # # # # # for i in matcher:
# # # # # # # # # # # # # #     count +=1
# # # # # # # # # # # # # #     print(i.start(), "...", i.end(), "...", i.group())
# # # # # # # # # # # # # # print("The number of occurrences: ", count)

# # # # # # # # # # # # # #====================================================================================

# # # # # # # # # # # # # import re
# # # # # # # # # # # # # count=0
# # # # # # # # # # # # # matcher=re.finditer("Hi", "HiHiHiHi")

# # # # # # # # # # # # # for i in matcher:
# # # # # # # # # # # # #     count+=1
# # # # # # # # # # # # #     print(i.start(), "...", i.end(), "...", i.group())
# # # # # # # # # # # # # print("The number of occurrences: ", count)

# # # # # # # # # # # # # #====================================================================================

# # # # # # # # # # # # import re
# # # # # # # # # # # # obj=input("Enter any character: ") #7
# # # # # # # # # # # # objmatch=re.finditer(obj, "ab7 @k9z")
# # # # # # # # # # # # #print(objmatch)
# # # # # # # # # # # # for match in objmatch:
# # # # # # # # # # # #     print(match.start(), "...", match.end(), "...", match.group())

# # # # # # # # # # # # #====================================================================================

# # # # # # # # # # # import re
# # # # # # # # # # # a = input("Enter string to perform match operation: ")
# # # # # # # # # # # mtch= re.match(a, "Python is very important language")
# # # # # # # # # # # print(mtch)

# # # # # # # # # # # if mtch!=None:
# # # # # # # # # # #     print("Match found at beginning level")
# # # # # # # # # # #     print(mtch.start()," ",mtch.end())
# # # # # # # # # # # else:
# # # # # # # # # # #     print("There is no matching at beginning level")

# # # # # # # # # # # #====================================================================================

# # # # # # # # # # import re
# # # # # # # # # # a = input("Enter string to perform match operation: ")
# # # # # # # # # # mtch= re.fullmatch(a, "Python is very important language")
# # # # # # # # # # print(mtch)

# # # # # # # # # # if mtch!=None:
# # # # # # # # # #     print("Match found")
# # # # # # # # # #     print(mtch.start()," ",mtch.end())
# # # # # # # # # # else:
# # # # # # # # # #     print("Full match not found")

# # # # # # # # # # #====================================================================================

# # # # # # # # # #Write a Python Program to check whether the given mail is valid gmail id or not ?

# # # # # # # # # # import re
# # # # # # # # # # s=input("Enter mail id: ")
# # # # # # # # # # m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# # # # # # # # # # if m!=None:
# # # # # # # # # #     print("Valid e-mail id")
# # # # # # # # # # else:
# # # # # # # # # #     print("Invalid e-mail id")

# # # # # # # # # import re
# # # # # # # # # s=input("Enter mail id: ")
# # # # # # # # # m=re.fullmatch("\w[a-zA-Z0-9_.]*@rbunagpur[.]in", s)
# # # # # # # # # if m!=None:
# # # # # # # # #     print("Valid e-mail id")
# # # # # # # # # else:
# # # # # # # # #     print("Invalid e-mail id")

# # # # # # # # # #====================================================================================

# # # # # # # # #WAP to check the valid mobile number

# # # # # # # # import re
# # # # # # # # mo=input("Enter mobile number: ")
# # # # # # # # obj=re.fullmatch("[0-9]\d{9}", mo)

# # # # # # # # if obj!=None:
# # # # # # # #     print("Valid mobile number")
# # # # # # # # else:
# # # # # # # #     print("Invalid mobile number")

# # # # # # # # #====================================================================================

# # # # # # # #search() function
# # # # # # # import re
# # # # # # # a=input("Enter string to perform match operation: ")
# # # # # # # mtch=re.search(a, "Python sss dynamic lannn")
# # # # # # # print(mtch)
# # # # # # # if mtch!=None:
# # # # # # #     print(mtch.start()," ", mtch.end(), " ", mtch.group())
# # # # # # # else:
# # # # # # #     print("There is no matching anywhere")

# # # # # # # #====================================================================================

# # # # # # #findall()

# # # # # # import re
# # # # # # mtch = re.findall('[A-Z]', "abch3hdh5bk7ZQ$&*")
# # # # # # print(mtch)

# # # # # # #====================================================================================

# # # # # #sub() function
# # # # # import re
# # # # # obj = re.sub('[a-z]','*', '2345 ABCD habc deff')
# # # # # print(obj)

# # # # # #====================================================================================

# # # # import re
# # # # obj=re.subn('[0-7]', '@', 'ab3gd6nkl7')
# # # # print(obj)
# # # # print("The string is= ", obj[0])
# # # # print("The number of replacement is= ", obj[1])

# # # # #====================================================================================

# # # import re
# # # f1=open("demo.txt", "r")
# # # f2=open("demooutput", "w")
# # # for line in f1:
# # #     obj=re.sub('Today',"Tomorrow", line)
# # #     f2.write(obj)
# # # f1.close()
# # # f2.close()

# # # #====================================================================================

# # # Program to print the number of lines, words and characters present in the given file

# # import os, sys

# # fname = input("Enter File Name: ")

# # if os.path.isfile(fname):
# #     print("File exists:", fname)
# #     f = open(fname, "r")
# # else:
# #     print("File does not exist:", fname)
# #     sys.exit(0)

# # lcount = wcount = ccount = 0

# # for line in f:
# #     lcount = lcount + 1
# #     ccount = ccount + len(line)

# #     words = line.split()
# #     wcount = wcount + len(words)

# # print("The number of Lines:", lcount)
# # print("The number of Words:", wcount)
# # print("The number of Characters:", ccount)

# # #====================================================================================

# # Consider this graph:

# #         A ---- B
# #         |      |
# #         |      |
# #         C ---- D

# # Connections:
# # * A ↔ B
# # * A ↔ C
# # * B ↔ D
# # * C ↔ D

# # # Adjacency Matrix Representation

# # |   | A | B | C | D |
# # |---|---|---|---|---|
# # | A | 0 | 1 | 1 | 0 |
# # | B | 1 | 0 | 0 | 1 |
# # | C | 1 | 0 | 0 | 1 |
# # | D | 0 | 1 | 1 | 0 |


# class Graph:
#     def __init__(self, vertices):
#         #Total number of vertices
#         self.V = vertices #4

#         #Create adjancey matrix with all 0s
#         self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

#     #add edge between two vertices

#     def add_edge(self,u,v): #(0,1)
#         self.matrix[u][v]=1
#         self.matrix[v][u]=1 #for undirected graph

#     #Remove edge
#     def remove_edge(self,u,v):
#         self.matrix[u][v]=0
#         self.matrix[v][u]=0
    
#     #display matrix

#     def display(self):
#         for row in self.matrix:
#             print(row)

# #Create graph with 4 vertices
# g = Graph(4)

# #Add edges
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)

# g.display()
# print("Removed edges")
# g.remove_edge(1,3)
# g.display()

# #====================================================================================

