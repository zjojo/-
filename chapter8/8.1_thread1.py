# -*- encoding:utf-8 -*-
"""线程的创建与阻塞，守护进程"""
import threading
import time


class Mythread(threading.Thread):
    """继承Thread类创建线程"""
    def __init__(self, sum):
        threading.Thread.__init__(self)
        self.sum = sum

    def run(self):
        print("I am {0}".format(self.sum))


t1 = Mythread(1)  # 创建线程
t2 = Mythread(2)
t3 = Mythread(3)

t1.start()  # 线程启动
t2.start()
t3.start()

# Thread对象中的常用方法：
# join() 线程阻塞等待时间


def func(x, y):
    """线程函数"""
    for i in range(x, y):
        print(i)
    time.sleep(10)  # 等待10秒


t4 = threading.Thread(target=func, args=(15, 20))  # 创建子线程4
t4.start()
t4.join(3)
# join的含义：线程等待时间 等待被调线程结束后在继续执行后续代码，timeout为最长等待时间，单位为妙，当不指定时间的时候，就一直等待程序执行完成
# 个人理解：
# join不设置timeout时间时相当于阻塞当前的主线程执行，一直等到子线程执行结束才继续执行主线程，
# 而当设定了timeout时间表示规定了子线程阻塞主线程的时间长短，时间到了就得往下继续执行主线程了


t5 = threading.Thread(target=func, args=(5, 11))  # 创建线程2
t5.start()

print("main thread has over")
# 主线程到这里就完结了，主线程个人理解其实就是整个代码执行的顺序，其中可能在中间分发了线程，那主线程结束之后，等不等待子线程全部结束，与
# 设置守护进程有关
