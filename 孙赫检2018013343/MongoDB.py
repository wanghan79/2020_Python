__author__ = '2018013343'
"""
Author: sun hejian
Purpose: Generate random data set
Created: 27/6/2020
"""
import random
import string
import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mongoclient["shj"]
col =mydb['homework']

def datasampling(datatype,datarange,num,strlen=8):
    result = set()
    if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                yield item
                continue
    elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield item
                continue
    elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                yield item
                continue

def datascreening(data, condition):
    result = set()
    for i in data:
        if type(i) is int:
            it = iter(condition)
            if next(it) <= i <= next(it):
                result.add(i)
        elif type(i) is float:
            it = iter(condition)
            if next(it) <= i <= next(it):
                result.add(i)
        elif type(i) is str:
            for n in condition:
                if n in i:
                    result.add(i)
    return result

def apply():

    result_int = datasampling(int, [0, 100], 10)
    dict_int = {'type': 'int', 'data': datascreening(result_int, 0, 50)}

    result_float = datasampling(float, [0, 100], 10)
    dict_float = {'type': 'float', 'data': datascreening(result_float, 20, 30)}

    result_str = datasampling(str, string.ascii_letters + string.digits + string.punctuation, 10, 10)
    dict_str = {'type': 'str', 'data': datascreening(result_str, 's', 'h','j')}

    col.insert_one(dict_int)
    col.insert_one(dict_float)
    col.insert_one(dict_str)


apply()

print(col.find_one({"type": 'int'}))
print(col.find_one({"type": 'float'}))
print(col.find_one({"type": 'str'}))