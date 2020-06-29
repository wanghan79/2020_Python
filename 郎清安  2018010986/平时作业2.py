##!/usr/bin/python3
"""
  Author:  QingAnLang
  Purpose: Generate random data set.
  Created: 1/6/2020
"""
import random
import string

def datasampling(func):
    '''
        :Description: Generate a given condition random data set.
        :param datatype: dddd
        :param datarange: iterable data set
        :param num: number
        :param strlen:
        :return: a dataset
        '''
    def wrapper(datatype, datarange, num, *args,strlen=8):
        result = set()
        if datatype is int:
            while len(result) != num:
                it = iter(datarange)  # 顺序型可迭代的数据变量，迭代器
                item = random.randint(next(it), next(it))  # next全局函数
                result.add(item)
        elif datatype is float:
            while len(result) != num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) != num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        print('筛选前：',result)
        return func(result,*args)
    return wrapper
@datasampling
def dataScreening(data,*args):
    result = set()
    for item in data:
        if type(item) is int:
            i = iter(args)
            if next(i) <= item <= next(i):
                result.add(item)
        elif type(item) is float:
            i = iter(args)
            if next(i) <= item <= next(i):
                result.add(item)
        elif type(item) is str:
            for i in args:
                if i in item:
                    result.add(item)
    print('筛选后:',result)

dataScreening(int,(1,100),30,40,60)
dataScreening(float,(1,100),30,40,60)
dataScreening(str, string.ascii_letters+string.digits+"@#$!",100,'s')