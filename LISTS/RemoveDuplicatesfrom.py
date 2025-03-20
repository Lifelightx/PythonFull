lst = [3,3,4,4,5,5,6,6,6,7]

my_lst = []

for i in lst:
    if i not in my_lst:
        my_lst.append(i)
    
    
print(my_lst)

seen = set()
new_lst = []
for i in lst:
    if i not in seen:
        seen.add(i)
        new_lst.append(i)
print(new_lst)