# x = 10
# print(id(x))

# def my():
#     x =10
#     # x +=5 #if values are same then id will be same
#     return id(x)
# print(my())


def modify(x):
    # x += 10
    lst = [x, id(x)]
    return lst
    
y = 25
print(id(y))
m = modify(y)
print(m)

lst = [2,3,5,7]

#integers, floating point, strings, tuples are immutable
""" that measn their data cannot be change when we try to modify a new object is created with the
    modified value
"""
def modifyLst(lst):
    lst.append(5)
    print(lst, id(lst))
    
modifyLst(lst)
print(id(lst))