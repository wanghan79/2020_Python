"""
  Author:JLH2018010984
  Created: 2020/6/28
"""


import random
import string
import pymongo

def print_line():
    print("*" * 60)
print_line()
############
def dataSampling(datatype, datarange, num, strlen=8):
    '''
        :Description: Generate a given condition random data set.
        :param datatype: The type of data which include int float and string
        :param datarange: iterable data set
        :param num: Input parameters that means The final result of the number of elements
        :param strlen:The length of input strings
        :return: a dataset
    '''
    try:
        result = set()
        if (datatype is int):
            while len(result) < num:    #防止重复
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                result.add(item)
        elif (datatype is float):
            while len(result) < num:
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                result.add(item)
        elif (datatype is str):
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
    except ValueError:
        print("参数是无效的")
    except TypeError:
        print("发生类型错误")
    except MemoryError:
        print("发生内存错误")
    except NameError:
        print("初始化参数名称")
    else:
        return result

def dataScreening(data,*args):
    try:
        resultT = set()
        for i in data:
            if (type(i) is int):
                T = iter(args)
                if(next(T) <= i and next(T) >= i):
                    resultT.add(i)
            elif (type(i) is float):
                    T = iter(args)
                    if (next(T) <= i and next(T) >= i):
                        resultT.add(i)
            elif (type(i) is str):
                for cstr in args:
                    if(cstr in i):
                        resultT.add(i)
    except ValueError:
        print("参数是无效的")
    except TypeError:
        print("发生类型错误")
    except MemoryError:
        print("发生内存错误")
    except NameError:
        print("初始化参数名称")
    else:
        return resultT

def apply():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["JLHData"]
    list = myclient.list_database_names()
    if 'JLHData' in list:
        print('had\n')
        #c创建c
    mycol = mydb["sites"]
    mycol.drop()

    JLHdata1 = dataSampling(int, [0, 101], 20)
    JLHdata2 = dataSampling(float, [0, 101], 20)
    JLHdata3 = dataSampling(str, string.ascii_letters, 20)

    for mydict_int in JLHdata1:
        mycol.insert_one({'data': mydict_int, 'datatype': 'int'})
    for mydict_float in JLHdata2:
        mycol.insert_one({'data': mydict_float, 'datatype': 'float'})
    for mydict_str in JLHdata3:
        mycol.insert_one({'data': mydict_str, 'datatype': 'str'})


    print('DATA：')
    for x in mycol.find():
        print(x)
    print('---------------\n')

    print('intDATA:')
    for i in mycol.find({"data":{"$gte": 20, "$lte": 80}, "datatype": "int"}):
        print(i)
    print('----------------\n')
    print_line()

    print('floatDATA:')
    for i in mycol.find({"data":{"$gte": 20, "$lte": 80}, "datatype": "float"}):
        print(i)
    print('-----------------\n')
    print_line()

    print('strDATA:')
    for i in mycol.find({"data": {"$regex": 'a'}, "datatype": "str"}):
        print(i)
    print('-----------------\n')

apply()

print_line()