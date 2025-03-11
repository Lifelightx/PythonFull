def checkPrimeNum(num):
    isPrime = True
    if num<=1:
        isPrime = False
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
            break
    return isPrime

def printPrimeNum(start, end):
    for i in range(start,end):
        if checkPrimeNum(i):
            print(i)
            
            
printPrimeNum(0,20)
            
    