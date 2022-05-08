import sys
#在解释器启动后, argv 列表包含了传递给脚本的所有参数, 列表的第一个元素为脚本自身的名称。
# sys.argv[0] 表示程序自身
# sys.argv[1] 表示程序的第一个参数
# sys.argv[2] 表示程序的第二个参数
print(sys.argv[0])
inputPath="D:/PycharmProjects/pythonProject/Python基础/test.txt"
filereader=open(inputPath,"r")
for row in filereader:
    print(row.strip())
filereader.close()

#新型语法-->读取文件
print("新型语法-->读取文件")
#with语法创建文件对象，这种语法会在with语句结束后自动关闭文件
with open(inputPath,'r',newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))