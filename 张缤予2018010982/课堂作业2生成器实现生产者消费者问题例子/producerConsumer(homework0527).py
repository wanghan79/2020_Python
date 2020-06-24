##!/usr/bin/python3
'''

Author: By.Zhang
Purpose: generate prime numbers in a specified range
Created: 27/5/2020

'''

import time
import random

cacheList = []
# 缓冲区的最大值，当缓冲区达到最大长度时，生产者就不能再生产了
cacheListLen = 5

def is_full():
    """
    判断缓冲区队列是否已经满了
    :return: boolean whether the length of cacheList is equal with cachListLen
    """
    return len(cacheList) == cacheListLen


def Producer(name):
    """
    生产者，用于生产数据
    """
    while True:
        if not is_full():
            print("生产者【%s】正在生成游戏机..."%(name))
            # 模拟生产者生产数据需要的时间，随机休眠0~1秒
            time.sleep(random.random())
            print("【%s】已经生产游戏机完成"%(name))
            # 将生产的游戏放到缓冲区
            cacheList.append('游戏机')
        else:
            print('生产足够多了...')
            yield


def Consumer(name):
    """
    消费者，用于处理/消费数据
    """

    print('[%s]正准备购买游戏机'%(name))
    while True:
        item = yield
        print('[%s]购买游戏机成功'%(name))

# producer是一个生成器
producer =Producer("张缤予")
next(producer)

# 列表生成式，生成消费者
consumers = [Consumer("消费者%s"%(i+1)) for i in range(10)]

# 依次遍历所有消费者，给提供游戏机
for consumer in consumers:
    if not cacheList:
        print("目前商店没有游戏库存...")
    else:
        if not is_full():
            next(producer)
        else:
            item = cacheList.pop(0)
            next(consumer)
            consumer.send(item)
