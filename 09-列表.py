#列表格式
#[数据1,数据2,数据3,数据4,数据5]
#列表可以⼀次性存储多个数据，但是列表中的数据允许更改。

#（1）查找
name_list=["Tom","Lily","Rose"]
print(name_list[0])
#列表序列.index(数据,开始位置下标,结束位置下标)
print(name_list.index("Tom"))
#count():计数
print(name_list.count("Tom"))
#len():访问列表长度
print(len(name_list))
#判断是否存在：in    not in
print("Tom" in name_list)

#(2)增加
#列表序列.append(数据)
name_list.append("xiaoyu")
print(name_list)
#extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表
name_list.extend(["xiaohu"])
print(name_list)
#insert()：指定位置新增数据
#列表序列.insert(位置下标, 数据)
name_list.insert(1, 'xiaoming')
print(name_list)

#(3)删除
#del ⽬标-->删除列表
test_list=["Tom","Lily","Rose"]
del test_list
#print(test_list) 报错
#删除指定数据
del name_list[1]
print(name_list)
#pop()：删除指定下标的数据(默认为最后⼀个)，并返回该数据
del_name=name_list.pop()
print(del_name)
#remove()：移除列表中某个数据的第⼀个匹配项
name_list.remove("Tom")
print(name_list)
#clear()：清空列表
name_list.clear()
print(name_list)

#(4)修改
name_list2=["Tom","Lily","Rose"]
name_list2[0]="tom"
print(name_list2)
#逆置：reverse()
name_list2.reverse()
print(name_list2)
#排序：sort()
name_list2.sort()
print(name_list2)

#(5)复制
name_list3=name_list2.copy()
print(name_list3)

