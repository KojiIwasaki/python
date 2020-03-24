#coding: utf-8
print("いくつまで数えますか？")

num = input()

num = int(num)

print("それじゃ", num, "まで数えるよ！ Enterキーでスタート！")
input()

def fizzbuzz(i):
    for i in range(1, i + 1):
        if i%3==0 and i%5==0:
            print("Fizz Buzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(num)

print("\nありがとうございました！")