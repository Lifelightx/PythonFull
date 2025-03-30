""" 
     A
    A B
   A B C
  A B C D
 A B C D E 
"""
alph = 65
rows = int(input("Enter rows : "))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end='')
    for j in range(0,i+1):
        print(chr(alph+j), end=" ")
    alph = 65
    print()