from queue import Queue
import time
import random
import threading

def writeQ(queue):
    print('producing object for Q...')
    queue.put('xxx',1)
    print("producer ,size now",queue.qsize())

def readQ(queue):
    val=queue.get(1)
    print('consumed object from Q... size now',queue.qsize())

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        time.sleep(random.randint(1,3))

def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        time.sleep(random.randint(2,5))

funcs=[writer,reader]
nfuncs=range(len(funcs))

def main():
    nloops=random.randint(2,5)
    q=Queue(32)
    threads=[]
    for i in nfuncs:
        t=threading.Thread(target=funcs[i],args=(q,nloops))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print('all DONE')

if __name__=='__main__':
    main()