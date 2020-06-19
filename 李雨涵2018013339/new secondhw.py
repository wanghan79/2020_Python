#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 17:42
# @Author  : liyuhan
# @File    : new secondhw.py
"""
   Author:liyuhan
   Purpose:Generate random data set by decorator.（改类型错误报错)
   Created:2020
"""
import random
import string

def DataSampling(func):
    def wrapper(datatype, datarange, num, *condition, strlen=10):
        '''
            :Description: Generate a given condition random data set.
            :param datatype: data type like int,float,string
            :param datarange:  iterable data set
            :param num:  number
            :param condition:
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
            return func(result, *condition)
        except TypeError:
            print("类型错误")
        except NameError:
            print("变量不存在")
        except Exception as e:
            print(e)
    return wrapper


@DataSampling
def DataScreening(data, *condition):
    '''
        :param data: data set above
        :param condition:
        :return: a data set
    '''
    newresult = set()
    try:
        for item in data:
            if type(item) is int:
                it = iter(condition)
                if next(it) <= item <= next(it):
                    newresult.add(item)
            elif type(item) is float:
                it = iter(condition)
                if next(it) <= item <= next(it):
                    newresult.add(item)
            elif type(item) is str:
                for temp in condition:
                    if temp in item:
                        newresult.add(item)
        print(newresult)
    except TypeError:
        print("类型错误")
    except NameError:
        print("变量不存在")
    except Exception as e:
        print(e)

print("筛选int类型随机数：")
DataScreening(int,(1,1000),10,10,500)
print("筛选float类型随机数：")
DataScreening(float,(1,1000),10,10,500)
print("筛选随机字符串：")
DataScreening(str, string.ascii_letters + string.digits + "@#$!", 10,'a')#有时会为空
print("类型异常：")
DataScreening(int,(1,1000),10,(10,500))#前面用*condition指针时筛选范围10,500不能加括号，否则会抓异常报类型错误！！！但是没搞明白为啥会这样
print("下标异常：")
DataScreening(int,(1000,600),10,10,500)#异常：random的下标  第一个大于第二个