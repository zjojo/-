# encodig:utf-8

"""
python中的数据结构：堆，栈，队列，堆，队列，栈均有各自的特点：
堆：类似于一个二叉树，当前节点的值总是小于等于子节点的值
栈：可以使用列表来实现栈，但是有缺点，就是列表元素pop模拟出栈，要是列表为空，会报异常
队列：队列有个特性，当指定队列大小后，如果队列已满，再往里面添加元素，且不指定超时时间则一直会出处于等待中，从队列获取元素也是一样的，要是队列中没有元素，且不设置超时时间，则一直等待，直到队列中有元素了则返回
队列除过一般队列外，还有优先队列，双端队列，优先队列会根据插入数据，自动进行排序，排序的规则有待继续学习
"""

# 堆
import heapq
import random

data = list((range(10)))  # range()是生成一个range 对象，再转化为list
random.shuffle(data)
# random.shuffle：随机打乱顺序的方法，再原列表处打乱，不是生成新的列表

print(data)
heap = []  # 定义一个空的堆
for n in data:  # 建堆
    heapq.heappush(heap, n)
print(heap)

heapq.heappush(heap, 0.5)  # 新的元素入堆
heapq.heappop(heap)  # 出堆，自动重建
print(heap)
# 堆的结构与列表，队列不一致，相当于一个二叉树，节点的元素值小于等于所有子节点的值，所以加入新的元素之后，会自动调整，使其满足二叉树节点值的规则


# 队列，队列有普通队列(先进先出），后进先出队列，优先级队列，还有双端队列

import queue  # 普通队列

#  普通队列
q = queue.Queue(maxsize=6)  # 可以指定队列长度，未指定长度的队列,队列可以一直增加元素
q.put(0)  # 入队，
q.put(1)
q.put(2)
print(q.queue)  # 查看队列中的元素
print(q.get())  # 出队
q.put(5, timeout=2)
# 当队列满了的时候，再添加元素，队列会无法再添加进去，一直处于等待中，添加timeout参数会等待timeooout后，
# 返回队列已满的结果，不添加则一直处于等待中，直到队列有空闲

# 后进先出队列
from queue import LifoQueue  # 后进先出队列

lq = LifoQueue()
lq.put(0)  # 入队，
lq.put(1)
lq.put(2)
lq.get()  # 删除并返回末尾的元素，当队列为空时，一直处于等待状态，直到队列中有元素可以弹出

# 优先级队列
from queue import PriorityQueue  # 优先级队列

pq = PriorityQueue()
pq.put(1)
pq.put(4)
pq.put(5)
# 入队列与出队列的方式与上面一致，不同之处在于优先级队列，后面进入的元素会按照优先级进行重排，具体的优先级规则需要重新补充


# 双端队列
from collections import deque  # 双端队列,添加元素的方法与列表一致

dq = deque(maxlen=5)
for n in range(6):
    dq.append(n)
print(dq)
dq.append(8)  # 队列满，元素自动溢出，插入新的元素
print(dq)

# 可以指定从左侧还是右侧(默认的即右侧)添加元素，如果左侧添加，到达最大长度，则从右侧溢出
dq.appendleft(18)
print(dq)


