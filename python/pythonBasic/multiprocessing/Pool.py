import multiprocessing
import time

def func(id):
    print('func %d is running'%id)
    time.sleep(2)
    print('func %d has finished'%id)  #一旦有子进程结束，下面马上运行新线程


def useMap():
    pool = multiprocessing.Pool(processes = 2)
    pool.map(func, [1,2,3,4,5]) #用于匹配函数与参数 设置完之后进程池有空位置，就马上运行
                                #map(func, iterable[, chunksize=None]) 其中每个任务func对应的不同参数都写在一个列表里面
                                # Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。


if __name__ == "__main__":
    # pool = multiprocessing.Pool(processes = 3) #设置进程池最大容纳量为3，默认为CPU线程数
    # for i in range(10):
    #     pool.apply_async(func, (i, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    # print('all tasks have been put into the pool') # for 循环一次性把所有的线程都放在pool中，但是部分未运行
    # pool.close()
    # #执行close()之后不会用行的子进程入池
    # #先关闭进程池，然后join()阻塞，等待进程池中的子任务结束
    # pool.join()   #调用join之前，先调用close函数，否则会出错
    useMap()
