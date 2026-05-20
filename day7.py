# # Factorial Solution

# def factorial (num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(4))


# # capitalizeFirst Solution using Recursion

# def capitalizeFirst(arr):
#     result=[]
#     if len(arr) ==0 :
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','manohar sharnagat','banana']))


# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power( base , exponent-1 )


# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])
# print(productOfArray([0,1,2,3]))
# print(productOfArray([1,2,3,10]))

# reverse string using recursion
# def recursiveRange(num):
#     if num <=0:
#         return 0
#     return num + recursiveRange(num -1)

# print(recursiveRange(6))



# def ReverseSring(S):
#     # print(S)
    
#     if len(S) <= 1:
#         return S
#     return S[len(S)-1] + ReverseSring(S[0:len(S)-1])
    


# print(ReverseSring("Manohar"))


# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome("manhar"))
# print(isPalindrome("nitin"))
# print(isPalindrome("112211"))


# def Palindrome(S):

#     # Base condition
#     if len(S) <= 1:
#         return True

#     # Compare first and last character
#     if S[0] != S[-1]:
#         return False

#     # Recursive call on middle part
#     return Palindrome(S[1:-1])


# print(Palindrome("112211"))

# def someRecursive(arr,cb):
#     if len(arr) == 0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)
#     return True

# def isOdd(num) :
#     if num%2 == 0:
#         return False
#     else:
#         return True
    
# print(someRecursive([1,2,3,4], isOdd))




# tree and linkedlist

# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]

#     def __str__(self,level=0):
#         ret= "  "* level + str(self.data) + "\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret
    
#     def addChild(self,object):
#         self.child.append(object)
#         print("Tree Node Added")


# rootNode=Tree("Drink")
# Hot     = Tree("Hot")
# Cold    = Tree("Cold")
# Tea    = Tree("Tea")
# Coffee    = Tree("Coffee")
# NonAlchohalic   = Tree("Non-Alchoholic")
# Alcoholic    = Tree("Alcoholic")

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlchohalic)
# Cold.addChild(Alcoholic)


# print(rootNode)


class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[]

    def __str__(self,level=0):
        ret= "   "* level + str(self.data) + "\n"
        for ch in self.child:
            ret += ch.__str__(level+1)
        return ret
    
    def addChild(self,object):
        self.child.append(object)
        print("Tree Node Added")


rootNode=Tree("N1")
N2     = Tree("N2")
N3    = Tree("N3")
N4    = Tree("N4")
N5    = Tree("N5")
N6   = Tree("N6")
N7    = Tree("N7")
N8    = Tree("N8")


rootNode.addChild(N2)
rootNode.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N6)
N4.addChild(N7)
N4.addChild(N8)


print(rootNode)