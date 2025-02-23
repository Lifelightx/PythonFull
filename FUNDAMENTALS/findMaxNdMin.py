lst = [23, 4, 14,2, 122, 18, 90]


max = lst[0]
min = lst[0]

for i in lst:
    if i>max:
        max = i
    if i<min:
        min = i
print(max,min)