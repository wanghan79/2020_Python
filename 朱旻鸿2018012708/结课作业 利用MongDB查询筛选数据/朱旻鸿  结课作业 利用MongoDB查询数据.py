##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Generate random data set through mongodb database
  Created: 22/6/2020
"""
import random
import string
import pymongo

Myclient=pymongo.MongoClient("mongodb://localhost:27017/")
Mydb=Myclient["DataServer"]
Mycol=Mydb["Datasites"]
Mycol.delete_many({})

def DataSampling(datatype, datarange, num, strlen=10):
    '''
    :param datatype: basic data type including int float string
    :param datarange: iterable data set
    :param num: number of data
    :param strlen: string length
    :return: yield a random data
    '''
    try:
        if datatype is int:
            while num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield {"int": item}
                num -= 1
        elif datatype is float:
            while num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield {"float": item}
                num -= 1
        elif datatype is str:
            while num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield {"str": item}
                num -= 1

    except NameError:
        print("Please input basic data type in DataSampling")
    except TypeError:
        print("Please check data type in DataSampling")
    except MemoryError:
        print("Too much data out of memory in DataSampling")
    except:
        raise Exception


def DataScreening(datatype, *conditions):
    '''

    :param datatype: basic data type including int float string
    :param conditions: variable-length argument
    :return: a data set
    '''
    try:
        result = set()
        if datatype is int:
            it = iter(conditions)
            for item in Mycol.find({"int": {"$gte": next(it), "$lte": next(it)}}):
                result.add(item["int"])
        elif datatype is float:
            it = iter(conditions)
            for item in Mycol.find({"float": {"$gte": next(it), "$lte": next(it)}}):
                result.add(item["float"])
        elif datatype is str:
            for item in Mycol.find({"str": {'$gt': "\0"}}):
                for substr in conditions:
                    if substr in item["str"]:
                        result.add(item["str"])
    except NameError:
        print("Please input basic data type in DataScreening")
    except TypeError:
        print("Please check data type in DataScreening")
    except MemoryError:
        print("Too much data out of memory in DataScreening")
    except:
        raise Exception
    else:
        print("The result of data screening")
        print(result)
        print("Welcome to continue generating random data ")


def Apply():
    print("********************************************************")
    for item in DataSampling(int,[0,200],100):
        Mycol.insert_one(item)
    DataScreening(int,60,90)
    print("********************************************************")
    for item in DataSampling(float,[0,100],100):
        Mycol.insert_one(item)
    DataScreening(float,60,70)
    print("********************************************************")
    for item in DataSampling(str, string.ascii_letters + string.digits, 2000, 15):
        Mycol.insert_one(item)
    DataScreening(str, 'at','att','attt')
    print("********************************************************")


Apply()