#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 17:45
# @Author  : liyuhan
# @File    : new finalhw.py
"""
   Author:liyuhan
   Purpose:Generate random data set by mangodb.
   Created:2020
"""
import string
import random
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["final"]
mycol =mydb['table']
mycol.drop()#更新数据 否则输出不变!!!


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

    newresult = []
    try:
        for item in data:
            if type(item) is int:
                it = iter(datarange)
                if next(it) <= item <= next(it):
                    newresult.append(item)
                continue
            elif type(item) is float:
                it = iter(datarange)
                if next(it) <= item <= next(it):
                    newresult.append(item)
                continue
            elif type(item) is str:
                for temp in datarange:
                    if temp in item:
                        newresult.append(item)
                continue
        return newresult
    except TypeError:
        print("类型错误")
    except NameError:
        print("变量不存在")
    except Exception as e:
        print(e)

def apply():

    #int类型
    result_int = DataSampling(int, [0, 1000], 10)
    # result1 = set()
    # for item in range(0, 10):
    #     result1.add(next(result_int))
    # print(result1)
    result1 = {'type': 'int', 'data': DataScreening(result_int, 100, 500)}
    mycol.insert_one(result1)

    #float类型
    result_float = DataSampling(float, [0, 1000], 10)
    result2 = {'type': 'float', 'data': DataScreening(result_float, 100, 500)}
    mycol.insert_one(result2)

    #字符串类型
    result_str = DataSampling(str,  string.ascii_letters + string.digits + "@#!$", 10)
    result3 = {'type': 'str', 'data': DataScreening(result_str, 'a')}
    mycol.insert_one(result3)


apply()

ans_result1 = mycol.find_one({"type": 'int'})
print("筛选int类型随机数")
if ans_result1:
    print(ans_result1)
else:
    print("不存在满足条件的数据")


ans_result2 = mycol.find_one({"type": 'float'})
print("筛选float类型随机数")
if ans_result2:
    print(ans_result2)
else:
    print("不存在满足条件的数据")

ans_result3 = mycol.find_one({"type": 'str'})
print("筛选字符串类型随机数")
if ans_result3:
    print(ans_result3)
else:
    print("不存在满足条件的数据")