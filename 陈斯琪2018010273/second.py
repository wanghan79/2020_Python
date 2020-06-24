# 随机数封装为修饰函数，修饰数据筛选函数
##!/usr/bin/python3
# """
#   Author:  Sq.Chen
#   Purpose: Decorator & Generate random data set.
#   Created: 16/6/2020
# """

import string
import random

def create(func):
    def dataSampling(datatype, datarange, num,condition, strlen=6):
        '''
            :Description: Generate a given condition random data set.
            :param datatype:
            :param datarange: iterable data set
            :param num: number
            :param condition: Pass to next function
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
            return func(result,condition) #choice传给dataScreening函数的，就是没有
        except Exception as e:
            # 没有单独给每个参数判断错误，不知道怎么整
            print(e)
            print("input is wrong!!!")
    return dataSampling


@create
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


print(dataScreening(int,{1,100},10,(5,80)))
print(dataScreening(float,{1,100},10,(5,80)))
print(dataScreening(str,string.ascii_letters + string.digits + "@#$!",10,'a'))