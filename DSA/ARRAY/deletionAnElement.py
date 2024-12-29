
arr = [4,2,1,9,6]

ele = int(input("Enter the element: "))

flag = True
pos = 0
for i in range(len(arr)):
    if arr[i] != ele:
        flag = False
        
    else:
        pos = i
        flag = True
        break

if  flag == False:
    print("Enterd element is not exists.")
    
else:
    for i in range(pos,len(arr)-1):
        arr[i] = arr[i+1]
        
    arr.pop()    
    print(arr)

#deleting an element using pos
arrr = [1,2,4,5,3,7]
pos = int(input("Enter position: "))
for i in range(pos,len(arrr)-1):
    arrr[i] = arrr[i+1]
arrr.pop()
print(arrr)
    