import random

comp_num = random.randint(1,20)

for i in range(6):
    num = int(input("guess the number: "))
    if num<comp_num:
        print("Number is Too Low")
    elif num>comp_num:
        print("Number is too High")
    elif num == comp_num:
        print("guess is correct..")
        break
else:
    print("Game over")       