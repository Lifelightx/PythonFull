ar = []

n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i % 3 == 0:
        ar.append("Fizz")
    elif i % 5 == 0:
        ar.append("Buzz")
    else:
        ar.append(i)
        
print(ar)
    