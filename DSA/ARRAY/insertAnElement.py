
ele = int(input("Enter the element: "))
pos = int(input("Enter position: "))

arr = [2,4,1,5,6,9]
new_arr = [0]*(len(arr)+1)

for i in range(pos):
    new_arr[i] = arr[i]
new_arr[pos] = ele
for i in range(pos,len(arr)):
    new_arr[i+1] = arr[i]

print(new_arr)

#without creating a new array

narr = [2,4,1,6,7,9]

#adding a dummy value for increase the size
narr.append(0)

for i in range(len(narr)-1,pos,-1):
    narr[i] = narr[i-1]

narr[pos] = ele

print(narr)
