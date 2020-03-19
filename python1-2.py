double = lambda x: x * 2
y = double(5)
print(y)

myfuncs = [lambda x=1:x, lambda x=2:x*2, lambda x=3:x*3]

for func in myfuncs:
    print(func())
