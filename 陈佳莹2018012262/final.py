"""
Author:Chenjiaying
Purpose:Generate random data set with MongoDB.
Created:25/6/2020
"""
import random
import string
import pymongo

def dataSampling(datatype, datarange, num, strlen=8):
    try:
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
            for i in range(0,num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
    except TypeError:
        print("类型错误.")
    except ValueError:
        print("参数无效.")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def apply():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["cdata"]
    dblist = myclient.list_database_names()
    if 'cdata' in dblist:
        print('The database exists.')
    mycol = mydb['col']
    # int
    mycol.drop()
    result = dataSampling(int, [0, 50], 10)
    for x in result:
        mycol.insert_one({'data': x, 'datatype': 'int'})
    for x in mycol.find():
        print(x)
    print('筛选0~20之间的整数')
    for x in mycol.find({"data": {"$lt": 20, "$gt": 0}, "datatype": "int"}):
        print(x)

    # float
    mycol.drop()
    result = dataSampling(float, [0, 50], 10)
    for x in result:
        mycol.insert_one({'data': x, 'datatype': 'float'})
    for x in mycol.find():
        print(x)
    print('筛选浮点数')
    for x in mycol.find({"data": {"$lt": 20, "$gt": 0}, "datatype": "float"}):
        print(x)

    # str
    mycol.drop()
    result = dataSampling(str, string.ascii_letters + string.digits, 20, 10)
    for x in result:
        mycol.insert_one({'data': x, 'datatype': 'str'})
    for x in mycol.find():
        print(x)
    print('筛选含有a的字符串')
    for x in mycol.find({"$or": [{"data": {"$regex": 'a'}, "datatype": "str"}]}):
        print(x)


apply()