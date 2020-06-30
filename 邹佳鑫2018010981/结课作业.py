#邹佳鑫结课作业

import random
import string
import pymongo

myclient = MongoClient("mongodb://localhost:27017")
mydb = myclient["zjx"]
mycol = mydb["form"]
mycol.drop() 
def create_set(datatype, datarange, num, strlen=8):
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
                continue

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
        else:
            print('请输入datatype:int、float、str!')
    except OverflowError:
        print('数值运算超过最大限制')
    except TypeError:
        print("The type is error.")
    except ValueError:
        print("The value is error.")
    except Exception as e:
        print("ERROR:",e)
def dataScreening(datatype, result, *conditions):
    try:
        for i in mycol.find({},{'num':1}):
            if datatype is int:
                it = iter(datarange)
                if next(it) <= i['num'] <= next(it):
                    print(i['num'])
                continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= i['num'] <= next(it):
                    print(i['num'])
                continue

            elif datatype is str:
                if i['num'].find(datarange) != -1:
                    print(i['num'])
                continue
    except OverflowError:
        print('数值运算超过最大限制')
    except TypeError:
        print("The type is error.")
    except ValueError:
        print("The value is error.")
    except Exception as e:
        print("ERROR:",e)
def apply():
    data_int = dataSampling(int, (1, 1000), 5) 
    data_float = dataSampling(float, (1.0, 1000.2), 5)
    data_str = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)

    dataresult_int = dataScreening(int, data_int, 10, 500)
    dataresult_float = dataScreening(float, data_float, 10.8, 500.9)
    dataresult_str = dataScreening(str, data_str, 'a', 'at')

    mydict_int = {'type': 'int', 'data': dataresult_int}
    mydict_float = {'type': 'float', 'data': dataresult_float}
    mydict_str = {'type': 'str', 'data': dataresult_str}
    mycol.insert_one(mydict_int)
    mycol.insert_one(mydict_float)
    mycol.insert_one(mydict_str)


apply()
