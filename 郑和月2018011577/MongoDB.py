"""
  Author:  heyue.zheng
  Purpose: MongoDB
  Created: 29/6/2020
"""
import random
import string
import pymongo


def dataSampling(datatype, datarange, num):
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
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(8))
                # result.add(item)
                yield item
                continue
            else:
                continue
        # return result

    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")


def dataScreening(data, *args):
    try:
        result = set()
        for value in data:
            if type(value) is int:
                if value in args:
                    # result.add(value)
                    yield value
                    continue
            elif type(value) is float:
                if value in args:
                    # result.add(value)
                    yield value
                    continue
            elif type(value) is str:
                for arg in args:
                    if arg in value:
                        # result.add(value)
                        yield value
                        continue
            else:
                continue
        # return result
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")


def apply():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["data_mongodb"]
    dblist = myclient.list_database_names()
    if "data_mongodb" in dblist:
        print("数据库已存在")
    mycol_int = mydb["data_int"]
    collist = mydb.list_collection_names()
    if "mycol_int" in collist:
        print("集合已存在")
    mycol_str = mydb["data_str"]
    collist = mydb.list_collection_names()
    if "mycol_str" in collist:
        print("集合已存在")
    mycol_float = mydb["data_float"]
    collist = mydb.list_collection_names()
    if "mycol_float" in collist:
        print("集合已存在")

    result1 = set(dataSampling(int, (0, 1000), 100))
    for i in result1:
         mycol_int.insert_one({"data_int": i})
    result_1 = set()
    for j in mycol_int.find({"data_int": {"$gte": 20, "$lte": 100}}):
        result_1.add(j)
    print(result_1)

    result2 = set(dataSampling(str, string.ascii_letters+string.digits+"@#$!", 100))
    for i in result2:
         mycol_str.insert_one({"data_str": i})
    result_2 = set()
    for j in mycol_str.find({"data_str": {'a', 'x', '5'}}):
        result_2.add(j)
    print(result_2)

    result3 = set(dataSampling(float, (1.0, 10.0), 100))
    for i in result3:
        mycol_float.insert_one({"data_float": i})
    result_3 = set()
    for j in mycol_float.find({"data_float": {"$gte": 2.0, "$lte": 3.0}}):
        result_3.add(j)
    print(result_3)
apply()