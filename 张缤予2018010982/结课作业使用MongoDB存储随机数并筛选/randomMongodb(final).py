##!/usr/bin/python3
"""

Author: By.Zhang
Purpose:Generate random data set and store in MongoDB,then screen by MongoDB.
Created:21/6/2020
"""
import string
import random
import pymongo


def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description:Generate a given condition random data set.
    :param datatype: the data type you want to sample including int, float,str.
    :param datarange: iterable data set
    :param num: the number of data you need
    :param strlen: the length of each string you want to generate
    '''
    if datatype is int:
        for i in range(0,num):
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item
    elif datatype is float:
        for i in range(0,num):
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
    elif datatype is str:
        for i in range(0, num):
            item = ''.join(random.SystemRandom().choice(datarange)for _ in range(strlen))
            yield item


def apply():

    # 生成随机数
    data_int = dataSampling(int, [0, 100], 10)
    data_float = dataSampling(float, [0, 50], 10)
    str_ex = string.ascii_letters + string.digits + string.punctuation
    data_str = dataSampling(str, str_ex, 50, 20)

    # 连接本地数据库
    myclient = pymongo.MongoClient(host='localhost', port=27017)

    # 创建名为'myData'的数据库
    mydb = myclient["zbyData"]

    # 检查'myData'是否存在
    dblist = myclient.list_database_names()
    if 'zbyData' in dblist:
        print('The database exists.')
    print('\n')

    # 创建表
    mycol = mydb['myCollection']

    # 每次插入前都清空，保证数据库中的数据是这次程序新生产的
    mycol.drop()

    # 插入数据
    for mydict_int in data_int:
        mycol.insert_one({'data': mydict_int, 'datatype': 'int'})
    for mydict_float in data_float:
        mycol.insert_one({'data': mydict_float, 'datatype': 'float'})
    for mydict_str in data_str:
        mycol.insert_one({'data': mydict_str, 'datatype': 'str'})


    print('数据库中的数据：')
    for x in mycol.find():
        print(x)
    print('\n\n')

    # int型筛选
    print('从数据库中取出20~50之间的整数:')
    for i in mycol.find({"data":{"$lt": 50, "$gt": 20},"datatype": "int"}):
        print(i)
    print('\n\n')

    # float型筛选
    print('从数据库中取出20~60之间的浮点数:')
    for i in mycol.find({"data": {"$lt": 60, "$gt": 20}, "datatype": "float"}):
        print(i)
    print('\n\n')

    print('从数据库中取出含有’a‘或者’no‘的字符串:')
    for i in mycol.find({"$or":[{"data": {"$regex": 'a'}, "datatype": "str"}, {"data": {"$regex": 'no'}, "datatype": "str"}]}):
        print(i)
    print('\n\n')


apply()
