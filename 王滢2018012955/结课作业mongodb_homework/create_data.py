##!/usr/bin/python3
"""
Author: Ying Wang
Purpose:
Created:21/6/2020
"""
import random
import string
def dataSampling(datatype, datarange, num, strlen=8):#固定参数；可变参数 *args；默认参数；关键字参数 **kwargs
    '''
    :Description: Generate a given condition random data set.
    :param datatype:
    :param datarange: iterable data set
    :param num: number
    :param strlen:
    :return: a dataset
    '''
    result = set()
    try:
        for index in range(0, num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
                continue
            elif datatype is float:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
            else:
                continue
    except (OverflowError,IOError):
        print('process exception')
    finally:
        return result

def apply():
    result5 = set()
    try:
         #字符串型
        c = dataSampling(str, string.ascii_letters + string.digits, 2000, 20)
        for x in range(0, 2000):
            result5.add(next(c))

    except Exception as ex:
        print(ex)

    finally:
        return result5
