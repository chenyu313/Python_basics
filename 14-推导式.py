#列表推导式
#(1)for循环实现
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

#(2)列表推导式实现
list2=[i+1 for i in range(10)]
print(list2)

#(3)range()步⻓实现
list3 = [i for i in range(0, 10, 2)]
print(list3)

#(4)带if的列表推导式
list4 = [i for i in range(10) if i % 2 == 0]
print(list4)