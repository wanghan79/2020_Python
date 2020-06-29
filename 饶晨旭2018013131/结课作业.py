import random
import string
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["runoobdb"]

dblist=myclient.list_database_names()
if "runoobdb"in dblist:
    print("数据库已存在")
mycol=mydb["sites"]
collist=mydb.list_collection_names()
if "sites" in collist:
    print("集合已存在")
mycol.drop()

def dataSampling(datatype, datarange, num, strlen=8, dataType=None):
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                mycol.insert_one({"dataType": dataType, "data": item})

        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                mycol.insert_one({"dataType": dataType, "data": item})

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange)
                               for _ in range(strlen))
                mycol.insert_one({"dataType": dataType, "data": item})

     except ValueError:
     print("Error: 无效参数")
     except TypeError:
     print("Error: 对类型无效的操作，无法迭代")


def dataScreening(datatype, *datarange):
    try:
        result = set()
        for x in result:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    result.add(x)

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    result.add(x)

            elif datatype is str:
                if x.find(datarange) != -1:
                    result.add(x)
        return result
        except ValueError:
        print("Error: 无效参数")
        except TypeError:
        print("Error: 对类型无效的操作，无法迭代")




def apply(mydict=None):
    dataSampling(int, {1, 100}, 10)
    ans = mycol.insert_one(mydict)
    print(ans)
    for x in mycol.find():
        print(x)

    dataSampling(float, {1.0, 100.0}, 10)
    ans = mycol.insert_one(mydict)
    print(ans)
    for x in mycol.find():
        print(x)

    dataSampling(str, string.printable, 50, 10)
    ans = mycol.insert_one(mydict)
    print(ans)
    for x in mycol.find():
        print(x)


apply()
