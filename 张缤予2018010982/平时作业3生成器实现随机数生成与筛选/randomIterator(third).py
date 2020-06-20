##!/usr/bin/python3
"""

Author: By.Zhang
Purpose:Generate random data set by an Iterator.
Created:20/6/2020
"""

import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description:Generate a given condition random data set.
    :param datatype: the data type you want to sample including int, float,str.
    :param datarange: iterable data set
    :param num: the number of data you need
    :param strlen: the length of each string you want to generate
    '''
    if datatype is int:
        for i in range(0, num):
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item
    elif datatype is float:
        for i in range(0, num):
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
    elif datatype is str:
        for i in range(0, num):
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item


def dataScreening(data, *conditions):
    '''
    :Description: according the conditions to pick the correct data in dataSampling
    :param data: iterable data set
    :param conditions: the condition such as range or string you want to screen from a data set
    :return: a data set
    '''
    result = set()
    # Screening
    for i in data:
        if type(i) is int:
            it = iter(conditions)
            if i>= next(it) and i<=next(it):
                result.add(i)
        elif type(i) is float:
            it = iter(conditions)
            if i>= next(it) and i<=next(it):
                result.add(i)
        elif type(i) is str:
            for teststr in conditions:
                if teststr in i:
                    result.add(i)
    return result


def apply():
    try:
        # int类型实例
        result_1 = set()
        data_int = dataSampling(int, (0, 280),100)
        for i in range(0, 100):
            result_1.add(next(data_int))
        print('随机生成100个在0~280内的整数:')
        print(result_1)
        print('筛选其中在10~50之间的数:')
        print(dataScreening(result_1, 20, 50))
        print('\n')

        # float类型实例
        result_2 = set()
        data_float = dataSampling(float, (0, 200), 100)
        for i in range(0,100):
            result_2.add(next(data_float))
        print('随机生成100个在0~200内的浮点数:')
        print(result_2)
        print('筛选其中在20~60之间的数:')
        print(dataScreening(result_2, 20, 60))
        print('\n')

        # str类型实例
        str_ex = string.ascii_letters + string.digits + string.punctuation
        result_3 = set()
        data_str = dataSampling(str, str_ex, 1000, 11)
        for i in range(0,1000):
            result_3.add(next(data_str))
        print('随机生成1000个字符串长度为11的字符串:')
        print(result_3)
        print('筛选其中含有‘at’或者‘no’的字符串:')
        print(dataScreening(result_3, 'at', 'no'))
        print('\n')
        
        # 异常实例（执行next()的次数超出范围时）
        result_4 = set()
        data_int = dataSampling(int, (0, 280), 100)
        for i in range(0, 200):
            result_4.add(next(data_int))
        print(result_4)
        print(dataScreening(result_4, 20, 50))
        print('\n')
    except StopIteration:
        print('Maybe iteration is out of range.')


apply()
