##!/usr/bin/python3
"""
Author:YiYang.Dong
Purpose:Generate random data set
Created:20/6/2020
"""
import random
import string
import pymongo
#连接本地数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dongyiyang"]
#建表
mycol = mydb['test']

def dataSampling(datatype, datarange, num, strlen=6):
                # 固定参数；可变参数 *args；默认参数；关键字参数 **kwargs
    """
        :Description: Generate a given condition random data set.
        :param datatype:int,float,string...
        :param datarange: iterable data set
        :param num: number of data
        :param strlen: string length
        :return: a dataset
    """
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
    except NameError:
        print("数据类型错误")
    except TypeError:
        print("数据与数据类型不符")
    except MemoryError:
        print("内存已满")
    except:
        raise Exception
                # finally:
                # print("请继续在数据采样中生成数据")


def dataScreening(data, *conditions):
    '''
        :param data: data set above
        :param conditions: variable-length argument
        :return: a data set
    '''
    result = []
    try:
        for i in data:
            if type(i) is int:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.append(i)
            elif type(i) is float:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.append(i)
            elif type(i) is str:
                for teststr in conditions:
                    if teststr in i:
                        result.append(i)
    except:
        print("无更多项")

    return result

def apply():
    # int型
    result1 = dataSampling(int, [0, 150], 100)
    # 声明成对象
    mydict = {'type': 'int', 'info': dataScreening(result1, 10, 100)}
    # 添加入数据库
    mycol.insert_one(mydict)
    # float型
    result2 = dataSampling(float, [0, 200], 50)
    mydict = {'type': 'float', 'info': dataScreening(result2, 10, 55)}
    mycol.insert_one(mydict)
    # string型
    result3 = dataSampling(str, string.ascii_letters + string.digits, 2000, 15)
    mydict = {'type': 'str', 'info': dataScreening(result3, 'd', 'dy')}
    mycol.insert_one(mydict)

apply()

x = mycol.find_one({'type': 'float'})
print("float型：")
print(x)