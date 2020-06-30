import random
import string
import pymongo

def dataSampling(datatype,datarange,num,str_len=8):
    try:
    result=set()
    for index in range(1,num):
        if datatype is int:
            it=iter(datarange)
            item=random.randint(next(it),next(it))
            result.append(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.append(item)
            continue
        elif datatype is str:
            item=''.join(random.SystemRandom().choice(datarange) for _ in range(str_len))
            continue
        else:
            continue
    return result

    except TypeError:
        print("数据类型必须为int,float或str")
    except ValueError:
        print("参数无效")
    except MemoryError:
        print("内存错误")
    except Exception as e:
        print(e)
        print("参数错误")

def apply():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["work"]
    col = db['data']
    
    mycol.drop()
    result1 = dataSampling(int, (1, 20), 5)
    for b in result1:
        mycol.insert_one({'data': b, 'datatype': 'int'})
    for b in mycol.find({"data": {"$lt": 15, "$gt": 5}, "datatype": "int"}):
        print(b)

    mycol.drop()
    result = dataSampling(float,(1, 20), 5)
    for b in result:
        mycol.insert_one({'data': b, 'datatype': 'float'})
    for b in mycol.find({"data": {"$lt": 15, "$gt": 5}, "datatype": "float"}):
        print(b)

    mycol.drop()
    result = dataSampling(str, string.ascii_letters + string.digits, 15, 10)
    for b in result:
        mycol.insert_one({'data': b, 'datatype': 'str'})
    for b in mycol.find({"data": { {"$regex": 'a'}, "datatype": "str"}}):
        print(b)

apply()