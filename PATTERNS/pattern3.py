""" 
*****
****
***
**
*
"""

rows = int(input("Enter rows: "))

for i in range(rows,0,-1):
    for j in range(i):
        print("*",end='')
    print()
    
    
for i in range(rows,0,-1):
    for j in range(i):
        print(j+1, end="")
    print()
    
""" 
54321
4321
321
21
1
"""

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()