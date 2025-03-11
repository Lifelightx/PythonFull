lst  = [2,3,4,6,7,8,9,10]

lrgst = float("-inf")
slrgst = float('-inf')


for i in lst:
    if i>lrgst:
        slrgst = lrgst
        lrgst = i
    if i != lrgst and i>slrgst:
        slrgst = i

print(slrgst)
print(lrgst)