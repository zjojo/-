# -*- encoding:utf-8 -*-
from threading import Thread
import argparse
import os
from queue import Queue
from shutil import copyfile
import sys

"""
Queue对象实现多线程文件复制，加快文件复制速度
思路：创建一个队列，存放需要复制的文件路径
方法1：实现读取原始路径，并把路径添加值至队列中
方法2：负责从队列中拿出对应的路径，然后判断当前是一个文件还是一个文件夹，如果是一个文件夹，还要判断路径是否存在，需要创建文件夹

用到的技术：函数嵌套定义，文件的操作，命令行参数解析，以及多线程
"""


def copyFile(src, dst, num):
    """多线程复制文件"""
    if not os.listdir(src):
        print("所需复制的文件夹必须存在")
    os.makedirs(dst)  # 创建目标文件夹

    q = Queue(10)  # 仅允许10个文件存放再队列中

    def add(src):
        """将源文件往队列中放"""
        for f in os.listdir(src):  # 返回的是一个上级目录
            print(f)
            # 读取出来的是当前路径下的最后文件名称
            f = os.path.join(src, f)
            print(f)
            if os.path.isfile(f):
                # 队列满了之后，线程自动会阻塞
                q.put(f)
            elif os.path.isdir(f):
                q.put(f)
                # 递归
                add(f)

        for _ in range(num):
            q.put(None)
        # 如何理解

    # 创建并启动添加文件至队列的线程
    t = Thread(target=add, args=(src,))
    t.start()

    def copy(name):
        """获取文件并复制文件到指定文件夹"""
        while True:
            srcItem = q.get()  # 完整的路径名
            if srcItem is None:
                print(name, 'quiting')
                break
            dstItem = srcItem.replace(src, dst)  # 替换原路径为新路径
            print("{0} from {1} ===>{2}".format(name, srcItem, dstItem))

            #复制文件s
            if os.path.isfile(srcItem):
                """如果是文件，需要创建目标文件夹"""
                disDir = os.path.split(dstItem)[0]  # 分割目录名和文件名?
                if not os.path.isdir(disDir):
                    # 获得的存放的地址是不是一个目录，
                    try:
                        os.makedirs(disDir)
                    except FileExistsError:
                        pass
                copyfile(srcItem, dstItem)

            else:
                print("获取到的是文件夹，直接创建目标文件夹")
                os.makedirs(dstItem)

    for _ in range(num):
        c = Thread(target=copy, args=('The thread ' + str(_),))
        c.start()


if __name__ == "__main__":
    parser =argparse.ArgumentParser(description= "Copy file from src to dst")
    parser.add_argument('-s', '--src'),  # default=''
    parser.add_argument('-d',  '--dst'),  # default=''
    parser.add_argument('-n', '--num', default='5')
    args = parser.parse_args()

    if (args.src is not None) and (args.dst is not None):
        copyFile(args.src, args.dst, int(args.num))
    else:
        print("Please use the following command to see how to use")
        print(" "+sys.argv[0] + '-h')


