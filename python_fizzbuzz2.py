#coding: utf-8
print("いくつまで数えますか？")

num = input()

num = int(num)

print("それじゃ", num, "まで数えるよ！ Enterキーでスタート！")
input()

def fizzbuzz(i):
    if i%3==0 and i%5==0:
        return("Fizz Buzz")
    elif i%3==0:
        return("Fizz")
    elif i%5==0:
        return("Buzz")
    else:
        return(i)

for i in range(1, num+1):
    print(fizzbuzz(i), "|", end="")

print("\n\nありがとうございました！")