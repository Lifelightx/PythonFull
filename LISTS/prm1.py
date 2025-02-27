spam = [1,2,3,4,5]
spam.insert(2,"Hello")
print(spam)

x = spam[int('3'*2)//11]
print(x)

print(spam[:2])

bacon = [3.14, 'cat', 11, 'cat', True]
m = bacon.index("cat")
bacon.append(99)
print(m)
bacon.remove("cat")
print(bacon)