##!/usr/bin/python3
"""
  Author:  XinYuan.Zhang
  Purpose: Generate random data set.
  Created: 23/6/2020
"""
import string
import random
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["homework"]
col =db['work']


def dataSampling(datatype, datarange, num, strlen=8):
    if datatype is int:
       for k in range(0, num):
            it = iter(datarange)
            i = random.randint(next(it), next(it))
            yield i
    elif datatype is float:
       for k in range(0, num):
            it = iter(datarange)
            i = random.uniform(next(it), next(it))
            yield i
    elif datatype is str:
       for k in range(0, num):
            i = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield i

def dataScreening(data,*ange):
    aresult = []
    try:
        for j in data:
            if type(j) is int or type(j) is float:
                it = iter(ange)
                if next(it) <= j <= next(it):
                    aresult.append(j)
            elif type(j) is str:
                for substr in ange:
                    if substr in j:
                        aresult.append(j)
    except ValueError:
        print("参数有误")
    except TypeError:
        print("类型有误")
    except Exception as e:
        print(e)
    return aresult


def apply():

    result1 = dataSampling(int, [0, 100], 10)
    dict1 = {'type': 'int', 'info': dataScreening(result1, 10, 90)}
    col.insert_one(dict1)

    result2 = dataSampling(float, [0, 100], 10)
    dict2 = {'type': 'float', 'info': dataScreening(result2, 10, 90)}
    col.insert_one(dict2)
    str_ex = string.ascii_letters + string.digits + string.punctuation

    result3 = dataSampling(str, str_ex, 100, 10)
    dict3 = {'type': 'str', 'info': dataScreening(result3, 'ai', 'bm')}
    col.insert_one(dict3)


apply()

x1 = col.find_one({"type": 'int'})
print(x1)
x2 = col.find_one({"type": 'float'})
print(x2)
x3 = col.find_one({"type": 'str'})
print(x3)
