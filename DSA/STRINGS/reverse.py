str = "Hello Jeeban"
revStr = ""
for i in range(len(str)-1,-1,-1):
    revStr += str[i]
    
print(revStr)


def revString(s):
    return s[::-1]

print(revString("My Name is Laxan"))

def revStr(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str

print(revStr("MY name is Jeeban"))
    