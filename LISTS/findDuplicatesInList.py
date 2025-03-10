lst = [1,2,2,1,3,3,4,5,5,6,7,8,8,0]

dup_list = []
#find duplicates

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] not in dup_list:
            if lst[i] == lst[j]:
                dup_list.append(lst[i])
                
print(dup_list)
