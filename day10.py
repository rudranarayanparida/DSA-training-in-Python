# # # # # # # # # import re #re module for performing all the regular expression based operation
# # # # # # # # # count=0
# # # # # # # # # pattern=re.compile("function")


# # # # # # # # # matcher=pattern.finditer("A function in python is defined by  def statementin python The general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists. ")

# # # # # # # # # for i in matcher:
# # # # # # # # #     count +=1
# # # # # # # # #     print(i.start(), "...", i.end(), "...", i.group())
# # # # # # # # # print("The number of occurrences: ", count)

# # # # # # # # #====================================================================================

# # # # # # # # import re
# # # # # # # # count=0
# # # # # # # # matcher=re.finditer("Hi", "HiHiHiHi")

# # # # # # # # for i in matcher:
# # # # # # # #     count+=1
# # # # # # # #     print(i.start(), "...", i.end(), "...", i.group())
# # # # # # # # print("The number of occurrences: ", count)

# # # # # # # # #====================================================================================

# # # # # # # import re
# # # # # # # obj=input("Enter any character: ") #7
# # # # # # # objmatch=re.finditer(obj, "ab7 @k9z")
# # # # # # # #print(objmatch)
# # # # # # # for match in objmatch:
# # # # # # #     print(match.start(), "...", match.end(), "...", match.group())

# # # # # # # #====================================================================================

# # # # # # import re
# # # # # # a = input("Enter string to perform match operation: ")
# # # # # # mtch= re.match(a, "Python is very important language")
# # # # # # print(mtch)

# # # # # # if mtch!=None:
# # # # # #     print("Match found at beginning level")
# # # # # #     print(mtch.start()," ",mtch.end())
# # # # # # else:
# # # # # #     print("There is no matching at beginning level")

# # # # # # #====================================================================================

# # # # # import re
# # # # # a = input("Enter string to perform match operation: ")
# # # # # mtch= re.fullmatch(a, "Python is very important language")
# # # # # print(mtch)

# # # # # if mtch!=None:
# # # # #     print("Match found")
# # # # #     print(mtch.start()," ",mtch.end())
# # # # # else:
# # # # #     print("Full match not found")

# # # # # #====================================================================================

# # # # #Write a Python Program to check whether the given mail is valid gmail id or not ?

# # # # # import re
# # # # # s=input("Enter mail id: ")
# # # # # m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# # # # # if m!=None:
# # # # #     print("Valid e-mail id")
# # # # # else:
# # # # #     print("Invalid e-mail id")

# # # # import re
# # # # s=input("Enter mail id: ")
# # # # m=re.fullmatch("\w[a-zA-Z0-9_.]*@rbunagpur[.]in", s)
# # # # if m!=None:
# # # #     print("Valid e-mail id")
# # # # else:
# # # #     print("Invalid e-mail id")

# # # # #====================================================================================

# # # #WAP to check the valid mobile number

# # # import re
# # # mo=input("Enter mobile number: ")
# # # obj=re.fullmatch("[0-9]\d{9}", mo)

# # # if obj!=None:
# # #     print("Valid mobile number")
# # # else:
# # #     print("Invalid mobile number")

# # # #====================================================================================

# # #search() function
# # import re
# # a=input("Enter string to perform match operation: ")
# # mtch=re.search(a, "Python sss dynamic lannn")
# # print(mtch)
# # if mtch!=None:
# #     print(mtch.start()," ", mtch.end(), " ", mtch.group())
# # else:
# #     print("There is no matching anywhere")

# # #====================================================================================

# #findall()

# import re
# mtch = re.findall('[A-Z]', "abch3hdh5bk7ZQ$&*")
# print(mtch)

# #====================================================================================

