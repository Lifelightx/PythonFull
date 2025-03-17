def zeroConverter(num):
    if num<0:
        i = num
        while i <= 0:
            print(i)
            i +=1
    elif num>0:
        i = num
        while i >= 0:
            print(i)
            i -=1
            
zeroConverter(-5)