'''
管道一个入口一个出口
如果出口被多个任务调用，则数据被取完之后就不存在了，现在先得，如果在pipeOut1 和 pipeOut2只有一个管道能拿到数据

'''
import multiprocessing
import time

def pipeIn(pipe):
    while True:
        for i in range(10):
            print("send: %s" %(i))
            pipe.send(i)
            time.sleep(1)

def pipeOut1(pipe):
    while True:
        print('pipeOut1 get message',pipe.recv())
        time.sleep(1)

def pipeOut2(pipe):
    while True:
        print('pipeOut2 get message',pipe.recv())
        time.sleep(1)

if __name__ == "__main__":
    pipe = multiprocessing.Pipe() #生成一个元祖，只有两个元素 一个入口，一个出口
    p1 = multiprocessing.Process(target=pipeIn, args=(pipe[0],))
    p2 = multiprocessing.Process(target=pipeOut1, args=(pipe[1],))
    p3 = multiprocessing.Process(target=pipeOut2, args=(pipe[1],))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()