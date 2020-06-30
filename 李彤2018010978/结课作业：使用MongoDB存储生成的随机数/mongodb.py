'''
Description:Use MONGODB to store the generated random numbers and
            to filter the data by querying it.
parameter:datarange
parameter:datatype
parameter:num
author:li tong
'''
import random
import string
from collections.abc import Iterable
import pymongo
class typeException(Exception):
    pass
class rangeException(Exception):
    pass
def dataSampling(datatype,datarange,num,strlen=10,**kwargs):

    try:

        if (isinstance(datarange, Iterable) == 0):
            raise rangeException("datarange不可迭代")
        if datatype is int:
            for index in range(1, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            for index in range(1, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            for index in range(1, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
        else:
            raise typeException("datatype不可识别")

    except typeException as e:
        print(e)
    except rangeException as e:
        print(e)

def dataScreen(data,*args):
    result=set()
    try:
        n=len(args)

        if(n==1 and isinstance(args[0],str)):
            for mystr in args:
                for index in data.find({"Value": {"$regex": mystr}}):
                    result.add(index["value"])
        elif(n==2 and isinstance(args[0],int) and isinstance(args[1],int)):
            for index in data.find({"type":"int","value":{"$gt":args[0],"$lt":args[1]}}):
                    result.add(index["value"])
        elif (n == 2 and isinstance(args[0], float) and isinstance(args[1], float)):
            for index in data.find({"type": "float", "value": {"$gt": args[0], "$lt": args[1]}}):
                result.add(index["value"])
        else:
            raise Exception("args个数错误")
    except Exception as e:
        print(e)
    finally:
        return result


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    dblist= myclient.list_database_names()
    if "runoobdb" in dblist:
        print("runoobdb数据库已存在")
    else:
        mydb=myclient["runoobdb"]
        collist=mydb.list_collection_names()
        if "data" in collist:
            print("data集合已存在")
        else:
            mycol = mydb["data"]
    i=dataSampling(int,(10,100),100)
    f=dataSampling(float,(10.0,50.0),100)
    s=dataSampling(str,string.ascii_letters+string.digits,15,8)
    n=input("将输出前n个整型变量")
    n=int(n)
    j=0
    while j<n:
        temp = next(i)
        mydict={"type":"int","value":temp}
        x = mycol.insert_one(mydict)
        j = j + 1
        print(x)
        print(temp)
    re=dataScreen(mycol,30,50)
    print("这",n,"个整型变量符合要求的有:",re)

    m = input("将输出前m个浮点型变量")
    m = int(m)
    result = set()
    j = 0
    while j < m:
        temp = next(f)
        mydict = {"type": "float",  "value": temp}
        x = mycol.insert_one(mydict)
        j = j + 1
        print(x)
        print(temp)
    re = dataScreen(mycol,30.0,50.0)
    print("这", m, "个浮点型变量符合要求的有:", re)

    k = input("将输出前k个字符串")
    k = int(k)
    result = set()
    j = 0
    while j < k:
        temp = next(s)
        mydict = {"type": "str", "value": temp}
        x=mycol.insert_one(mydict)
        j = j + 1
        print(x)
        print(temp)
    re = dataScreen(mycol,'w')
    print("这", k, "个字符串符合要求的有:", re)

if __name__ == "__main__":
    main()

