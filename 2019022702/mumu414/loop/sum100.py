#创建一个变量初始化为0
sum = 0

#调用range()函数创建一个有序数列并通过for循环遍历数列
for n in range(101):
    #将遍历的数列元素求和
    sum += n

#打印输出求和结果
print(sum)