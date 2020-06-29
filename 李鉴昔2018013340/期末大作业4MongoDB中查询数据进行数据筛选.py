"""
  Author:  jianxi.li
  Purpose: homework4:USE MONGODB to store random numbers generated in normal homework3 and to filter data by querying data from MONGODB
  Created: 19/6/2020
"""
import random
import string
import pymongo

def datasampling(type,datarangement,quantity,strlen=10):
    if type is int :
        for i in range(0, quantity):
            options = iter(datarangement)
            document = random.randint(next(options),next(options))
            yield  document
    elif type is float:
        for i in range(0, quantity):
            options = iter(datarangement)
            document = random.uniform(next(options), next(options))
            yield document
    elif type is str:
        for i in range(0, quantity):
            document = ''.join(random.SystemRandom().choice(datarangement) for _ in range(strlen))
            yield document

def dataScreening(datafile,*datatype):
    output = list()
    for item in datafile:
        if type(item) == type(datatype[0]):
            if isinstance(item,int):
                if item >= datatype[0] and item <= datatype[1]:
                     output.append(item)
            elif isinstance(item,float):
                if item >= datatype[0] and item <= datatype[1]:
                    output.append(item)
            elif isinstance(item,str):
                flag=1
                for x in item:
                    if x  not in datatype[0]:
                        flag = 0
                if flag:
                    output.append(item)
    return output


def check():
    firstclient = pymongo.MongoClient("mongodb://localhost:27017/")
    numberhome = firstclient["numbers"]
    inttype = numberhome["int numbers"]
    doubletype = numberhome["double numbers"]
    stringtype = numberhome["strings"]

    output1 = list();
    ans1=datasampling(int,(1,1000),100)
    while True:
        try:
            result={"value":next(ans1)};
            inttype.insert_one(result)
        except StopIteration:
            break
    print("int before：",end="")
    for x in inttype.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            output1.append(n)
    print(output1)
    outputs1 = dataScreening(output1, 10, 125)
    print("int later：",outputs1)

    output2=list()
    ans2 = datasampling(float, (1, 800), 120)
    while True:
        try:
            result={"value":next(ans2)};
            doubletype.insert_one(result)
        except StopIteration:
            break
    print("float before：",end="")
    for x in doubletype.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            output2.append(n)
    print(output2)
    outputs2 = dataScreening(output2, 15.0, 120.0)
    print("float later：",outputs2)

    output3 = list()
    ans3 = datasampling(str, string.ascii_letters+string.digits, 80,12)
    while True:
        try:
            result = {"value": next(ans3)};
            stringtype.insert_one(result)
        except StopIteration:
            break
    print("string before：",end="")
    for x in stringtype.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            output3.append(n)
    print(output3)
    outputs3 = dataScreening(output3, string.ascii_letters)
    print("string later：", outputs3)

check()