""" 
1
12
123
1234
12345
"""

rows = int(input("Enter no of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1,end="")
    print()
    
""" 
1
22
333
4444
55555
"""
for i in range(rows):
    for j in range(i+1):
        print(i+1,end="")
    print()