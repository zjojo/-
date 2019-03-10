# encoding:utf-8
"""
正则表达式常用方法：
compile(pattern) 创建模式对象
search,match方法的区别
search()方法是再整个字符串中寻找模式，返回match对象或None
match()方法是从字符串的开始出开始匹配模式，返回match对象或None,只有在0位置匹配成功的话才返回match对象，否则就是None
"""

import re
print(re.match('super', 'superstition').span())

print(re.match('super', 'insuperable'))   # 从0的位置未匹配，所以返回的是None

print(re.search('super', 'superstition').span())

print(re.search('super', 'insuperable').span())