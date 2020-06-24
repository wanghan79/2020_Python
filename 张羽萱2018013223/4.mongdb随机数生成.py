"""
Author: Zhang yuxuan 2018013223
Purpose: Generate random data set by generator.
Created: 19/6/2020

"""
import random
import string
import pymongo

def DataSampling(datatype, datarange, num, strlen=8):
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



def dataScreening(data, *conditions):
    result = set()
    for item in data:
        if type(item) is int:
            it = iter(conditions)
            if next(it) <= item <= next(it):
                result.add(item)
        elif type(item) is float:
            it = iter(conditions)
            if next(it) <= item <= next(it):
                result.add(item)
        elif type(item) is str:
            for substr in conditions:
                if substr in item:
                    result.add(item)
    return result

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mongoclient["number"]
mongoint = mydb["int"]
mongofloat = mydb["float"]
mongostring = mydb["string"]


result1 = set()
f = DataSampling(int, (1, 1000), 100)
while True:
    try:
        result1.add(next(f))
        mongoint.insert_one(result1)
    except StopIteration:
        break
print("Randomly generated integer：", result1)
for x in mongoint.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result1.add(n)
print(result1)
result2 = dataScreening(result1, 10, 100)
print("After selecting：", result2)

result3 = set()
f1 = DataSampling(float, (1, 1000), 100)
while True:
    try:
        result3.add(next(f1))
        mongofloat.insert_one(result3)
    except StopIteration:
        break
print("Randomly generated float：",end="")
for x in mongofloat.find({},{ "value": 1, "_id": 0 }):
    for m,n in x.items():
        result3.add(n)
print(result3)
result4 = dataScreening(result3, 10.0, 100.0)
print("After selecting：", result4)

result5 = set()
f2 = DataSampling(str, string.ascii_letters+string.digits, 100, 10)
while True:
    try:
        result5.add(next(f2))
        mongostring.insert_one(result5)
    except StopIteration:
        break
print("Randomly generated float：", end="")
for x in mongostring.find({}, {"value": 1, "_id": 0}):
    for m, n in x.items():
        result5.add(n)
print(result5)
result6 = dataScreening(result5, string.ascii_letters)
print("After selecting：", result6)
