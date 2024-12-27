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
    

