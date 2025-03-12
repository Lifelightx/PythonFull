def arm_strong_checker(num):
    len_num = len(str(num))
    sum_of_digits = 0
    for i in str(num):
        sum_of_digits += int(i) ** len_num
    
    if sum_of_digits == num:
        print(num)
        
    
for i in range(100,400):
    arm_strong_checker(i)
    
    
def arm_strong_checker_m(num):
    len_num = len(str(num))
    original_num = num
    sum = 0
    while num != 0:
        digit = num % 10
        sum += digit ** len_num
        num //= 10 
    if sum == original_num:
        print(original_num)

arm_strong_checker_m(153)