lst = [2,3,4,67,12,14,18,11]

start = 0
end = len(lst)-1
while(start<end):
    temp = lst[end]
    lst[end] = lst[start]
    lst[start] = temp
    start +=1
    end -= 1

print(lst)