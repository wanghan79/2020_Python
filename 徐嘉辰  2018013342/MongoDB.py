import random
import string
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["final"]
mycol =mydb['table']
mycol.drop()

def DataSampling(datatype, datarange, num, strlen=8):
    for index in range(0,num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it),next(it))
            yield item
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it),next(it))
            yield item
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item
            continue
        else:
            continue

def DataScreening(data,condition):
    result = set()
    for i in data:
        if type(i) is int:
            if i>=condition[0] and i<=condition[1]:
                result.add(i)
        if type(i) is float:
            if i>=condition[0] and i<=condition[1]:
                result.add(i)
        if type(i) is str:
            for item in condition:
                if item in i:
                    result.add(i)
    return result

def apply():

    result_int = DataSampling(int, [0, 1000], 10)
    result1 = {'type': 'int', 'data': DataScreening(result_int, (100, 500))}
    mycol.insert_one(result1)

    result_float = DataSampling(float, [0, 1000], 10)
    result2 = {'type': 'float', 'data': DataScreening(result_float, (100, 500))}
    mycol.insert_one(result2)

    result_str = DataSampling(str,  string.ascii_letters + string.digits + "@#!$", 10)
    result3 = {'type': 'str', 'data': DataScreening(result_str, 'a')}
    mycol.insert_one(result3)

apply()

ans_result1 = mycol.find_one({"type": 'int'})
print(ans_result1)

ans_result2 = mycol.find_one({"type": 'float'})
print(ans_result2)

ans_result3 = mycol.find_one({"type": 'str'})
print(ans_result3)







