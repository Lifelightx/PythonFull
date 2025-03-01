def commandCode(lst):
    lst.insert(len(lst)-1,"and")
    str =""
    for i in lst:
        str += i+", " 
    print(str)

commandCode(["Hello", "Jeeban", "How are", "You"])

