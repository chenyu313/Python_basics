#写入文件
my_letters=['a','b','c','d','e','f','g','h','i']
max_index=len(my_letters)
output_file="D:/PycharmProjects/pythonProject/Python基础/文件夹1/test2.txt"
filewriter=open(output_file,'w')
for index_value in range(len(my_letters)):
    if index_value<(max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()