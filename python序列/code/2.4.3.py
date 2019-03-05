#encodig:utf-8
"""
集合运用案例
需求：生成number个介于start和end之间不重复的随机数并比较各自的效率
"""

#方式一：使用列表实现
import time
import random
def RandomNumbers(number, start, end):
    """使用列表生成基于start和end之间的number个不重复的随机数"""
    data = []
    n = 0
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
            n += 1  #如果元素不在列表里面，就加进去，并且个数+1，
        if n == number-1:
            break
    return  data

def RandomNumbers1(number, start,end):
    """使用列表的第二种方式，生成在start和end之间的number个不重复的随机数"""
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
        if len(data) == number:
            break#当长度等于number个数了，就结束循环
    return data

def RandomNumber2(number, start, end):
    """使用集合创建number个介于start和end之间的不重复的随机数"""
    data = set()
    while True:
        element = random.randint(start, end)
        data.add(element)
        if len(data) == number:
            break
    return data

print("---"*20)

#以下测试效率
#数字范围
begin,end = 1, 100000
#生成个数
num = 5000
#执行次数
rep = 10

for ran  in (RandomNumbers, RandomNumbers1, RandomNumber2):
    """遍历所有函数，取出函数对象"""
    start =time.time()
    for i in range(rep):
        ran(num, begin, end) #这里给函数传参执行
    print(ran.__name__, time.time() -start) #这里查看对应的执行时间


#测试效率比较下来，第一个函数的效率比第二个函数效率还高一点，原因在于什么？
#在RandomNumber2  中判断个数是否够了的时候用的是len函数，而len实际统计长度是通过从左到右开始数列表元素有多少个，然后返回，
# 所以效率相对较差，比较下来，集合的效率最高

