import sys
import glob
import os
#os模块和glob模块组合一起使用，可以找出符合特定模式的某个文件夹下的所有文件
inputPath="D:/PycharmProjects/pythonProject/Python基础/文件夹1"
i=1
for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
    print("=======这是第{}个文件=======".format(i))
    i=i+1
    with open(input_file,'r',newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))