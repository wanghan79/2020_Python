##!/usr/bin/python3
"""
  Author:  ZhengPeng.Han
  Purpose: Realize producer-consumer problem by python
  Created: 3/6/2020
"""
import time
import random

cacheList = []
cacheListLen = 3                #设置缓冲区的最大长度，当缓冲区到达最大长度，生产者就不能再生产

def is_full():                  #判断缓冲区是否已满
    return len(cacheList) == cacheListLen

def Producer():                 #生产者函数，用于生成数据并送入缓冲区
    while True:
        if not is_full():       #如果缓冲区不满，就一直生产下去
            print("--Producer are producing PlayStation4--")
            print("--production completed--")
            cacheList.append('PlayStation4')
        else:                   #如果缓冲区满了，则停止生产并在yield处停止执行函数
            print("--Buffer is full! Production stop--")
            yield

def Consumer(name):             #消费者函数，用于将缓冲区中数据取出
    print("--【%s】is going to buy PlayStation4--" %(name))
    while True:                 #消费者不断尝试获取数据
        item = yield
        print("--【%s】buy %s successfully--" %(name,item))

producer = Producer()           #获得producer的生成器并迭代
next(producer)

consumers = [Consumer("Consumer%s" %(i+1)) for i in range(3)]  #生成多个不同的消费者

for consumer in consumers:      #依次遍历所有的消费者，执行消费过程
    if not cacheList:           #如果缓冲区为空，则提示
        print("--Buffer is empty!--")
    else:                       #如果缓冲区不为空，则执行消费者或生产者
        if not is_full():       #如果缓冲区不满，先生产，再提供消费
            next(producer)
            item = cacheList.pop(0)
            next(consumer)
            consumer.send(item)
        else:                   #如果缓冲区满，则无需生产，直接消费
            item = cacheList.pop(0)
            next(consumer)
            consumer.send(item)