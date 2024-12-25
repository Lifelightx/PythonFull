from math import floor

lst = [23,45,48,49,51,125]

def binarySearch(lst,ele,start,end):
    mid =  (len(lst)-1) // 2

    if lst[mid] == ele:
        return mid
    if lst[mid] < ele:
        binarySearch(lst,ele,mid+1,end)
    else:
        binarySearch(lst,ele,start,mid-1)

x = binarySearch(lst,125,0,len(lst)-1)

print("Found at position: ",x)
    