arr = [12,4,56,13,78,11]

#brut force mthod
for i in range(len(arr)):
    for j in range(0,len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print("Highest Element: ",arr[len(arr)-1])

#optimal method
arr = [13,144,11,33,44]

largest = arr[0]
for i in arr:
    if arr[i]>largest:
        largest = arr[i]
print(largest)

