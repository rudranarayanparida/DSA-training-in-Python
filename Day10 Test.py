# # # # #Q1. find the leaders in the array
# # # # #Input: n=6 A[]={16, 17, 4, 3,5, 2,}
# # # # #Ouput: 17 5 2 Explanation: The first leader is 17 as it is greater than all the elements to its right. Similarly, the next leader is 5. The right most element is always a leader so it is also included.

# # # # def leaders(arr, n):
# # # #     result=[]
    
# # # #     max_right = arr[n-1]
# # # #     result.append(max_right)
    
# # # #     for i in range (n -2, -1, -1):
# # # #         if arr[i] >= max_right:
# # # #             max_right =arr[i]
# # # #             result.append(arr[i])
            
# # # #     result.reverse()
# # # #     return result

# # # # n = int(input())
# # # # arr=list(map(int, input().split()))

# # # # ans= leaders(arr, n)

# # # # print(*ans)
# # # # #====================================================================================

# # # #Q2. Find Missing Numbers
# # # #arr=[7, 2, 5, 3, 5, 3]
# # # #arr=[7, 2, 5, 4, 6, 3, 5, 3]
# # # # The brr is the original List. The number missing are [4, 6].

# # # def missingNumbers(arr, brr):
# # #     freq1 = {}
# # #     freq2 = {}

# # #     for num in arr:
# # #         freq1[num] = freq1.get(num, 0) + 1

# # #     for num in brr:
# # #         freq2[num] = freq2.get(num, 0) + 1

# # #     result = []

# # #     for num in sorted(freq2):
# # #         if freq1.get(num, 0) != freq2[num]:
# # #             result.append(num)

# # #     return result

# # # #====================================================================================

# # #3. A given string with multiple characters that are repeated consecutively. Reduce the side of this string using given logic
# # #Input: aabbbbeeeeggg
# # #Output: a2b4e4g3

# # s = input()

# # result = ""
# # count = 1

# # for i in range(1, len(s)):
# #     if s[i] == s[i - 1]:
# #         count += 1
# #     else:
# #         result += s[i - 1]
        
# #         # Add count only if greater than 1
# #         if count > 1:
# #             result += str(count)
            
# #         count = 1

# # # Handle last character
# # result += s[-1]

# # if count > 1:
# #     result += str(count)

# # print(result)

# # #====================================================================================

# #Q.4 Given an array of integers of length N. For each element in the array, find the next element to its right which is larger than it. If there is no such element, output -1 for that element.
# #Input: N=4 [1 3 2 4]
# #Output: [3 4 4 -1]

# # Read input
# n = int(input())
# arr = list(map(int, input().split()))

# result = []

# # Find next greater element for each element
# for i in range(n):
#     next_greater = -1
    
#     for j in range(i + 1, n):
#         if arr[j] > arr[i]:
#             next_greater = arr[j]
#             break
    
#     result.append(next_greater)

# # Print result
# print(*result)

# #====================================================================================

#Q.5 Post Order Traversal
#Sample Input:
#   1
#     \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4
#Output: 4 3 6 5 2 1

def postOrderTraversal(rootNode):
    if not rootNode:
        return
        
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)