lst = [2,4,6,5,5,4,6,2,4,1,3,7,0]


#remove duplicates from a list 
lst1 = [1,2,3]
lst2 = [4,5,6]

unique_list = []

for i in lst:
    if i not in unique_list:
        unique_list.append(i)
        
        
print(unique_list)

#time complexcity O(n^2)
#space complexcity O(n)

""" 

"""

lst = [3,4,4,2,1,1,5]

uniqueIndex = 1
for i in range(1,len(lst)):
    is_duplicate = False
    for j in range(uniqueIndex):
        if lst[i] == lst[j]:
            is_duplicate = True
            break
    if not is_duplicate:
        lst[uniqueIndex] = lst[i]
        uniqueIndex +=1
            

         
del lst[uniqueIndex:]
print(lst)  

