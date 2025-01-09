import math

def odd_even(num):
    if num % 2 ==0:
        print("Number is Even")
    print("Number is Odd.")
    
    
odd_even(5)

#factorial of number

def factorials(num):
    prod = 1
    while num>=1:
        prod *= num
        num -= 1
    return prod

for i in range(1,11):
    print(f"Factorial of {i} is {factorials(i)}")
    
#function to check if a give number is prime or not

def checkerPrime(num):
    flag =1
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            flag = 0
            break
    return flag

count = 0
for i in range(12563212000000000,52563212000000000):
    if checkerPrime(i):
        count +=1
        print(i)
print("Total number of PrimeNumber: ",count)