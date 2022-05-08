#导⼊os模块
import os
#(1)文件重命名
#os.rename("文件夹", "文件夹1")
#(2)删除文件
#os.remove("文件夹1")
#(3)创建⽂件夹
os.mkdir("这是一个文件夹")
#(4)删除⽂件夹
os.rmdir("这是一个文件夹")
#(5)获取当前⽬录
os.getcwd()
#(6)改变默认⽬录
os.chdir("Python基础")
#(7)获取⽬录列表
os.listdir("Python基础")