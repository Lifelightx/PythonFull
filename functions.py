def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)
    

x = factorial(4)
print(f'factorial is',x)

vol = lambda x,y,z: x*y*z
print(vol(10,20,30))


for i in range(5,0,-1):
    print(i)