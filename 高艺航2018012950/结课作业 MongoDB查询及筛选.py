"""
  Author:  Yihang.Gao 高艺航
StuNumber: 2018012950
  Purpose: Generate random data set with MongoDB.
  Created: 19/6/2020
"""
import random
import string
import pymongo

def DataSampling(datatype,datarange,num,strlen=8):
    if datatype is int :
        for i in range(0, num):
            it = iter(datarange)
            item = random.randint(next(it),next(it))
            yield  item
    elif datatype is float:
        for i in range(0, num):
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
    elif datatype is str:
        for i in range(0, num):
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item

def DataScreening(data,*arguments):
    result = list()
    for i in data:
        if type(i) == type(arguments[0]):
            if isinstance(i,int):
                if i >= arguments[0] and i <= arguments[1]:
                     result.append(i)
            elif isinstance(i,float):
                if i >= arguments[0] and i <= arguments[1]:
                    result.append(i)
            elif isinstance(i,str):
                flag=1
                for x in i:
                    if x  not in arguments[0]:
                        flag = 0
                if flag:
                    result.append(i)
    return result


def work():
    mgoclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myDB = mgoclient["number"]
    mgoint = myDB["integer"]
    mgodouble = myDB["double"]
    mgostring = myDB["string"]
#整型
    res1 = list();
    k1=DataSampling(int,(1,1000),100)
    while True:
        try:
            result={"value":next(k1)};
            mgoint.insert_one(result)
        except StopIteration:
            break
    print("随机生成Integer型：",end="")
    for x in mgoint.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            res1.append(n)
    print(res1)
    res2 = DataScreening(res1, 10, 100)
    print("筛选后：",res2)
#浮点型
    res3=list()
    k2 = DataSampling(float, (1, 1000), 100)
    while True:
        try:
            result={"value":next(k2)};
            mgodouble.insert_one(result)
        except StopIteration:
            break
    print("随机生成浮点型：",end="")
    for x in mgodouble.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            res3.append(n)
    print(res3)
    res4 = DataScreening(res3, 10.0, 100.0)
    print("筛选后：",res4)
#字符型
    res5 = list()
    k3 = DataSampling(str, string.ascii_letters+string.digits, 100,10)
    while True:
        try:
            result = {"value": next(k3)};
            mgostring.insert_one(result)
        except StopIteration:
            break
    print("随机生成字符型：",end="")
    for x in mgostring.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            res5.append(n)
    print(res5)
    res6 = DataScreening(res5, string.ascii_letters)
    print("筛选后：", res6)

work()