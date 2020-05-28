'''
创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
Queue([maxsize])创建共享的进程队列。 默认为不限制队列大小
q.put(block,timeout) 往队列里面放数据 block = True 时，若队列没有位置，则等待直到有空余位置存放
                    timeout 为超时时间
q.get(block,timeout) 往队列里面取数据 block = True 时，若队列没有数据，则等待直到有数据进来
                    timeout 为超时时间

JoinableQueue() 在 Queue()基础上改进
每个读取的任务拿到数据之后，就调用q.task_done()任务，告诉队列我以及完成读取任务了
对了的放置任务q.join() 一直阻塞，知道队列的所有数据都没读取完成，解除join()阻塞
'''
import multiprocessing
import time

def writer_proc(q):
    try:
        # time.sleep(1)
        q.put(1, block = False)
        q.join()
        print('ok i know you have got the data')
    except:
        pass

def reader_proc(q):
    try:

        print(q.get(block = True))
        print('has got the data')
        q.task_done()

    except:
        print('has not get the data')
        pass

if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()

    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    reader.join()
    writer.join()