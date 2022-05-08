# 把函数作为参数传⼊，这样的函数称为⾼阶函数，⾼阶函数是函数式编程的体现。函数式编程就是指这
# 种⾼度抽象的编程范式。

def sum_num(a, b, f):
    return f(a) + f(b)
result = sum_num(-1, 2, abs)
print(result) # 3

#内置⾼阶函数
#(1)map()
#map(func, lst)，将传⼊的函数变量func作⽤到lst变量的每个元素中，并将结果组成新的列表返回
list1= [1, 2, 3, 4, 5]
def func(x):
    return x ** 2
result = map(func, list1)
print(result) # <map object at 0x0000013769653198>
print(list(result)) # [1, 4, 9, 16, 25]

#(2)reduce()
# reduce(func(x,y)，lst)，其中func必须有两个参数。每次func计算的结果继续和序列的下⼀个元素做累
# 积计算。
import functools
list1 = [1, 2, 3, 4, 5]
def func(a, b):
    return a + b
result = functools.reduce(func, list1)
print(result) # 15

#(3) filter()
# filter(func, lst)函数⽤于过滤序列, 过滤掉不符合条件的元素, 返回⼀个 filter 对象,。如果要转换为列表,
# 可以使⽤ list() 来转换。
def func(x):
    return x % 2 == 0
result = filter(func, list1)
print(result) # <filter object at 0x0000017AF9DC3198>
print(list(result)) # [2, 4, 6, 8, 10]