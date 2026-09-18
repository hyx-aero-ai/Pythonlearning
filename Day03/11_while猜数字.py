answer=7
a=int(input("请输入数字"))

while a!=7:
    if a<7:
        print("太小了")
    elif a>7:
        print("太大了")

    a=int(input("请继续输入"))

print("猜对了")