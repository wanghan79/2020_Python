##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:generate random data set.
      Created:25/4/2020
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
        result = set()
        if datatype is int:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
                    continue
        elif datatype is float:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
                    n = len(result)
                    continue
        elif datatype is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
                    continue
        return result
    except ValueError:
        print("传入无效的参数")
    except MemoryError:
        print("内存溢出错误")
    except Exception as r:
        print('未知错误 %s' % (r))
    finally:
        print("hello world!")

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
     finally:
         print("hello world!")

def apply():
    #Str
    result = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
    print(result)
    a2 = dataScreening(result, 'c')
    print(a2)
    #Int
    b1 = dataSampling(int, [0, 100], 20)
    print(b1)
    b2 = dataScreening(b1, 20, 50)
    print(b2)
    #Float
    c1 = dataSampling(float, [0.0, 100.0], 20)
    print(c1)
    c2 = dataScreening(c1, 30.0, 50.0)
    print(c2)
    #异常
    d1 = dataSampling(int, 20, 2.5)
    print(d1)

apply()