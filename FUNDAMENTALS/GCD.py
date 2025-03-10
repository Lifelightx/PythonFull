n1 = int(input("Enter 1st num: "))
n2 = int(input("Enter 2nd numb: "))

min_num = min(n1,n2)

gcd = 1

for i in range(1,min_num+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i

print(gcd) 