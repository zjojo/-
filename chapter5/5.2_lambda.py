# encoding:utf-8

"""
lambda表达式
lambda parama:results
"""
import random

data = list(range(10))
print(data)
print(random.shuffle(data))

data.sort(key = lambda x:x)  # key执行排序规则
print(data)

data.sort(key = lambda x:len(str(x)))  #按转化成字符串以后的长度排序

x = [[random.randint(1,10) for j in range(5)] for i in range(5)] #二维列表，包含5个子列表的列表，每个子列表包含5个1到10之间的随机数
x1 = [random.randint(1,10) for j in range(5)]   # 列表推导式，生成一个包含5个随机值元素的列表
print(x)
print(x1)
for item in x:
    print(item)

y = sorted(x, key=lambda item: (item[1], item[4])) #先按照子列表中下标为1的元素升序排序，然后按照下标为4的进行升序排序
for item in y:
    print("y中item的值%s"%item)
