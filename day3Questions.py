# find the maximum number of consecutive 1s iin a binary array

# input = [1,1,0,1,1,1,0,1,1,1,1]

# count = 0

# for i in input:
#     if i == 1:
#         count += 1
    
#     elif input[i] == 0: 
#         count = 0
#         print("elif loop")
# print(count)

# write a progrram to count the number of occurrences of a substring in a given string
# input = "abababab"
# sub = "ab"
# count = 0
# # for i in input:
# #     input[i] +


# #chatgpt
# count = input.count(sub)
# print(count)

#Q. how many types of argument we can pass in function


# # Q. find row wise max value
# row = [[100,198,333,323],
#  [122,232,221,111],
#  [223,565,245,764]]

# newlist=[]
# for i in range(3):
#     j =0 
#     max = row[i][j]
#     for j in range(4):
#         c_max = row[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)

input= "prashant*is*good*programmer"

newname=''
val=''
for i in input:
    if i !='*':
        newname += i
    else:
        val +=i
print(newname)
print(str(val+newname))

# homework
# input = aaabbbbccceeeee
# output= a3b4c3e5