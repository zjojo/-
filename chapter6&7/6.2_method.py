# encoding:utf-8

"""
方法：包含静态方法，类方法，私有方法，公有方法
区分：静态方法和类方法的不同
静态方法：通过staticmethod定义，可以通过类或者实例对象调用,静态方法是类中的函数，不需要实例。引用别人说的：静态方法主要是
用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理
解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
类方法：通过classmethod定义，调用对象为类或者方法，第一个参数必须是类对象
实例方法：必须通过实例对象才可以调用

"""
class Root(object):
    __total = 0  # 属于类的私有变量
    def __init__(self, v):
        self.__value = v # 属于实例的私有变量
        self.__total += 1  # 当前类实例对象可以访问类的私有变量

    def show(self):    # 普通实例方法
        print('self.__value', self.__value)
        print('Root.__total', Root.__total)

    @classmethod   # 装饰器，声明类方法
    def classShowTotal(cls): # 类方法
        print(cls.__total)

    @staticmethod  # 装饰器，声明静态方法
    def staticMethodTotal():
        print(Root.__total)


if __name__ == "__main__":
    Root.classShowTotal()
    r = Root(5)
    r.show()
    r.classShowTotal()
    r.staticMethodTotal()