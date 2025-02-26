""" 
*******
 *****
  ***
   *
"""

rows = int(input("Enter rows: "))
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()