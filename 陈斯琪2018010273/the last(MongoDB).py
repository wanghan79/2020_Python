# 函数封装随机数生成和数据筛选,有异常处理
##!/usr/bin/python3
# """
#   Author:  Sq.Chen
#   Purpose: Store Generate random data set with MongoDB & Query data with MongoDB .
#   Created: 21/6/2020
# """

import string
import random
import pymongo

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
        return result
    except Exception as e:
        # 没有单独给每个参数判断错误，不知道怎么整
        print(e)
        print("input is wrong!!!")


def apply():
    myclient=pymongo.MongoClient("mongodb://localhost:27017")
    # 数据库named:sqbdb
    mydb=myclient["sqbdb"]
    # 检查sqbdb是否存在
    dblist = myclient.list_database_names()
    if 'sqdbd' in dblist:
        print('Database exists!!')

    # 表named:sqsite
    mycol=mydb["sqsite"]

    # 输入数据
    # float型
    result1 = dataSampling(float, {0, 100}, 10)
    for x1 in result1:
        mycol.insert_one({'data': x1})
    print('the data in database：')
    for x in mycol.find():
        print(x)
    # 筛选5~50的数
    n=0
    print("datascreening:")
    for i in mycol.find({"data":{"$lt": 50, "$gt": 5}}):
        print(i)
        n += 1
    if n == 0:
        print("there is not suitable data!!!")
    print("\n")

    # int型
    # 清空表
    mycol.drop()
    result2 = dataSampling(int, {0, 100}, 10)
    for x2 in result2:
        mycol.insert_one({'data': x2})
    print('the data in database：')
    for x in mycol.find():
        print(x)
    # 筛选5~50的数
    n=0
    print("datascreening:")
    for i in mycol.find({"data": {"$lt": 50, "$gt": 5}}):
        print(i)
        n += 1
    if n == 0:
        print("there is not suitable data!!!")
    print("\n")


    # str型
    # 清空表
    mycol.drop()
    result3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
    for x3 in result3:
        mycol.insert_one({'data': x3})
    print('the data in database：')
    for x in mycol.find():
        print(x)
    # 筛选含"a"的字符串
    n=0
    print("datascreening:")
    for i in mycol.find({"data": {"$regex": 'a'}}):
        print(i)
        n += 1
    if n == 0:
        print("there is not suitable data!!!")
    print("\n")

apply()