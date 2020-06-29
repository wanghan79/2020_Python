# 函数封装随机数生成和数据筛选,有异常处理
##!/usr/bin/python3
# """
#   Author:  Sq.Chen
#   Purpose: Generate random data set.
#   Created: 2020
# """

import string
import random

def dataSampling(datatype,datarange,num,strlen=6):
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
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                continue
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
        return result
    except Exception as e:
        # 没有单独给每个参数判断错误，不知道怎么整
        print(e)
        print("input is wrong!!!")



def dataScreening(data, datarange):
    new_result=set()
    try:
        for x in data:
            if type(x) is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_result.add(x)
                continue

            elif type(x) is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_result.add(x)
                continue

            elif type(x) is str:
                if x.find(datarange) != -1:
                    new_result.add(x)
                continue
        return new_result
    except Exception as e:
        print(e)
        print('input is wrong!!!')


def apply():
    result1 = dataSampling(float, {0, 100}, 10)
    result1_1 = dataScreening(result1,(5, 50))
    print(result1)
    print(result1_1)

    result2 = dataSampling(int, {0,100}, 10)
    result2_1 = dataScreening(result2, (5, 50))
    print(result2)
    print(result2_1)

    result3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
    result3_1 = dataScreening(result3, 'a')
    print(result3)
    print(result3_1)


apply()