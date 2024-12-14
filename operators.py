x = 10
y = 20

#swap two variables without using third variable
x = x+y
y = x-y
x = x-y
print(x,y)

#swap two variables using bitwise XOR operator
x = x^y
y = x^y
x = x^y
print(x,y)

#modulo operator

x = 10
y = 3
print(x % y)

#integer division   

x = 10
y = 3
print(x/y)
print(x ** y) #power 10 to the power 3
print(x // y) #integer division

#assignment operator

x = 10
x += 5
x -= 3
x *= 2
x /= 4

#urinary minus operator

x = 10
print(-x)

#unary plus operator

x = -10
print(+x)

#increment and decrement operators

x = 10
x += 1
x -= 1

#logical operator
x = 3
y = 1
print(x and y)
print(x or y)
print(not y)

a = 10
print(id(a))
b = 10
print(id(b))

if(a is b):
    print('a and b are same')

one = [1,2,3]
print(id(one))
two = [1,2,3]
print(id(two))

if(one != two):
    print('one and two are same')
elif(one is two):
    print('one and two are same as objects')
else:
    print('one and two are different')