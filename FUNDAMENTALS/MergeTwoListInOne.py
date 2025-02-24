lst1 = [1,3,5,7]
lst2 = [2,6,8]


lst = []

# with time complexcity O(m+n)
i,j = 0,0

while i<len(lst1) and j<len(lst2):
    if lst1[i]<lst2[j]:
        lst.append(lst1[i])
        i+=1
    else:
        lst.append(lst2[j])
        j+=1
while i<len(lst1):
    lst.append(lst1[i])
    i+=1
while j<len(lst2):
    lst.append(lst2[j])
    j+=1
    
print(lst)