# single_threaded.py
import time
import os
from threading import Thread
from multiprocessing import Process
import timer


def singlethreadtest():
    COUNT1 = 100000000

    def countdown1(n):
        while n>0:
            n -= 1

    start = time.time()
    countdown1(COUNT1)
    end = time.time()
    print('Single threaded:  -', end - start)


# -------------------------------------------------------------------------------------------
# multi_threaded.py


def multithreadtest():
    COUNT2 = 100000000

    def countdown2(n):
        while n>0:
            n -= 1

    t1 = Thread(target=countdown2, args=(COUNT2//2,))
    t2 = Thread(target=countdown2, args=(COUNT2//2,))

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print('Multi threaded:   -', end - start)

# --------------------------------------------------------------------------------------------


def countdown3(n):
    while n>0:
        n -= 1
        # proc = os.getpid()
        # print('process id: {0}'.format(proc))


if __name__ == '__main__':
    singlethreadtest()
    multithreadtest()
    numbers = [25000000,25000000,25000000,25000000]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=countdown3, args=(number,))
        procs.append(proc)
    start = time.time()

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()
    end = time.time()
    print('Multi processing: -', end - start)