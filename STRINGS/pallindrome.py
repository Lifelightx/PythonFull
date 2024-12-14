str = "pppppp"

def pallindromeChecker(str):
    x = str[::-1]
    if str == x:
        print("String is pallindrome")
    else:
        print("String is not pallindrome")

pallindromeChecker(str)

