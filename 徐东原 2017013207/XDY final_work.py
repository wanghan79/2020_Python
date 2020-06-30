##!/usr/bin/python3
"""
  Author: DY.Xu
  Purpose: mongoDB
  Created: 22/6/2020
"""
import random
import string
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.XDY
Sampledata = mydb.Sampledata


def dataSampling(datatype, datarange, num, strlen = 12):
    '''
            :Description: Generate a given condition random data set.
            :param datatype: basic data type (int  float  str)
            :param datarange: iterable data set
            :param num: number of data
            :param strlen:string length
            :return a data set
        '''
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
        else:
            raise NameError
    except TypeError:
        print("Please enter the iterable data range in dataSampling")
    except NameError:
        print("Please enter the correct data type in dataSampling")
    except Exception:
        print("There are other errors in dataSampling")
def tryscreen(producter):
    try:
        while True:
            Sampledata.insert_one({"data":next(producter)})
    except StopIteration:
        pass

def Apply():
    tryscreen(dataSampling(int, (0, 100), 30))
    print("type:int range:(0, 90)")
    print([i["data"] for i in Sampledata.find({"data": {"$gte": 0, "$lte": 90,"$type":16}},{"_id":0,"data":1})]) #mongo中16代表整型

    tryscreen(dataSampling(float, (0, 100), 20))
    print("type:float range:(0, 90)")
    print([i["data"] for i in Sampledata.find({"data": {"$gte": 0, "$lte": 90, "$type": "double"}}, {"_id": 0, "data": 1})])

    tryscreen(dataSampling(str, string.ascii_letters + string.digits + "@#$!", 20))
    print("type:string range:'a'")
    print([i["data"] for i in Sampledata.find()])
    print([i["data"] for i in Sampledata.find({"data": {"$regex": 'a', "$type": "string"}}, {"_id": 0, "data": 1})])

if __name__ == '__main__':
    Sampledata.drop()
    Apply()