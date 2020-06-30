

import random
import string
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["liyl"]
dblist = myclient.list_database_names()
if "liyl" in dblist:
    print('liyl exists!')
mycol = mydb["key"]

def dataSampling(dataType, dataRange, num, strlen=8):

    try:
        if dataType is int:
            for i in range(0,num):
                j = iter(dataRange)
                temp = random.randint(next(j), next(j))
                yield temp
        elif dataType is float:
            for i in range(0,num):
                j = iter(dataRange)
                temp = random.uniform(next(j), next(j))
                yield temp
        elif dataType is str:
            for i in range(0,num):
                temp = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                yield temp
        else:
            pass

    except TypeError:
        print("The Type is error.")
    except MemoryError:
        print("The Memory is error.")
    except ValueError:
        print("The value is not correct")
    except Exception as e:
        print(e)
        print("ERROR")

def dataScreening(dataType,*args):
    result = set()
    # Screening

    if dataType is int:
        num = iter(args)
        for item in mycol.find({"data": {"$gt": next(num), "$lt": next(num)}}):
            result.add(item['data'])
    elif dataType is float:
        num = iter(args)
        for item in mycol.find({"data": {"$gt": next(num), "$lt": next(num)}}):
            result.add(item['data'])
    elif dataType is str:
        for substr in args:
            for item in mycol.find({"data": {"$regex": substr}}):
                result.add(item['data'])
    return result

def apply():
    for i in mycol.find():
        print(i)
    print("-----------------------------------")
    #int 类型
    result_Int = dataSampling(int, (0, 300), 100)

    for i in result_Int:
        mycol.insert_one({"type":'int','data':i})

    print(dataScreening(result_Int, (50, 100)))
    print("\n")
    #float 类型
    result_Float = dataSampling(float, (0.0, 120.0), 100)
    for i in result_Float:
        mycol.insert_one({"type": 'float', 'data': i})

    print(dataScreening(result_Float, (50.0, 100.0)))
    print("\n")


    #str类型
    result_Str = dataSampling(str, string.ascii_letters + string.digits, 100, 20)
    for substr in result_Str:
        mycol.insert_one({"type":'str','data':substr})


    print(dataScreening(result_Str, 'at'))
    print("\n")


apply()



