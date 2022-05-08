num=input("请您输入您的幸运数：")
print(f"您的幸运数是{int(num)}")
print(type(int(num)))

#eval 将字符串中的数据转换成python表达式原本的类型
str="[1,2,3]"
str2="(1000,2000,3000)"
print(type(eval(str)))
print(type(eval(str2)))