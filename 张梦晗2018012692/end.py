##!/usr/bin/python3
"""
  Author:Mh,Zhang
  Purpose:
  StuNumber:2020/6/29
"""
import string
import random
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["homework"]
col =db['work']


def data_sampling(data_type, data_range, num, begin, end, str_len=10):
    result = set()
    try:
        if data_type is int:
            while True:
                it = iter(data_range)
                i = random.randint(next(it), next(it))
                if data_screening(i, begin, end) is not None:
                    result.add(i)
                if len(result) >= num:
                    break
        elif data_type is float:
            while True:
                it = iter(data_range)
                i = random.uniform(next(it), next(it))
                if data_screening(i, begin, end) is not None:
                    result.add(i)
                if len(result) >= num:
                    break
        elif data_type is str:
            while True:
                i = ''.join(random.SystemRandom().choice(data_range) for _ in range(str_len))
                if data_screening(i, begin, end) is not None:
                    result.add(i)
                if len(result) >= num:
                    break
        return result
    except ValueError:
        print("输入的值有误!")
    except TypeError:
        print("参数类型错误!")
    except Exception as er:
        print(er)


def data_screening(data, *ange):
    try:
        it = iter(ange)
        if type(data) is int or type(data) is float:
            if next(it) <= data <= next(it):
                return data
        elif type(data) is str:
            for val in ange:
                if val in data:
                    return data
    except ValueError:
        print("输入的值有误!")
    except TypeError:
        print("参数类型错误!")
    except Exception as er:
        print(er)
    return None


def insert_mongodb():

    dict1 = {'type': 'int', 'info': data_sampling(int, (1, 100), 5, 20, 90)}
    col.insert_one(dict1)

    dict2 = {'type': 'float', 'info': data_sampling(float, (1, 100), 5, 20, 90)}
    col.insert_one(dict2)

    str_ex = string.ascii_letters + string.digits + "@!#@"
    dict3 = {'type': 'str', 'info': data_sampling(str, str_ex, 10, 'ae', 'bc')}
    col.insert_one(dict3)


insert_mongodb()

int_result = col.find_one({"type": 'int'})
print(int_result)
float_result = col.find_one({"type": 'float'})
print(float_result)
str_result = col.find_one({"type": 'str'})
print(str_result)
