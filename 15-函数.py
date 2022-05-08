#(1)函数的定义
# def 函数名(参数):
#  代码1
#  代码2
#  ......

#(2)函数的调用
#函数名(参数)

def sum_num(a, b):
    return a + b
# ⽤result变量保存函数返回值
result = sum_num(1, 2)
print(result)

#(3)不定长参数
def user_info(*args):
    print(args)
# ('TOM',)
user_info('TOM')
# ('TOM', 18)
user_info('TOM', 18)

#(4)字典拆包
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1
# 对字典进⾏拆包，取出来的是字典的key
print(a) # name
print(b) # age
print(dict1[a]) # TOM
print(dict1[b]) # 18