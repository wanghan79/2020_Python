##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:generate random data set.
      Created:30/5/2020
"""
import random
import string
from filecmp import cmp

def dataSampling(func):
    '''
          :Description:Generate a given condition random data set.
          :param datatype: dddd
          :param datarange: iterable data set
          :param num:number
          :param strlen:
          :return:a dataset
       '''
    try:
        def wrapper(datatype, datarange, num, *args, strlen=1):
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
                    continue
            elif datatype is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
                    continue
            print('生成的数据：', result)
            return func(result, *args)
    except ValueError:
        print("传入无效的参数")
    except MemoryError:
        print("内存溢出错误")
    except Exception as r:
        print('未知错误 %s' % (r))
    finally:
        print("hello world!")
    return wrapper
@dataSampling
def dataScreening(data, *args):
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
            print("筛选后的数据：", result)
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
 #str
 print(dataScreening(str, string.ascii_letters + string.digits + "@#$!", 20, 't'))
 #int
 print(dataScreening(int, [0, 100], 20, 20, 50))
 #float
 print(dataScreening(float, [0.0, 100.0], 20, 30.0, 50.0))
apply()