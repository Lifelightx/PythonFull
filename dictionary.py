my_dict = {"rama":"1st Jan", "sita":"24th Feb", "Laxman":"12th March"}

my_dict.update()
print(my_dict.keys())
print(my_dict.values())

my_dict["Laxman"] = "1st Nov"
print(my_dict)
print(my_dict["rama"])
print(my_dict.items())

for i in my_dict.keys():
    print(my_dict[i])
    
for i,k in my_dict.items():
    print(i,k)
    
dic = {x : x**2 for x in range(5)}
print(dic)

#list comprehension

lst = [1,3,4,5,6,11,3]

n = [x**2 for x in lst]
print(lst)
print(n)