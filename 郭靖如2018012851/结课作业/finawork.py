import random
import string
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["finawork"]
mycol=mydb["sites"]

def dataSampling(datatype,datarange,num,strlen=6):
    if datatype is float:
        it = iter(datarange)
        down=next(it)
        up=next(it)
        result = (random.uniform(down, up) for i in range(num))
    elif datatype is int:
        it = iter(datarange)
        down=next(it)
        up=next(it)
        result = (random.randint(down, up) for i in range(num))
    elif datatype is str:
        result = (''.join(random.SystemRandom().choice(datarange)for _ in range(5)) for i in range(num))
    return result

def apply():
    mydict={"type": 'int',"data":dataSampling(int,[1,100],100)}
    mycol.insert_one(mydict)
    mydict = {'type': 'float', 'data': dataSampling(float,[1,100],50)}
    mycol.insert_one(mydict)
    mydict = {'type': 'str', 'data': dataSampling(str,"abcdefg",100)}
    mycol.insert_one(mydict)
    x = mycol.find_one({"type": 'int'},{"type",0})
    for data in x:
        print(data)

    x = mycol.find_one({"type": 'float'},{"type",0})
    for data in x:
        print(data)

    x = mycol.find_one({"type": 'string'},{"type",0})
    for data in x:
        print(data)

apply()

x = mycol.find_one({"type":'int'})
print(x)