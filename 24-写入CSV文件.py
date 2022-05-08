#写入CSV文件
my_numbers=[0,1,2,3,4,5,6,7,8,9]
max_index=len(my_numbers)
output_file="D:/PycharmProjects/pythonProject/Python基础/文件夹1/test2.txt"
#'a'是追加方式，将输出追加到一个已经存在的输出文件末尾的方法
filewriter=open(output_file,'a')
for index_value in range(len(my_numbers)):
    if index_value<(max_index-1):
        #wirte函数处理的是字符串，你需要将整数转为字符串
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()