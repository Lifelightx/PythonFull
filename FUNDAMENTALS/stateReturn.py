num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 1st num: "))

flag = True


if (num1>0 and num2<0) or (num1<0 and num2>0):
    flag = False
    
print(flag)