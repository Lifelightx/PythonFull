lst = [4,5,4,5,5,6,6,7,8,9,8]

new_set = list(set(lst))
print(new_set)

unique_list = []

for i in lst:
    if i not in unique_list:
        unique_list.append(i)
            
print(unique_list)