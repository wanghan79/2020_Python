'''
Author: WeiFan 2018011641
Aim:  Generation and filtering of random numbers——PyMongo
Data: 2020/6/21
'''
import string
import random
import PyMongo
def DataSampling(datatype,datarange,num,strlen=8):
    try:
        if datatype is int:
            for i in range(0,num):
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                #result.add(item)
                yield item
        elif datatype is float:
            for i in range(0,num):
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                #result.add(item)
                yield item
        elif datatype is str:
            for i in range(0,num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                #result.add(item)
                yield item
    except ValueError:
        print("Invalid Data")
    except TypeError:
        print("Error in type,which may cause the parameter to fail to iterate")


def DataSelect(result,datatype,item1,item2):
    try:
        newresult=set()
        for it in result:
            if datatype is int:
                if (it>=item1) and (it<=item2):
                    newresult.add(it)
            elif datatype is float:
                if (it>=item1) and (it<=item2):
                    newresult.add(it)
            elif datatype is str:
                if (item1 in it) and (item2 not in it):
                    newresult.add(it)
    except ValueError:
        print("Invalid Data")
    except TypeError:
        print("Error in type,which may cause the parameter to fail to iterate")
    else :
        return newresult

def apply():
 try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Randomnumber"]
    dblist = myclient.list_database_names()
    if "Randomnumber" in dblist:
        print("True")
    mycol = mydb["sites"]
    collist = mydb.list_collection_names()
    if "sites" in collist:
        print("True")

    result1 = set()
    g1 = DataSampling(int, (0, 100), 8)
    while True:
        try:
            mydict1 = {'type': datatype, 'data': next(g1)}
            mycol.insert_one(mydict1)
        except StopIteration:
            break
    print("DataSamping:")
    for x in mycol.find():
        result1.add(x)
    print(result1)
    newresult1 = DataSelect(result1, int, 10, 40)
    if not newresult1:
        print("No Found")
    else:
        print(newresult1)

    result2 = set()
    g2 = DataSampling(float, (0, 100), 8)
    while True:
        try:
            mydict2 = {'type': datatype, 'data': next(g2)}
            mycol.insert_one(mydict2)
        except StopIteration:
            break
    print("DataSamping:")
    for x in mycol.find():
        result2.add(x)
    print(result2)
    newresult2 = DataSelect(result2, float, 1.5, 65.5)
    if not newresult2:
        print("No Found")
    else:
        print(newresult2)

    result3 = set()
    g3 = DataSampling(str, string.ascii_letters + string.digits, 8)
    while True:
        try:
            mydict3 = {'type': datatype, 'data': next(g3)}
            mycol.insert_one(mydict3)
        except StopIteration:
            break
    print("DataSamping:")
    for x in mycol.find():
        result3.add(x)
    print(result3)
    newresult3 = DataSelect(result3, str, "A", "c")
    if not newresult3:
        print("No Found")
    else:
        print(newresult3)

 except Exception as e:
        print(e)

apply()

