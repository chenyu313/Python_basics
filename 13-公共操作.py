#len()
str="abcdefg"
print(len(str))

#del()
list1 = [10, 20, 30, 40]
del(list1[0])
print(list1) # [20, 30, 40]

#max() & min()
print(max(str))
print(min(str))

#range()
# 1 3 5 7 9
for i in range(1, 10, 2):
    print(i)

list2 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list2):
 print(i)
for index, char in enumerate(list2, start=1):
 print(f'下标是{index}, 对应的字符是{char}')