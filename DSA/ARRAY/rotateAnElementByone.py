arr = [2,1,3,7,5,4]

temp = arr[0]

for i in range(1,len(arr)):
    arr[i-1] = arr[i]

arr[len(arr)-1] = temp

print(arr)