#Tuple

tup = 1,2,4
print(type(tup))

lst = [1, 45, [3, 4], 35]
x = tuple(lst)
print(x.count(1))
print(x)

#nested tuple

nstup = (2,3,4),(5,6,7)
print(nstup)

# str = 'String'
# tup = tuple(str)
print(tup[0])

tup = tuple(['str', [1,2,3], 34])
tup[1].append(4)
tup[0].upper()
print(tup)

#concate tuple using + operator

tups = (1,3)+(3,8)
print(tups)

tup = ('foo','bar')*4
print(tup)

#unpacking tuple
tup = (2,3,6)
a,b,c = tup
print(a)
print(b)
print(c)

a,b = 1,2
b,a = a,b

print(a)
print(b)

tup = [(1,2,3), (4,5,6), (12, 1, 13)]
for a,b,c in tup:
    print(f"a= {a} b={b} c={c}")
    
tup = (1,2,3,4,5,6)
a,b,*rest = tup
print(a)
print(b)
print(rest)
rest.append(9)
print(rest)
print(type(rest))
print(tup)

#tuple methods

a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))

#List
tup = 1,2,5,7
lst = list(tup)
lst[1] = 45 #update
print(lst)
lst.append([4,56,9])
print(lst)

gen = range(10)
x = list(gen)
print(x)
import random as rd
x = [3,4,8,9,10,1,2]
x.insert(1,233)
m = x.pop(1)
print(m)
print(x)
m = rd.choice(x)
print("random choice",m)
x = rd.randrange(1,100)
print(x)

fruits = ['apple', 'banana','papaya','grapes','orange']
fruits.append('gauva')
fruits.extend(['gauva','tree','chiku'])
fruits.remove('banana')
fruits.insert(3,'banana')
# fruits.pop(len(fruits)-1)
print(len(fruits))
print(fruits)
print('gauva' not in fruits)

a = [3,5,89,1,10,23,12]
a.sort()
print(a)

b = ['banana', 'apple', 'arpita','chiku','jeeban','mama']
b.sort()
b.sort(key=len)

print(b)

a = [2,4,12,1,5,90,1]
a.sort(reverse=True)
print(a)

import bisect

a = [1,4,6,8,9,43]

print(bisect.bisect(a,4)) #find the index where should be the element to inserted to maintain sort
bisect.insort(a,12)
print(a)

print(a[3:5])

a[3:4] = 45,23
print(a)


#built in sequence functions
collection = [4521,45,65,23,85,92]
# i = 0
# for val in collection:
#     i+=1
    
# print(i)

#enumerate
for i, val in enumerate(collection):
    val +=20
    print(i,val)
    
print(collection)

collection = [[1,2],[2,3],[4,5]]

for i, j in collection:
    print(i,j)
    
a = 'Hello'
b = 10
print(a+str(b))

#mapping

s_list = ['foo', 'bar', 'baz']

mapping = {}

for i, val in enumerate(s_list):
    mapping[i] = val

print(mapping)


#sorted

a = [1,23,56,89,32]


x = sorted(a)
print(x)

zip1 = ['foo', 'bar', 'baz']
zip2 = ['one', 'two', 'three']

x = zip(zip1,zip2)
print(type(x))
y = list(x)
for i,j in x:
    print(i,j)
print(y)

#reversed is a generator

xlist = list(reversed(range(10)))
for i , val in enumerate(xlist):
    print(i, val)
    
#dictionary

empty_dict = {}

empty_dict.update({'name':'Jeeban',
                   'address':'Siadimal'})
print(list(empty_dict.items()))

empty_dict['name'] = 'Hrudananda'
# empty_dict.clear()
del empty_dict['address']
print(empty_dict)

#set

s = {2,4,6,5,3,4,5,2,34,12,32,33,1}

print(s)

a = {3,4,5,6}
b = {2,3,1,6,7,8}

x = a.union(b)
y = a | b
z = a.intersection(b)
z1 = a & b
print(y)
print(x)
print(z)
print(z1)

a = a.union(b)
print(a)


strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
str = []
for val in strings:
    if len(val)>2:
        str.append(val.upper())
        
print(str)
m = [x.upper() for x in strings if len(x)>3]
print(m)

