##!/usr/bin/python3
"""
  Author:  Jiaza.Xin
  Purpose: Use MongoDB to store random Numbers generated in normal work 3, and query data from MongoDB for data filtering.
  Created: 27/6/2020
"""
import random
import string
import pymongo

def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description: Generate a given condition random data set.As a yield, returns an iterable object
    :param datatype: int,flout,str
    :param datarange: iterable data set,len(datarange) == 2
    :param num: number
    :param strlen:length of string
    :return: a dataset
    '''
    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item
            continue
        else:
            continue


def dataScreening(data, datatype, *range):
    '''
    :Description:Data filtering
    :param data:a set the result of dataSampling
    :param datatype:type,int,float,str
    :param range:condition for data filtering,len(range) <= 2 when type is int or float
    :return:a set
    '''
    try:
        if type(range) is int or float:
            if len(range) > 2:
                print("TypeError:incorrect filter condition for input")
            elif len(range) == 1:
                print("Warning:the filter result is greater than the given condition")
        # Screening---------------------------------------------

            if datatype is int or float:
                if len(range) == 2:
                    a, b = range
                    result = {x for x in data if a <= x <= b}
                elif len(range) == 1:
                    a = range
                    result = {x for x in data if a <= x}
            elif datatype is str:
                st = iter(range)
                result = {x for x in data if next(st) in x}
    except TypeError:
        print("TypeError :wrong type parameter entered")
    except MemoryError:
        print("MemoryError:Memory overflow error (not fatal to Python interpreter)")
    except Exception as e:
        print(str(e))
        print("Error")
    else:
        return result

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()
mydb = myclient["sampdta"]
if "sampdta" in dblist:  # 判断数据库是否存在
    print("数据库已存在！")
mycol = mydb["db_sampdta"]
collist = mydb.list_collection_names()
if "db_sampdta" in collist:  # 判断 db_sampdta 集合是否存在
    print("集合已存在！")


def apply():
    #--------------------------------------------------------------int
    result1 = dataSampling(int, (1, 100), 50)
    #afresult1 = dataScreening(result1, int, 20, 40)  # ---after the screening
    #print(afresult1)

    for x in result1:
        mydict = {"datatype": "int", "data": x}
        mycol.insert_one(mydict)
        print(db_sampdta)
    for x in mycol.find():
        afresult1 = dataScreening(x, int, 20, 40)
    print(afresult1)
    #--------------------------------------------------------------float
    result2 = dataSampling(float, (1, 100), 500)
    #afresult2 = dataScreening(result2, float, 20, 40)  # ---after the screening
    #print(afresult2)

    for x in result2:
        mydict = {"datatype": "float", "data": x}
        mycol.insert_one(mydict)
        print(db_sampdta)
    for x in mycol.find({},{"datatype": "float"}):
        afresult2 = dataScreening(x, float, 20, 40)
    print(afresult2)
    #--------------------------------------------------------------str
    result3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 200)
    #afresult3 = dataScreening(result3, str, 'siywueiwwfbwwfb', 'd')  # ---after the screening
    #print(afresult3)

    for x in result3:
        mydict = {"datatype": "str", "data": x}
        mycol.insert_one(mydict)
        print(db_sampdta)
    for x in mycol.find({},{"datatype": "str"}):
        afresult3 = dataScreening(x, str, 'siywueiwwfbwwfb', 'd')
    print(afresult3)


apply()
