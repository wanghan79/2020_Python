# -*- coding: utf-8 -*-
import random

import string
import pymongo


def gen_random(dtype, num, datatange=(10, 1000), str_num=8):
    """
    随机数生成
    :return:
    """
    try:
        start, end = datatange
        if dtype is int:
            return [random.choice(range(start, end + 1)) for _ in range(num)]

        elif dtype is float:
            return [random.uniform(start, end + 1) for _ in range(num)]

        elif dtype is str:
            return [''.join([random.choice(string.ascii_letters) for _ in range(str_num)]) for x in range(num)]

        else:
            print('请参入int、float、str类型的数据')
    except:
        print('传入参数错误')


def random_search(dtype, result, *datarange):
    """
    随机数搜索
    :return:
    """
    try:
        start, end = datarange
        if dtype is int:
            return [x for x in result if start <= x <= end]

        elif dtype is float:
            return [x for x in result if start <= x <= end]

        elif dtype is str:
            return [x for x in result if x.find(start) > -1 or x.find(end) > -1]

        else:
            print('请参入int、float、str类型的数据')
    except:
        print('传入参数错误')


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["random"]
# mycol = mydb["str"]
# mydict = {'data': gen_random(str, 10)}
# mycol.insert_one(mydict)
# y = mycol.find_one()['data']
# print(y)
# print(random_search(str, y, 'a', 'at'))
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["random"]
# mycol = mydb["int"]
# mydict = {'data': gen_random(int, 10)}
# mycol.insert_one(mydict)
# y = mycol.find_one()['data']
# print(y)
# print(random_search(int, y, 20, 500))



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["random"]
mycol = mydb["float"]
mydict = {'data': gen_random(float, 10)}
mycol.insert_one(mydict)
y = mycol.find_one()['data']
print(y)
print(random_search(float, y, 30, 700))
