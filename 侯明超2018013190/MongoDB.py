import random
import string
import pymongo


def dataSampling(datatype, datarange, num, strlen=8):
    try:
        result = set()
        if (datatype is int):
            while len(result) < num:
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                result.add(item)
        elif (datatype is float):
            while len(result) < num:
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                result.add(item)
        elif (datatype is str):
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return result
    except ValueError:
        print("error:参数无效")
    except TypeError:
        print("error:类型错误")
    ##else:
    ##    return result

def dataScreening(data,*args):
    try:
        ansresult = set()
        for i in data:
            if (type(i) is int):
                cond = iter(args)
                if(next(cond) <= i and next(cond) >= i):
                    ansresult.add(i)
            elif (type(i) is float):
                    cond = iter(args)
                    if (next(cond) <= i and next(cond) >= i):
                        ansresult.add(i)
            elif (type(i) is str):
                for condstr in args:
                    if(condstr in i):
                        ansresult.add(i)
    except ValueError:
        print("error:参数无效")
    except TypeError:
        print("error:类型错误")
    return ansresult

def apply():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["Data"]
    mycolint = mydb["Data_int"]
    mycolfloat = mydb["Data_float"]
    mycolstr = mydb["Data_str"]

    result = set()
    j = dataSampling(str, string.printable, 6)
    for index in range(0, 10):
        mycolstr.insert_one(next(j))
    for x in mycolstr.find():
        result.add(x.get("Data"))
    print(result)
    result = dataScreening(result,'a'or'b')
    if not result:
        print("error")
    else:
        print(result)
    print

    result = set()
    j = dataSampling(float, (0, 100), 6)
    for index in range(0, 90):
        mycolfloat.insert_one(next(j))
    for x in mycolfloat.find():
        result.add(x.get("Data"))
    print(result)
    result = dataScreening(result,(20,60))
    if not result:
        print("error")
    else:
        print(result)
    print

    result = set()
    j = dataSampling(int, (0, 100), 6)
    for index in range(0, 90):
        mycolint.insert_one(next(j))
    for x in mycolint.find():
        result.add(x.get("Data"))
    print(result)
    result = dataScreening(result,(20,70))
    if not result:
        print("error")
    else:
        print(result)
    print


if __name__ == "__main__":
    apply()