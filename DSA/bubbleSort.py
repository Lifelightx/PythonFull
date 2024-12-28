lst = [3,12,5,7,9,8,6,1]

lenth = len(lst)
print(lenth)
for i in range(lenth):
    for j in range(0,lenth-1):
        if lst[j+1] > lst[j]:
            temp = lst[j+1]
            lst[j+1] = lst[j]
            lst[j] = temp

print(lst)

arr = [2,5,9,3,7]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)

#selection sort

arr = [2,5,1,9,3,7]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
    
print(arr)