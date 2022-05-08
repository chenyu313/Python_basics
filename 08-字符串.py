#字符串的转义
str1='I\'m Tom'
print(str1)

#三引号形式字符串支持换行
str2="""i am Tom,
        nice to meet you"""
print(str2)

#下标
str3="abc"
print(str3[0])

#切片
#序列[开始位置下标:结束位置下标:步长]
str4="abcdefg"
print(str4[1:4:2])
#-1表示从后前
print(str4[::-1])

#常用方法
#(1)查找：
# 字符串序列.find(子串,开始位置下标,结束位置下标) 注意：查找错误返回-1
str5="hello world and Python"
print(str5.find("and"))
#字符串序列.index(子串,开始位置下标,结束位置下标) 注意：查找错误会报错
print(str5.index("and"))
#字符串序列.count(子串,开始位置下标,结束位置下标)
print(str5.count("and"))

#(2)修改：
#字符串序列.replace(旧子串,新子串,替换次数)
str6="hello world and Python"
print(str6.replace("and","or"))
#字符串序列.split(分割字符,num)
print(str6.split("and"))
#字符或子串.join(多字符串组成的序列)
list1=["chenyu","zy"]
print("&".join(list1))

#capitlize():将字符串第一个字符转换成大写
print(str6.capitalize())

#title():将字符串每个单词首字母转换成大写
print(str6.title())

#lower():将字符串中大写转小写
#upper():将字符串中小写转大写
#lstrip():删除字符串左侧空白字符
#rstrip():删除字符串右侧空白字符
#strip():删除字符串两侧空白字符

#ljust():返回一个原字符串左对齐，并使用指定字符(默认空格)填充至对应长度的新字符串
#字符串序列.ljust(长度,填充字符)
print(str6.ljust(30,","))
#rjust()和center()同理

#(3)判断
#startswith(子串,开始位置下标,结束位置下标):检查字符串是否以指定子串开头，返回true和false
print(str6.startswith("hello"))
#endswith()同理

#isalpha():如果字符串至少有一个字符并且所有字符都是字符则返回true，否则返回false
#isdigit():如果字符串只包含数字则返回true，否则返回false
#isalnum():如果字符串至少有一个字符并且所有字符都是字母或者数字则返回true，否则返回false
#isspace():如果字符串中只包含空格，则返回true，否者返回false