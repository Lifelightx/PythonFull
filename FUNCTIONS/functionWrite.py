def myFun():
    """First function"""
    print("Hello From function")
    
myFun()

def greet(name):
    print("Good morning ", name)
    
greet("Jeeban")

def sumFun(a,b):
    c = a+b
    return c

res = sumFun(10,5)
print(res)

def calculate(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div

#this will return a tuple of retrn values

for i in calculate(10,5):
    print(i)