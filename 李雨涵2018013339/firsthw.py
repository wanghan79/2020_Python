#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 17:45
# @Author  : liyuhan
# @File    : firsthw.py
"""
   Author:liyuhan
   Purpose:Generate random data set.
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
    except TypeError:
        print("类型错误")
    except NameError:
        print("变量不存在")
    except Exception as e:
        print(e)
    # finally:    #每次抓异常都会运行到finally！！所以不加了
    #     print("OKK")

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
    # finally:
    #     print("OKK")

def apply():
        #int类型
        print("int类型随机数")
        result1 = DataSampling(int, (1, 1000), 10)
        print(result1)
        print("筛选int类型随机数")
        ans_result1 = DataScreening(result1, 100, 500)
        if ans_result1:
            print(ans_result1)
        else:
            print("不存在满足条件的数据")


        #float类型
        print("float类型随机数")
        result2 = DataSampling(float, (1, 1000), 10)
        print(result2)
        print("筛选float类型随机数")
        ans_result2 = DataScreening(result2, 100, 500)
        if ans_result2:
            print(ans_result2)
        else:
            print("不存在满足条件的数据")

        #字符串类型
        print("随机字符串")
        result3 = DataSampling(str, string.ascii_letters + string.digits + "@#!$", 10)
        print(result3)
        print("筛选随机字符串")
        ans_result3 = DataScreening(result3, 'a')
        if ans_result3:
            print(ans_result3)
        else:
            print("不存在满足条件的字符串")


apply()




