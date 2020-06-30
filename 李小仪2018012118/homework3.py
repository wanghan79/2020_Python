##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:generate random data set.
      Created:20/6/2020
"""
import random
import string
from filecmp import cmp


def dataSampling(datatype, datarange, num, strlen=1):
    '''
       :Description:Generate a given condition random data set.
       :param datatype: dddd
       :param datarange: iterable data set
       :param num:number
       :param strlen:
       :return:a dataset
    '''
    try:
        #result = set()
        for index in range(0, num):
            if datatype is int:
                        it = iter(datarange)
                        item = random.randint(next(it), next(it))
                        #result.add(item)
                        yield item
                        continue
            elif datatype is float:
                        it = iter(datarange)
                        item = random.uniform(next(it), next(it))
                        #result.add(item)
                        yield item
                        continue
            elif datatype is str:
                        item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                        #result.add(item)
                        yield item
                        continue
            #return result
    except ValueError:
        print("传入无效的参数")
    except MemoryError:
        print("内存溢出错误")
    except Exception as r:
        print('未知错误 %s' % (r))
def dataScreening(data, *args):#*args
     try:
            result = set()
            for i in data:
                if type(i) is int:
                    it = iter(args)
                    if next(it) <= i <= next(it):
                        result.add(i)
                    continue
                elif type(i) is float:
                    it = iter(args)
                    if next(it) <= i <= next(it):
                        result.add(i)
                        continue
                elif type(i) is str:
                    it = iter(args)
                    if i == next(it):
                        result.add(i)
                        continue
            return result
     except ValueError:
         print("传入无效的参数")
     except MemoryError:
         print("内存溢出错误")
     except Exception as r:
         print('未知错误 %s' % (r))

def apply():
    #Str
    b1 = set()
    b2 = set()
    for index in range(0, 10):
        item = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
        b1.add(next(item))
        print(item)
    print("生成的数据：")
    print(b1)
    b2 = dataScreening(b1, 20, 50)
    print("筛选后的数据：")
    print(b2)
    #Int
    result = set()
    sult = set()
    for index in range(0,10):
     item = dataSampling(int, [0, 100], 10)
     result.add(next(item))
    print("生成的数据：")
    print(result)
    sult = dataScreening(result, 20, 50)
    print("筛选后的数据：")
    print(sult)
    #Float
    a1 = set()
    a2 = set()
    for index in range(0, 10):
      item = dataSampling(float, [0.0, 100.0], 10)
      a1.add(next(item))
    print("生成的数据：")
    print(a1)
    a2 = dataScreening(a1, 30.0, 50.0)
    print("筛选后的数据：")
    print(a2)
apply()