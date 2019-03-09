# encoding:utf-8

"""
生产者和消费者例子：Condition对象
"""

import threading
from time import sleep
import random

# 利用condition对象实现线程同步


class Producer(threading.Thread):
    """生产者"""
    def __int__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global x
        sleep(random.randrange(0, 5))  # 线程启动之后，等待1秒之后在执行
        con.acquire()

        if x == 20:  # 获取线程锁之后，判断当前变量为多少，即比如面包师和消费者，每次只生产20个面包放在盒子里，当盒子里面已经由20个面包了，就不生产了
            print("Producer is waiting....")
            con.wait()  # 阻塞当前线程并释放锁,如果有其他的消费者线程在进行中的话，就直接执行消费者线程
            print("Producer resumed", end=' ')

        print("Producer begin produce", end=" ")
        for i in range(20):
            print(x, end=" ")
            x = x + 1
        print(x)
        con.notify_all()  # notify不会自动释放锁，需要手动的release

        con.release()


class Consumer(threading.Thread):
    """消费者"""
    def __int__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global x
        sleep(3)
        con.acquire()
        if x == 0:  # 当没有东西可消费的时候，就处于等待中，并释放锁
            print("Consume waiting。。。"  )
            con.wait()   # 之前这里的线程被阻塞，下面的语句不被执行，那么当生产者释放锁之后，下次拿到锁之后，再执行这里
            print("Consumer resumed", end=' ')

        print("Consumer:", end=' ')
        for i in range(20):
            print(x, end=' ')
            x = x - 1
        print(x)
        con.notify_all()

        con.release()


con = threading.Condition()  # 创建condition对象
x = 0
p = Producer(name='producer')
c = Consumer(name='Consumer')
p.start()
c.start()

sleep(5)
print("all thread has over")
