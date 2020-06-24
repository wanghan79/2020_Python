##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Producer consumer problem realize by generator.
  Created: 01/6/2020
"""
import threading
import time
import random

num = 3   #num缓冲池的容量
buffer=[]
lock = threading.Lock()

class Producer(threading.Thread):
    def run(self):
        global buffer
        while(True):
            flag = 0
            item=random.randint(1,100)
            lock.acquire()
            if len(buffer)<num:
                buffer.append(item)
                flag=1
            lock.release()
            time.sleep(0.2)
            if flag==1:
                yield "Producer produce {0} products".format(item)
            else:
                yield "The buffer pool is full. Please produce later"

class Consumer(threading.Thread):
    def run(self):
        global buffer
        while(True):
            flag=0
            lock.acquire()
            if len(buffer)>0:
                item=buffer[0]
                del buffer[0]
                flag=1
            lock.release()
            time.sleep(0.2)
            if flag==1:
                yield "Consumer consume {0} product".format(item)
            else:
                yield "The buffer pool is empty. Please consume later "

p=Producer()
c=Consumer()
print(next(p.run()))
print(next(p.run()))
print(next(p.run()))
print(next(c.run()))
print(next(p.run()))
print(next(p.run()))
print(next(c.run()))
print(next(c.run()))
print(next(c.run()))
print(next(c.run()))