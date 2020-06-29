#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   databaseSamplingAndScreening.py
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/20 18:59   Linyf      1.0         None
'''
# !/usr/bin/python3

import string
import pymongo
from dataScreening import dataScreening
from Factory import elementSamplingFactory


def databaseSamplingAndScreening(totInt = 1000,totFloat = 1000,totStr = 1000,conditionInt = [10,30], conditionFloat = [10,30],conditionStr = 'at'):
    '''
    :param totInt:生成整型的个数
    :param totFloat: 生成浮点型的个数
    :param totStr: 生成字符串类型的个数
    :param conditionInt: 筛选整型的范围
    :param conditionFloat: 筛选浮点型的范围
    :param conditionStr: 筛选字符串型的范围
    :return: 包含所筛选数据的集合
    '''
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient["randomEleDB"]
    mycol = mydb["randomEleList"]

    mycol.drop()

    factoryInt = elementSamplingFactory([0, 100], 1)
    factoryFloat = elementSamplingFactory([0, 100], 1)
    factoryStr = elementSamplingFactory(string.ascii_letters,1,8)

    cnt = 0
    while cnt != totInt:
        intList = factoryInt.randomIntSampling()
        for x in intList:
            mycol.insert_one({"cnt":cnt,"type":"int","dig":x})
            cnt=cnt+1

    cnt = 0
    while cnt != totFloat:
        floatList = factoryFloat.randomFloatSampling()
        for x in floatList:
            mycol.insert_one({"cnt":cnt,"type":"float","dig":x})
            cnt=cnt+1

    cnt = 0
    while cnt != totStr:
        strList = factoryStr.randomStrSampling()
        for x in strList:
            mycol.insert_one({"cnt":cnt,"type":"str","dig":x})
            cnt=cnt+1

    ans=[]
    for x in mycol.find():

        if x['type'] == 'int':
            if dataScreening(x['dig'],conditionInt).screeningInt():
                ans.append(x['dig'])
        if x['type'] == 'str':
            if dataScreening(x['dig'],conditionStr).screeningStr():
                ans.append(x['dig'])
        if x['type'] == 'float':
            if dataScreening(x['dig'],conditionFloat).screeningFloat():
                ans.append(x['dig'])

    mycol.drop()
    return ans










