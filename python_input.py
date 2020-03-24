#coding:UTF-8
print("Please input the first number.")
i = input()

print("Please input the second number.")
j = input()

i = int(i)
j = int(j)

if i > j:
    print("First number is bigger than second number")
elif i < j:
    print("First number is smaller than second number")
else:
    print("Two Numbers is equal.")