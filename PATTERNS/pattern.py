""" 
*
**
***
****
*****
"""
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("*" * i, end='')
    print()

""" 
1
1 2
1 2 3
1 2 3 4
"""
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

""" 
    1
   121
  12321
 1234321
123454321
"""
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end='')
    for j in range(1,i+1):
        print(j, end='')
    for j in range(i-1,0,-1):
        print(j, end='')
    print()
    
""" 
     *
    **
   ***
  ****
 *****
******
"""
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print("*", end='')
    print()
""" 
    *
   * *
  * * *
 * * * *
* * * * *
"""
