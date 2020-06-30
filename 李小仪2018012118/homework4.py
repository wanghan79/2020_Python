##!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
      Author:XY.Li
      Purpose:generate random data set.
      Created:25/6/2020
"""
import random
import string
from collections.abc import Iterable

import pymongo


def dataSampling(datatype, datarange, num, strlen=1):
    '''
           :Description:Generate a given condition random data set.
           :param datatype: dddd
           :param datarange: iterable data set
           :param num:number
           :param strlen:
           :return:a dataset
        '''

    try:
        # result = set()
        for index in range(0, num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                # result.add(item)
                yield item
                continue
            elif datatype is float:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                # result.add(item)
                yield item
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                # result.add(item)
                yield item
                continue
            # return result
    except ValueError:
        print("传入无效的参数")
    except MemoryError:
        print("内存溢出错误")
    except Exception as r:
        print('未知错误 %s' % (r))
def dataScreening(data, *args):
    try:
        result = set()
        for i in data:
            if type(i) is int:
                it = iter(args)
                if next(it) <= i <= next(it):
                    result.add(i)
                continue
            elif type(i) is float:
                it = iter(args)
                if next(it) <= i <= next(it):
                    result.add(i)
                    continue
            elif type(i) is str:
                it = iter(args)
                if i == next(it):
                    result.add(i)
                    continue
        return result
    except ValueError:
        print("传入无效的参数")
    except MemoryError:
        print("内存溢出错误")
    except Exception as r:
        print('未知错误 %s' % (r))

def apply():
    result = set()
    sult = set()
    b1 = set()
    b2 = set()
    c1 = set()
    c2 = set()
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["runoobdb"]
    dblist = myclient.list_database_names()
    # dblist = myclient.database_names()
    if "runoobdb" in dblist:
        print("数据库已存在！")
    mycol1 = mydb["sites1"]
    mycol2 = mydb["sites2"]
    mycol3 = mydb["sites3"]
    collist = mydb.list_collection_names()
    #collist = mydb.collection_names()
    if "sites1" in collist:   #判断sites1集合是否存在
        print("集合1已存在！")
    if "sites2" in collist:   #判断sites2集合是否存在
        print("集合2已存在！")
    if "sites3" in collist:   #判断sites3集合是否存在
        print("集合3已存在！")

    #Int
    print("Int!")
    for index in range(0, 10):
     item = dataSampling(int, [0, 100], 10)
     mycol1.insert_one({'data': next(item)})
    for x in mycol1.find():
     result.add(x.get('data'))
    print("生成的数据:", result)
    sult = dataScreening(result, 20, 50)
    print("筛选后的数据", sult)
    #Float
    print("Float!")
    for index in range(0, 10):
     item = dataSampling(float, [0.0, 100.0], 10)
    mycol2.insert_one({'data': next(item)})
    for x in mycol2.find():
     b1.add(x.get('data'))
    print("生成的数据:", b1)
    b2 = dataScreening(b1, 30.0, 50.0)
    print("筛选后的数据", b2)
    #Str
    print("Str!")
    for index in range(0, 10):
     item = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
     mycol3.insert_one({'data': next(item)})
    for x in mycol3.find():
     c1.add(x.get('data'))
    print("生成的数据:", c1)
    c2 = dataScreening(c1, 't')
    print("筛选后的数据", c2)
apply()
