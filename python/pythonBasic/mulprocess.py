from multiprocessing import Process
import time
import os
import multiprocessing

def info():
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    # info()
    # time.sleep(3)
    print('hello', name)


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    # info()
    # p1 = multiprocessing.Process(target=f, args=('Bob',))
    p1 = ClockProcess(1)
    lock = multiprocessing.Lock()
    
    p2 = multiprocessing.Process(target=f, args=('Job',))
    p3 = multiprocessing.Process(target=f, args=('Steve',))
    # p1.daemon = False
    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    p2.join()


    print("END!!!!!!!!!!!!!!!!!")
