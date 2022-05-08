# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 空字典
dict2 = {}
dict3 = dict()

print("=================")
#增加--->字典为可变类型
dict1['name'] = 'Rose'
# 结果：{'name': 'Rose', 'age': 20, 'gender': '男'}
print(dict1)
dict1['id'] = 110
# {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
print(dict1)

print("=================")
#删
#del() / del：删除字典或删除字典中指定键值对
dict2 = {'name': 'Tom', 'age': 20, 'gender': '男'}
del dict2['gender']
# 结果：{'name': 'Tom', 'age': 20}
print(dict2)
#clear()：清空字典
dict3 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict3.clear()
print(dict3)

print("=================")
#查
print(dict1['name'])
#字典序列.get(key, 默认值)
# 如果当前查找的key不存在则返回第⼆个参数(默认值)，如果省略第⼆个参数，则返回 None
dict4 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict4.get('name')) # Tom
print(dict4.get('id', 110)) # 110
print(dict4.get('id')) # None
#keys()
print(dict1.keys())
#values()
print(dict1.values())
# items()
print(dict1.items())

print("=================")
#字典的循环遍历
for key in dict1.keys():
    print(key)
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)
for key, value in dict1.items():
    print(f'{key} = {value}')