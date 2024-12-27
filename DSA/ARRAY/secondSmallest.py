arr = [6,4,5,7,6,7,2]


#second smallest

small = arr[0]
ssmall = arr[-1]

for i in range(len(arr)):
    if arr[i]<small:
        ssmall = small
        small = arr[i]
    if arr[i]<ssmall and arr[i] != small:
        ssmall = arr[i]
        
print(small,ssmall)