# coding=utf-8

"""
  Author:  Jiang Eryu 姜尔彧 2018011766
  Purpose: Generate random data set with MongoDB.
  Created: 21/6/2020
"""

import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # 连接本地数据库
mydb = myclient["jiangeryu"]  # 创建数据库
mycol = mydb["sites"]  # 创建表
mycol.drop()    #每次更新数据


def dataSampling(datatype, datarange, num, strlen=8):
    """
    :Description: Generate a given condition random data set.
    :param datatype:int/float/str
    :param datarange: iterable data set
    :param num: number
    :param strlen:8
    :return: a dataset
    """
    try:  # 异常处理
        result = []
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.append(item)
                yield item
                continue
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
                yield item
                continue
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
                yield item
                continue
    except TypeError:
        print("? Type Error")
    except StopIteration:
        print("? Iteration Error")
    finally:
        pass



def dataScreening(datatype, result, *conditions):
    """
    :Description: Screen a given condition random data set.
    :param datatype: int/float/str
    :param result: random dataset
    :param conditions: variable-length argument
    :return: a dataset
    """
    try:  # 异常处理
        result_scr = []
        if datatype is int:
            for i in result:
                it = iter(conditions)
                low = next(it)
                high = next(it)
                if low <= i <= high:
                    result_scr.append(i)
                continue
        elif datatype is float:
            for i in result:
                it = iter(conditions)
                low = next(it)
                high = next(it)
                if low <= i <= high:
                    result_scr.append(i)
                continue
        elif datatype is str:
            for i in result:
                for sub in i:
                    if sub in conditions:
                        result_scr.append(i)
                continue
        return result_scr
    except TypeError:
        print("? Type Error")
    except StopIteration:
        print("？Iteration Error")
    finally:
        pass


def apply():
    data_int = dataSampling(int, (1, 1000), 5)  # 生成随机数
    data_float = dataSampling(float, (1.0, 1000.2), 5)
    data_str = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)

    dataresult_int = dataScreening(int, data_int, 10, 500)  # 筛选随机数 # 筛选（10，500）以内的整型随机数
    dataresult_float = dataScreening(float, data_float, 10.8, 500.9)    # 筛选(10.8, 500.9)以内的浮点随机数
    dataresult_str = dataScreening(str, data_str, 'a', 'at')    # 筛选带有'a'和'at'的字符串

    mydict_int = {'type': 'int', 'data': dataresult_int}  # 插入数据
    mydict_float = {'type': 'float', 'data': dataresult_float}
    mydict_str = {'type': 'str', 'data': dataresult_str}
    mycol.insert_one(mydict_int)
    mycol.insert_one(mydict_float)
    mycol.insert_one(mydict_str)


apply()
x = mycol.find_one({'type': 'int'})  # 调用数据
print("\nint类型示例：")
print(x)
x = mycol.find_one({'type': 'float'})
print("\nfloat类型示例：")
print(x)
x = mycol.find_one({'type': 'str'})
print("\nstr类型示例：")
print(x)
