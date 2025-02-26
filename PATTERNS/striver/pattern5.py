""" 
*******
 *****
  ***
   *
"""

rows = int(input("Enter rows: "))
for i in range(rows):
    for j in range(i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()