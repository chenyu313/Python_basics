#循环
i=0
while i<5:
    print("zy我想你了")
    i+=1
#break
j=1
while j<5:
    if j==4:
        print("吃饱了，不吃了")
        break
    print(f"吃了第{j}个苹果")
    j+=1
#continue

#for循环
str1="123456"
for a in str1:
    print(a)

#拓展1
# while 条件:
#     条件成立执行
# else:
#     循环正常结束后执行的代码

#拓展2
# for 临时变量 in 序列:
#     重复执行代码
# else:
#     循环正常结束执行