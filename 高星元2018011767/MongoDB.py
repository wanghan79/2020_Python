#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : GaoXingyuan
# @FileName: MongoDB.py
# @Software: PyCharm

import pymongo
import random
import string



def dataSampling(datatype,datarange,num,strlen=8):

        if datatype is int:
            for i in range(num):
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                yield  item
        elif datatype is float:
            for i in range(num):
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                yield  item
        elif datatype is str:
            for i in range(num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield  item


def apply():

    # 创建数据库
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["minghuiDB"]

    dblist = myclient.list_database_names()
    # dblist = myclient.list_database.names()
    if 'minghuiDB' in dblist:
        print('数据库已存在！')
    print('\n')
    mycol = mydb["sites"]
    mycol.drop()
    data_int = dataSampling(int, [0, 122], 20)
    data_float = dataSampling(float, [0, 122], 20)
    data_str = dataSampling(str, string.ascii_letters, 20)

    for mydict_int in data_int:
        mycol.insert_one({'data': mydict_int, 'datatype': 'int'})
    for mydict_float in data_float:
        mycol.insert_one({'data': mydict_float, 'datatype': 'float'})
    for mydict_str in data_str:
        mycol.insert_one({'data': mydict_str, 'datatype': 'str'})


    print('数据库中的数据：')
    for x in mycol.find():
        print(x)
    print('\n')
    print('从数据库中找出22~77之间的int型数据:')
    for i in mycol.find({"data":{"$gte": 22, "$lte": 77}, "datatype": "int"}):
        print(i)
    print('\n')
    print('从数据库中找出22~77之间的float型数据:')
    for i in mycol.find({"data":{"$gte": 22, "$lte": 77}, "datatype": "float"}):
        print(i)
    print('\n')
    print('从数据库中找出包含字符“a”的string型数据:')
    for i in mycol.find({"data": {"$regex": 'a'}, "datatype": "str"}):
        print(i)
    print('\n')
apply()

