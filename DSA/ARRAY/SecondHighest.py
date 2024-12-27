#brut force method

arr = [1,3,2,4,5,4,5]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)

#find second highest
large = arr[len(arr)-1]
slarge = arr[0]
for i in range(len(arr)-2,-1,-1):
    if arr[i] != large:
        slarge = arr[i]
        break
        
print(slarge)

#optimal method
arr = [1,5,7,4,7,6,2]

large = arr[0]
slarge = arr[-1]
for i in range(len(arr)-1):
    if arr[i]>large:
        slarge = large
        large = arr[i]
    if arr[i]>slarge and arr[i] !=large:
        slarge = arr[i]

print(large,slarge)