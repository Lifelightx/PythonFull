def jumpingWhite(num):
    for i in range(1,num+1):
        if i**2 < num:
            print(i**2)
            
jumpingWhite(10)