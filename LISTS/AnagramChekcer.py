str1 = input("Enter string 1: ").lower()
str2 = input("Enter string 2: ").lower()

lst1 = list(str1)
lst2 = list(str2)

if sorted(lst1) == sorted(lst2):
    print("Equal")