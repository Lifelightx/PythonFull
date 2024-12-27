arr = [2,2,2,1,1,1,3,3,3]

#brut force method
without_repeat = list(set(arr))
print(without_repeat)


#brut force method

s = set()
for i in arr:
    s.add(i)

index = 0
for i in s:
    arr[index] = i
    index +=1
    

print(arr)


#optimal method

arr = [1,1,1,2,2,3,3,4]

i = 0
while i < len(arr):
    j = i+1
    while j<len(arr):
        if arr[i] == arr[j]:
            arr.pop(j)
        else:
            j +=1
    i+=1
print(arr) 


#using for loop

arr = [1,2,2,2,5,5,5,3,3]

for i in range(len(arr)):
    index = i+1
    while index < len(arr):
        if arr[i] == arr[index]:
            arr.pop(index)
        else:
            index +=1
print(arr)
        