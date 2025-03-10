str = input("Enter a string: ")

rev = "" 

for i in str:
    rev = i + rev

if rev == str:
    print("Strings are pallindrome.")
else:
    print("Strings are not pallindrome.")