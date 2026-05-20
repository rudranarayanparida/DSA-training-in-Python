# Q.
# def fun(value,values):
#     var =1 
#     values[0]=44

# t =3 
# v = [1,2,3]
# fun(t,v)
# print(t, v[0])

# output
# A. 1 44
# B. 3 1
# C. 3 44
# D. 1 1


# Q. 

def f(i , values=[]):
    values.append(i)
    print(values)


f(1)
f(2)
f(3)