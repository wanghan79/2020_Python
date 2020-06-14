##!/usr/bin/python3
"""

Author: BinYuZhang      2018010982
Purpose:Generate random data set by decoration.
Created:6/5/2020
"""

import random
import string

def dataSampling(func):
    '''
    :Description: a decoration
    :param func: the func you want to run
    :return: wrapper
    '''
    def wrapper(datatype, datarange, num, *conditions, strlen=8):
        '''
        :Description:Generate a given condition random data set.
        :param datatype: the data type you want to sample including int, float,str.
        :param datarange: iterable data set
        :param num: the number of data you need
        :param strlen: the length of each string you want to generate
        :return: func you input in dataSampling
        '''
        print("Generate data")
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) <num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return func(result, *conditions)
    return wrapper


@dataSampling
def dataScreening(data, *conditions):
    '''
    :Description: decorated function ; according the conditions to pick the correct data in dataSampling
    :param data: iterable data set
    :param conditions: the condition such as range or string you want to screen from a data set
    :return: a data set
    '''
    print("Screen data")
    result = set()
    for i in data:
        if type(i) is int:
            it = iter(conditions)
            if next(it)<=i and next(it)>=i:
                result.add(i)
        elif type(i) is float:
            it = iter(conditions)
            if next(it)<=i and next(it)>=i:
                result.add(i)
        elif type(i) is str:
            for teststr in conditions:
                if teststr in i:
                    result.add(i)
    return result



str_ex = string.ascii_letters + string.digits + string.punctuation
# int类型例子
print(dataScreening(int, [0,280], 200, 10,80))
# float类型例子
print(dataScreening(float, [0,200], 100, 20,70))
# # str类型例子
print(dataScreening(str, str_ex, 1000, 'at', 'no'))


