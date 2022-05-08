#累加
def sum_numbers(num):
    #出口
    if num==1:
        return 1
    return num+sum_numbers(num-1)
#调用函数
sum_result=sum_numbers(10)
print(sum_result)