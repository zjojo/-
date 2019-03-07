# -*-encoding:utf-8 -*-
"""
字符串应用实例：密码的加密解密  和 密码强度判断实例
"""
from itertools import cycle


def crypt(source, key):
    """编写函数实现字符串加密和解密，循环使用指定密钥，采用简单的异或算法"""
    result = ''
    temp = cycle(key)  # itertool提供用于循环操作迭代对象的函数，返回的是一个迭代器对象，惰性求值，用到的时候才会返回一个值
    print(type(temp))
    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))
        # 进行一个异或运算，异或运算只能整数使用，不能字符串之间使用
        # ord()与chr()函数是配对函数，ord()返回值是对应的十进制整数。即ASCII值
        # chr()恰巧与ord函数是相反的，返回值是当前整数对应的ascii字符。
    return result


if __name__ == "__main__":
    source = "Hello ,jotling"
    key = "Swie792n#dsn3h"
    print("加密前：{0}".format(source))
    encrypt = crypt(source, key)  # 加密
    print("加密后：{0}".format(encrypt))
    decrypt = crypt(encrypt, key)  # 解密，异或运算的原因，可以用加密的值重新组合key进行解密操作
    print("解密后：{0}".format(decrypt))


