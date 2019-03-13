# encoding:utf-8

"""
变量的作用域：全局变量与局部变量
全局变量：global 作用：声明全局变量，或者创建全局变量
"""

def scope_test():
    def do_local():
        spam = "我是局部变量"

    def do_nolocal():
        nonlocal spam
        spam = "我不是局部变量， 也不是全局变量"

    def do_global():
        global spam  # 会创建一个在 scpoe_test之外的一个全局变量
        spam = "我是全局变量"  # 不会修改局部变量spam='原来的值'的值

    spam = "原来的值"  # 在scope_test中属于局部变量
    do_local()
    print("do_local",spam)
    do_nolocal()
    print("do_nonlocal之后的值", spam)
    do_global()
    print("do global", spam)
scope_test()
print("scp_test", spam)