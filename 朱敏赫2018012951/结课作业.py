"""
  Author:  zhu min he
  Created: 30/6/2020
"""
import string
import random
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["zhuminhe"]
mycol = mydb["sites"]

def dataSampling(datatype, datarange, num, strlen=6):
    try:
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                yield (item)
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield (item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                yield (item)
    except TypeError:
        print("数据类型不符")
    except NameError:
        print("数据类型错误")
    except:
        raise Exception

def dataScreening(data, *args):
    try:
        result = set()
        for item in data:
            if isinstance(item, int):
                it = iter(args)
                if next(it) <= item and next(it) >= item:
                    result.add(item)
            elif isinstance(item, float):
                it = iter(args)
                if next(it) <= item and next(it) >= item:
                    result.add(item)
            elif isinstance(item, str):
                for x in args:
                    if x in item:
                        result.add(item)
    except:
        print("没有更多项")
    return result

def apply():
    #int
    result01 = dataSampling(int, [0, 100], 50)
    mydict = {'type': 'int', 'info': dataScreening(result01, 20, 50)}
    mycol.insert_one(mydict)
    y = mycol.find_one({'type': 'int'})
    print('int:')
    print(y)
    #float
    result02 = dataSampling(float, [0, 200], 50)
    mydict = {'type': 'float', 'info': dataScreening(result02, 20, 50)}
    mycol.insert_one(mydict)
    y = mycol.find_one({'type': 'float'})
    print('float:')
    print(y)
    #string
    result03 = dataSampling(str, string.ascii_letters + string.digits, 1000,50)
    mydict = {'type': 'str', 'info': dataScreening(result03, 'a', 'ab')}
    mycol.insert_one(mydict)
    y = mycol.find_one({'type': 'str'})
    print('string:')
    print(y)

apply()
