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
    
