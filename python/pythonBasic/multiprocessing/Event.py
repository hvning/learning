'''
Event用来实现进程间同步通信。
事件event运行的机制是:全局定义了一个Flag，
如果Flag值为 False，当程序执行event.wait()方法时就会阻塞 停在原地等待，
如果Flag值为True时，程序执行event.wait()方法时不会阻塞继续执行。
wait()方法:wait是否阻塞是看event对象内部的Flag的值。
set()方法:将Flag的值改成True。
clear()方法:将Flag的值改成False。
is_set()方法:判断当前的Flag的值。
'''

import multiprocessing
import time

def task1(e):
    print("task1--: starting\n")
    e.wait()
    print("task1--: e.is_set()->" + str(e.is_set()))

def task2(e):
    print("task2--: starting\n")
    e.wait(3)
    print("task2--: e.is_set()->" + str(e.is_set()))

if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = "block",
            target = task1,
            args = (e,))

    w2 = multiprocessing.Process(name = "non-block",
            target = task2,
            args = (e,))
    e.clear() #设置flag 为 False，则任务wait(t)的时候就卡住了，其中 参数t为超时时间
    w1.start()
    w2.start()
    time.sleep(5)
    e.set()
    print("main: event is set")
