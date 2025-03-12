lst = [3, 7, 1, 2, 8, 4, 5] 


actual_sum = 0
for i in lst:
    actual_sum += i

#since one number is missing
n = len(lst)+1
list_sum = (n*(n+1)) // 2

missing_num = list_sum - actual_sum

print(missing_num)
