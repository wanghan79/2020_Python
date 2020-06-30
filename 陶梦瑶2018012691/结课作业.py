import random
import string
import pymongo

def dataSampling(datatype, datarange, num, strlen=8):
    try:
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item

        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item

        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item

        else:
            pass

    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")
    except Exception as e:
        print(e)

def apply():

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tmydata"]
    dblist = myclient.list_database_names()
    if 'tmydata' in dblist:
        print('The database exists')
    mycol = mydb['colletion']

    result1 = dataSampling(int, (0, 100), 10)
    result2 = dataSampling(float, (0, 100), 10)
    result3 = dataSampling(str, string.ascii_letters + string.digits, 10, 5)

    mycol.drop()
    for item in result1:
        mycol.insert_one({'data': item, 'datatype': 'int'})
    for item in result2:
        mycol.insert_one({'data': item, 'datatype': 'float'})
    for item in result3:
        mycol.insert_one({'data': item, 'datatype': 'str'})

    for item in mycol.find():
        print(item)
        
    for item in mycol.find({"data": {"$lt": 70, "$gt": 30}}):
        print(item)
    for item in mycol.find({"data": {"$lt": 70, "$gt": 30}}):
        print(item)
    for item in mycol.find({"data": {"$regex": 't'}}):
        print(item)

apply()