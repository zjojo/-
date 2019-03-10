# encoding:utf-8
"""
通过Event对象实现线程同步，模拟消费者和生产者的实例
"""
import threading
from time import sleep


class mythread(threading.Thread):
    """Event对象"""
    def __int__(self):
        threading.Thread.__init__(self)

    def run(self):
        if not event.isSet():
            event.set()
            for i in range(10):
                print(self.getName(), i)
            event.clear()
        else:
            print(self.getName(), "waiting")


event = threading.Event()
t1 = mythread(name = "Thread1")
t2 = mythread(name = "Thread2")
t1.start()
t2.start()
sleep(2)  # 为了让最后一句话最后输出，等待5秒
print("Producer and Consumer".center(50, '='))



class consumer():
    """消费者"""
    def __int__(self):
        pass

    def run(self):
        pass

