# ⽂件操作的作⽤就是把⼀些内容(数据)存储存放起来，可以让程序下⼀次执⾏的时候直接使
# ⽤，⽽不必重新制作⼀份，省时省⼒。

#====>写<====
# 1. 打开⽂件
f = open('文件操作文件夹/test.txt', 'w')
# 2.⽂件写⼊
f.write('hello world')
# 3. 关闭⽂件
f.close()

#====>读<====
f = open('文件操作文件夹/test.txt')
content = f.readlines()
print(f"读取全部：{content}")
# 关闭⽂件
f.close()

#====>⽂件备份<====
old_name = input('请输⼊您要备份的⽂件名：')
# 2.1 提取⽂件后缀点的下标
index = old_name.rfind('.')
new_name = old_name[:index] + '[备份]' + old_name[index:]
print(new_name)
# 3.1 打开⽂件
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')
# 3.2 将源⽂件数据写⼊备份⽂件
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

# 3.3 关闭⽂件
old_f.close()
new_f.close()