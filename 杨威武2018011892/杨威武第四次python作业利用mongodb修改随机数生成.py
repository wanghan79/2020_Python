import random
import string
import pymongo

def datasampling(datatype,datarange,num,strlen=8):
    if datatype is int :
        for i in range(0, num):
            it = iter(datarange)
            item = random.randint(next(it),next(it))
            yield  item
    elif datatype is float:
        for i in range(0, num):
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
    elif datatype is str:
        for i in range(0, num):
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item

def dataScreening(data,*args):
    result = list()
    for i in data:
        if type(i) == type(args[0]):
            if isinstance(i,int):
                if i >= args[0] and i <= args[1]:
                     result.append(i)
            elif isinstance(i,float):
                if i >= args[0] and i <= args[1]:
                    result.append(i)
            elif isinstance(i,str):
                flag=1
                for x in i:
                    if x  not in args[0]:
                        flag = 0
                if flag:
                    result.append(i)
    return result


def check():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["number"]
    myint = mydb["intnumber"]
    mydouble = mydb["doublenumber"]
    mystring = mydb["strings"]

    result1 = list();
    f1=datasampling(int,(1,1000),100)
    while True:
        try:
            result={"value":next(f1)};
            myint.insert_one(result)
        except StopIteration:
            break
    print("整型随机数生成：",end="")
    for x in myint.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result1.append(n)
    print(result1)
    results1s = dataScreening(result1, 10, 100)
    print("筛选后的整型随机数：",results1s)

    result2=list()
    f2 = datasampling(float, (1, 1000), 100)
    while True:
        try:
            result={"value":next(f2)};
            mydouble.insert_one(result)
        except StopIteration:
            break
    print("浮点随机数生成：",end="")
    for x in mydouble.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result2.append(n)
    print(result2)
    results2s = dataScreening(result2, 10.0, 100.0)
    print("筛选后的浮点随机数：",results2s)

    result3 = list()
    f3 = datasampling(str, string.ascii_letters+string.digits, 100,10)
    while True:
        try:
            result = {"value": next(f3)};
            mystring.insert_one(result)
        except StopIteration:
            break
    print("字符随机数生成：",end="")
    for x in mystring.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result3.append(n)
    print(result3)
    results3s = dataScreening(result3, string.ascii_letters)
    print("筛选后的字符随机数：", results3s)

check()