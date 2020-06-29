# python3
"""
mongod.exe --nojournal --dbpath .
  Author:  Tanlin
  Purpose: 结课作业：使用MongoDB存储平时作业3中生成的随机数，并能从MongoDB中查询数据进行数据筛选。
  Created: 2020.6.24
"""
import random
import string
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # 27017是本机端口号
mydb = myclient["RandomDatadb"]  # 创建数据库（Mongo打开和创建不分）
# dblist = myclient.list_databases_names()
# if "RandomDatadb" in dblist:
#     print("数据库已经存在！")
mycol = mydb["Data"]  # 创建表（集合）
# 检查集合是否存在与数据库一样
def dataSampling(datatype, datarange, num, strlen=10):  # 生成
    try:
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                yield item  #yield代替return返回的是生成器
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield item
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                yield item
    except TypeError:
        print('The data type is error!')
    except ValueError:
        print("The data value is error!")
    except MemoryError:
        print("The data is too much!")
    print("The random data:\n", result)
    return result

def dataScreening(data, *args):  # 筛选*args(可变参数)
    try:
        result = set()
        for index in data:
            if type(index) is int or type(index) is float:
                it = iter(args)
                if next(it) <= index <= next(it):
                    result.add(index)
            elif type(index) is str:
                for substr in args:
                    if substr in index:
                        result.add(index)
    except TypeError:
        print("The data type is error!")
    except ValueError:
        print("The data value is error!")
    print("After filtered:")
    return result

def apply():  # 输出结果
    mycol.drop()#清空
    print("INT:")
    result1 = dataSampling(int, (1, 100), 5)
    #item1 = dataScreening(result1, 20, 80)
    for item1 in result1:
        mycol.insert_one({"Data":item1})
    result1_1=set()
    for index in mycol.find():
        result1_1.add(index['Data'])
    i = 0
    result1_1_1=set()
    for item1 in mycol.find({"Data": {"$gte": 20, "$lte": 80}}):
        result1_1_1.add(item1['Data'])
        i += 1
    if i == 0:
        print("Can't find!")
    else:
        print("After filtered:\n",result1_1_1)
    mycol.drop()
    print("FLOAT:")
    result2 = dataSampling(float, (1, 100), 5)
    #item2 = dataScreening(result2, 20, 80)
    for item2 in result2:
        mycol.insert_one({'Data': item2})
    result2_2 = set()
    for index in mycol.find():
        result2_2.add(index['Data'])
    i = 0
    result2_2_2 = set()
    for item2 in mycol.find({"Data": {"$gte": 20, "$lte": 80}}):
        result2_2_2.add(item2['Data'])
        i += 1
    if i == 0:
        print("Can't find!")
    else:
        print("After filtered:\n", result2_2_2)
    mycol.drop()
    print("STR:")
    result3 = dataSampling(str, string.ascii_letters + string.digits + string.printable, 5)
    #item3 = dataScreening(result3,"T")
    for item3 in result3:
        mycol.insert_one({"Data": item3})
    result3_3=set()
    for index in mycol.find():
        result3_3.add(index['Data'])
    i = 0
    result3_3_3=set()
    for item3 in mycol.find({"Data": {"$regex":"T"}}):
        result3_3_3.add(item3['Data'])
        i += 1
    if i == 0:
        print("Can't find!")
    else:
        print("After filtered:\n",result3_3_3)

apply()