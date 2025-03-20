my_str = "Hello This is Jeebanjyoti Mallik is a good man this is a good time for start everything"

my_lst = my_str.split()
my_dict = {}

for i in my_lst:
    if i not in my_dict.keys():
        my_dict[i] = 1
    else:
        my_dict[i] +=1
        
print(my_dict)