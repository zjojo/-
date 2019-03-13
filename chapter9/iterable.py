# encoding:utf-8

"""
什么是迭代协议？
迭代器是什么？ 迭代器是访问集合元素的一种方式，一般来遍历数据
迭代器和以下标的方式访问不一样，迭代器是不能重复访问的，迭代器提供了一种惰性求值的方式
迭代器：继承了Iterable 中的__iter__方法和，以及自身的__next__方法，而list等多种可迭代对象，仅仅是实现了__iter__方法
"""
from collections.abc import Iterable, Iterator
a = [1,2,3]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))