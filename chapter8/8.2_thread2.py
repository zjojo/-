# -*- encoding:utf-8 -*-
"""
线程同步：获取锁，释放锁，临界区
"""

import threading
import time


class Mythread(threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        """获取到线程锁之后再执行"""
        global x   # 声明全局变量
        lock.acquire()  # 获取锁，进入临界区，这行代码：即线程获取到锁才开始执行下面的代码
        # 疑问点:多核cpu?那同时有多把锁，会不会影响x值的输出，比如线程1在第一个cpu上获得了锁,然后执行，线程2在另外的一个cpu上获取了锁使得
        # 线程1和线程2同时执行这样子？输出了多次发现x的值都是顺序输出
        # 解答：不会的，就算线程1和线程2同时拿到了cpu的锁，需要执行，但是python解释器的锁只允许一个线程使用,所以一个线程执行完成之后，
        # x的值已经发生变化，那么线程2在执行的时候，输出的值是基于上一个线程执行后x的值进行计算
        for i in range(3):
            x = x + i
        time.sleep(2)
        print(x)   # 打印结果顺序打出：3，6，9.。。。30
        lock.release()   # 释放锁  只有等到释放了锁之后，才可以执行下一个线程

    def run(self):
        """不锁定线程锁，自由的由cpu调度执行"""
        global x
        # lock.acquire()  # 注释掉这里，线程不会将锁锁定，任意的由cpu去调度
        for i in range(3):
            x = x + i
        time.sleep(2)
        print(x)   # 打印结果打出：10个30
        # lock.release() # 注释掉这里
        # 打印结果解释：其中time.sleep(2),等待的两秒，相当于线程阻塞了，那么这时候每一个线程执行到这里被阻塞了，因为没有锁定线程锁，
        # cpu就去调度其他的线程执行，
        # 还没等2秒时间呢，最后一个线程已经执行结束了，此时x已经为30了，所以打印出来的每一个线程的值都为30，线程之间是共享内存，共享变量值的

    def run(self):
        """线程内，不等待2秒，随机由调度执行"""
        global x
        # lock.acquire()  # 注释掉这里，线程不会将锁锁定，任意的由cpu去调度
        for i in range(3):
            x = x + i
        # time.sleep(2)  # 注释掉这里，线程内，不阻塞
        print(x)   # 打印结果：随机的3的倍数，不按照顺序
        # lock.release() # 注释掉这里
        # 打印结果解释:相比与上一个例子，等待时间，阻塞线程，这个执行去掉了等待时间，那么cpu任意的去切换线程执行，每一个线程执行到哪里是
        # 不确定的，可能执行了一半，改变了x的值没打印，就切换出去了，下次打印的时候x的值已经被其他线程改变


lock = threading.Lock()   # 创建一个锁对象
t1 = []    # 线程组
for i in range(10):
    t = Mythread()
    t1.append(t)  # 创建线程并并加入线程组

x = 0
for i in t1:
    i.start()   # 线程启动

# 线程对象默认执行的是run方法，所以再类里面写run方法，start之后不用显示的调用run方法
