'''
从该网站 https://www.cnblogs.com/kaituorensheng/p/4445418.html
学习多进程相关知识点

'''
import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + " acquire");
    time.sleep(i)
    print(multiprocessing.current_process().name + " release\n");
    s.release()
    print(multiprocessing.current_process().name + " has already released \n");
    time.sleep(i)
    print(multiprocessing.current_process().name + " has already outed \n");
'''
semaphore对象适用于控制一个仅支持有限个用户的共享资源
当线程完成一次对该semaphore对象的等待（wait）时，该计数值减一；
当线程完成一次对semaphore对象的释放（release）时，计数值加一
当计数值为0，则线程等待该semaphore对象不再能成功直至该semaphore对象变成signaled状态。
semaphore对象的计数值大于0，为signaled状态；计数值等于0，为nonsignaled状态.
'''
if __name__ == "__main__":
    #Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。
    s = multiprocessing.Semaphore(1)
    for i in range(5):
        p = multiprocessing.Process(target = worker, args=(s, i*2))
        p.start() #启动该进程之后，只有当信号量大于0时才能正常运行
        print('process %d is running'%i)