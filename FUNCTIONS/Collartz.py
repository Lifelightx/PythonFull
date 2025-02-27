def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num*3 +1
    
while True:
    try:
        num = int(input("Enter number: "))
        if num == 1:
            break
        else:
            print(collatz(num))
    except Exception as e:
        print(e)