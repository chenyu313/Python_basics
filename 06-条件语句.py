age=int(input("请输入您的年龄："))
if age<18:
    print(f"您的年龄是{age},童工一个！")
elif age>=18 and age<=60:
    print(f"您的年龄是{age},合法年龄！")
else:
    print(f"您的年龄是{age},该退休了！")

#三目运算符
a=1
b=2
c=a if a>b else b
print(c)