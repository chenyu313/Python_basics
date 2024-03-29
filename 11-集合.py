#创建集合使⽤ {} 或 set() ， 但是如果要创建空集合只能使⽤ set() ，因为 {} ⽤来创建空字典

# 特点：
# 1. 集合可以去掉重复数据；
# 2. 集合数据是⽆序的，故不⽀持下标
s1 = {10, 20, 30, 40, 50}
print(s1)

print("=================")
#添加
#add():增加数据
s1.add(60)
print(s1)
#update(),追加的数据是序列
s1.update([100, 200])
print(s1)

print("=================")
#删除
#remove():删除集合中的指定数据，如果数据不存在则报错
s1.remove(10)
print(s1)
#discard()，删除集合中的指定数据，如果数据不存在也不会报错
s1.discard(20)
print(s1)
#pop()，随机删除集合中的某个数据，并返回这个数据
del_num=s1.pop()
print(del_num)

print("=================")
#查找
# in：判断数据在集合序列
# not in：判断数据不在集合序列
print(10 in s1)
print(10 not in s1)