
ele = int(input("Enter the element: "))
pos = int(input("Enter position: "))

arr = [2,4,1,5,6,9]
new_arr = [0]*(len(arr)+1)

for i in range(pos):
    new_arr[i] = arr[i]
new_arr[pos] = ele
for i in range(pos,len(new_arr)):
    new_arr[i+1] = arr[i]

print(new_arr)

arr.insert()