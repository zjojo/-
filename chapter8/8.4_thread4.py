# encoding:utf-8
import threading
from queue import Queue

"""
Queue对象实现生产者消费者实例
"""

print("The way two".center(100, '*'))


class Producer(threading.Thread):
    def __int__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global myque
        print(self.getName(),'put',self.getName(), 'to queue')
        myque.put(self.getName())


class Consumer(threading.Thread):
    def __int__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def consumer(self):
        global myque
        print(self.getName(),'get', myque.get(), 'from queue')  # 从队列获取值


myque = Queue()
plist = []
clist = []
for i in range(20):
    p = Producer(name='Producer'+str(i))
    c = Consumer(name='Consumer' + str(i))
    plist.append(p)
    clist.append(c)  # 创建线程对象并添加值队列中

for i in plist:
    i.start()
    i.join()   # 阻塞当前线程，等待每一个子线程结束，即这个循环才会继续往下执行
for j in clist:
    j.start()
    j.join()  # 消费者的线程也只有等到生产者的线程执行完成之后才可以执行


# 以上用到了线程阻塞实现的线程同步，没有实际用到queue 的特性,下面直接使用queue的，put，然后get
print("The way two".center(100, '*'))


class Provider(threading.Thread):
    """供货商"""
    def __int__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global mq
        for m in range(10):
            print('Provider put {0} in queue'.format(m))
            mq.put(m)


class Sales(threading.Thread):
    """消费"""
    def __int__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global mq
        for n in range(10):
            print('Sales get {0} from queue'.format(n))
            mq.get()


mq = Queue()
pv = Provider(name='Provider')
s = Sales(name='Sales')
pv.start()
s.start()
