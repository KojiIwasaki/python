def vmachine(pay, price=130, number = 1):
    change = pay - (price * number)

    if change >= 0:
        print("Thank you for purchasing")
        return change
    elif change < 0:
        print(-change, "yen is short")
        return pay

x = vmachine(500)
print(x)

x = vmachine(500, 180)
print(x)

x = vmachine(100)
print(x)

