#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 14:30
# @Author  : liyuhan
# @File    : thirdhw.py
"""
   Author:liyuhan
   Purpose:Generate random data set by generator.
   Created:2020
"""

import random
import string

def DataSampling(datatype,datarange,num,strlen=10):
    '''
    :Description: Generate a given condition random data set.
    :param datatype: data type like int,float,string
    :param datarange:  iterable data set
    :param num:  number
    :param strlen:  length
    :return:  a dataset
    '''

    result = set()
    try:
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
                continue
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
    except TypeError:
        print("类型错误")
    except NameError:
        print("变量不存在")
    except Exception as e:
        print(e)


def DataScreening(data,*datarange):
    '''

    :param data: data set above
    :param datarange: iterable data set
    :return: a data set
    '''
    newresult = set()
    try:
        for item in data:
            if type(item) is int:
                it = iter(datarange)
                if next(it) <= item <= next(it):
                    newresult.add(item)
                continue
            elif type(item) is float:
                it = iter(datarange)
                if next(it) <= item <= next(it):
                    newresult.add(item)
                continue
            elif type(item) is str:
                for temp in datarange:
                    if temp in item:
                        newresult.add(item)
                continue
        return newresult
    except TypeError:
        print("类型错误")
    except NameError:
        print("变量不存在")
    except Exception as e:
        print(e)

def apply():
    # int类型
    result1 = set()
    print("int类型随机数")
    result1_1 = DataSampling(int, (1, 1000), 10)
    for item in range(0,10):
        result1.add(next(result1_1))
    print(result1)
    print("筛选int类型随机数")
    ans_result1 = DataScreening(result1, 100, 500)
    if ans_result1:
        print(ans_result1)
    else:
        print("不存在满足条件的数据")

    # float类型
    result2 = set()
    print("float类型随机数")
    result2_2 = DataSampling(float, (1, 1000), 10)
    for item in range(0,10):
        result2.add(next(result2_2))
    print(result2)
    print("筛选float类型随机数")
    ans_result2 = DataScreening(result2, 100, 500)
    if ans_result2:
        print(ans_result2)
    else:
        print("不存在满足条件的数据")

    # 字符串类型
    result3 = set()
    print("随机字符串")
    result3_3 = DataSampling(str, string.ascii_letters + string.digits + "@#!$", 10)
    for item in range(0,10):
        result3.add(next(result3_3))
    print(result3)
    print("筛选随机字符串")
    ans_result3 = DataScreening(result3, 'a')
    if ans_result3:
        print(ans_result3)
    else:
        print("不存在满足条件的字符串")

apply()