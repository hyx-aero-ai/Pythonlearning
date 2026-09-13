a=int(input("a"))
b=int(input("b"))

if a==b:
    print("一样大")
elif a>b:
    print("a大")
else :
    print("b大")
    
------------------------------------------
a=int(input("整数"))

if a%3==0:
    print("是3的倍数")
else :
    print("不是3的倍数")

------------------------------------------

a=int(input("整数"))

if a>0:
      if a%2==0:
          print("正偶数")
      else :
          print("正奇数")
elif a==0:
    print("零")
else :
    print("负数")
