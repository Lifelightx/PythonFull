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