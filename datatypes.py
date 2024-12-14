x = 10

print(type(x))

y = 10.3
print(type(y))

z = "HEllo"
print(type(z))

#built in data types
"""
None type
Numeric type
Sequence
Sets
Mappings
"""
#none type
""" Represents an object that does not contain any value"""
# numeric data types
"""
int
float
complex
"""

z = -90 #int
z = 4.56 #float
z = 4 + 3j #complex 

#converting data types explicitly or type casting

z = 3.4
int(z) # will display 3

num = 12
float(num) # will display 12.0

n = 10
com = complex(n)
print(com) # will display 10+0j

a = 10
b= -5
x = complex(a,b)
print(x)

#number to binary, octal, hexadecimal 
x = 20
print(bin(x))
print(hex(x))
print(oct(x))

#Sequence in Python

""" 

str
bytes
bytearray
list
tuple
range

"""

str = "Hello, world!"
print(str)
print(str[2:])
print(str[::-1])
print(str[2:5])
print(str[:4])
#bytes

eles = [12, 13, 14, 15, 16, 17, 18, 19, 25] #range from 0 to 255 
x = bytes(eles)
print(x[0])

#bytearray

y = bytearray(eles)
y[0] = 100
print(y)

#list

'''
Array : Similar type of elements

list : Different types of elements
'''

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.append(3)
list1.insert(0, 1)
list1.insert(4,[1, 2, 3, 4])
print(list1)
list3 = list1 + list2
print(list3)

#tuple

'''
can't be modified.
'''

#range Data type

r = range(30)

# for i in r: print(i)

#list

x = list(range(4))
print(x)


#set

'''
Unordered collection of unique elements
'''

s = {1, 2, 3, 4, 5, 6, 6, 7, 8, 9}
s.update([34, 24]) #argument must be a iterable data type
s.remove(2)
print(s)

#frozenset

'''
Unordered collection of unique elements. It is immutable.
update and remove functions are not supported
'''

fs = frozenset([1, 2, 3, 4, 5, 6, 6, 7, 8, 9])

#mapping

#or

#dictionary or dict data type

'''
unordered collection of key-value pairs
'''

d = {'name': 'John', 'age': 25, 'city': 'New York'}

d['address'] = 'Siadimal'

print(d.keys())
print(d.values())
print(d['name'])

for i in d:
    print(i,d.get(i))
    
#characters

str = 'Bharat'
newstr = str.upper()
print(newstr)
for i in str:
    print(i)