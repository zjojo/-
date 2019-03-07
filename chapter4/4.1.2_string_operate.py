# -*- encoding:utf-8 -*-
"""
字符串认识及使用方法
字符串是不可变序列，其中序列即表示它和列表等一样，可以使用切片，索引的方法获取其中的值，不可变，表示一旦定义之后，不能通过
索引等方法去修改其中的值，也表示对字符串执行的方法都是会生成新的字符串，因为字符串不允许修改
"""
# 字符串格式化：
# 方式一：%
data = ("Linda", 14)
print("This is %s，he(she) is %d years old"%(data[0],data[1]))

# 方式二：format   ------官方推荐的方法，因为使用方式灵活
print("The number {0:,} in hex is{0:#x}, the number {1} in oct is {1:#o}".format(555,55))
#通过位置指定：其中0表示指定要格式化的值的位置，#o,#x表示格式化的格式

print("My name is {name},my age is {age}".format(name="joting",age=24))
# 通过参数指定值

position = (5,6,12)
print("X:{0[0]};Y{0[1]};Z{0[2]}".format(position))
# 可以传入元组形式的值

# 字符串的查找与计数
s = "dahsojdpwjqpwenqwinepqw"
print(s.find("j",7))  # 从左边第七个位置查找到字母为j的位置并返回
print(s.rfind("j"))  # 从右边开始查找到字母为j的位置并返回
print(s.count("d")) # 统计s中出现"d"字母的个数

# 字符串的分隔于连接
t = "adb,daerr,linda,wew"
l = t.split(",")  # 按照","将字符串分隔，返回一个列表
print(l)
# 分隔除过split之外，还有partitioon方法，以指定字符串为分隔符将原字符串分隔为3部分：分隔符之前字符串，分隔符本身，分隔符之后的字符串
print(t.partition(","))  # 找到第一个逗号之后，就将字符串分隔完毕，与split不同
sep = "-".join(l)  # 按照-将列表连接成一个字符串
print(sep)

# 字符串的替换：简单替换和映射替换
# 简单替换：replace(a, b)
s = "Python is a amazing language"
rs = s.replace("u", "a")
print(rs)
# 测试用户输入中是否有敏感词
words =("暴力", "敏感", "银行卡")
text = "用户输入银行卡号"
for word in words:
    if word in text:
        text = text.replace(word, "***")
print(text)


#复杂映射替换
"""创建映射表，adb一一对应转化为：uxw,即a转化为u，b转换为x..."""
table = "".maketrans('abc', 'uxw')
s = "Python is a greater programming language,I like it"
print(s.translate(table))
# maketrans和translate成对出现使用，可以用来做加密
# 例子： 凯撒加密
import string
def kaisa(s, k):
    lower = string.ascii_lowercase  #返回所有的小写字母
    upper = string.ascii_uppercase   # 返回所有的大写字母
    before = string.ascii_letters  # 返回所有字母a......Z
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = "".maketrans(before, after)
    return s.translate(table)

print(kaisa(s, 3))