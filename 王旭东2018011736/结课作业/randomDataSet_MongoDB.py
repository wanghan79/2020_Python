'''
    Author: XudongWang
    Purpose:  Generate random data set
    Data: 28/6/2020
'''

import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wangxd"]
mycol = mydb["sites"]
mycol.drop()

def dataSampling(datatype, datarange, num, strlen=8):
    try:
        if datatype is int:
            for i in range(0,num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item 
        elif (datatype is float):
            for i in range(0,num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item 
        elif (datatype is str):
            for i in range(0,num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
        
        except Exception as ex:
        print(ex)
    else :
        return result


def dataSelect(result,datatype,*args):
    try:  
        newresult=set()
        for it in result:
            if datatype is int:
                Range = iter(args)
                if (next(Range)<=it<=next(Range)):
                    newresult.add(it)
            elif datatype is float:
                Range = iter(args)
                if (next(Range)<=it<=next(Range)):
                    newresult.add(it)
            elif datatype is str:
                for target in args:
                    if(target in it):
                        newresult.add(it)
    except Exception as ex:
        print(ex)
    else:
        return newresult


def apply():
    try:
        #test: data Type is int
        result=dataGeneration(int,(0,100))
        result_1=set()
        while len(result_1) < 8:
            result_1.add(next(result))
        print("生成的整形随机数为：",result_1)
         print("筛选后的整形随机数为：",newresult_1)
        print("-------------------\n")_1=dataSelect(result_1,int,10,40)
        print("筛选后的整形随机数为：",newresult_1)
        print("-------------------\n")
        
        #test: data Type is float
        result = dataGeneration(float, (0, 100))
        result_2=set()
        while len(result_2) < 8:
            result_2.add(next(result))
        print("生成的浮点型随机数为：",result_2)
        newresult_2 = dataSelect(result_2, float,20,50)
        print("筛选后的浮点型随机数为：",newresult_2)
        print("-------------------\n")
        
        #test: data Type is str
        result = dataGeneration(str,string.ascii_letters + string.digits)
        result_3=set()
        while len(result_3) < 8:
            result_3.add(next(result))
        print("生成的随机字符串为：",result_3)
        newresult_3 = dataSelect(result_3,str,'A','b')
        print("筛选后的随机字符串为：",newresult_3)
        print("-------------------\n")
        data_one = {'type': 'int', 'data':  newresult_1}
        data_tow = {'type': 'float', 'data': newresult_2}
        data_three = {'type': 'str', 'data': newresult_3}
        mycol.insert_one(data_one)
        mycol.insert_one(data_tow)
        mycol.insert_one(data_three)
    except Exception as ex:
      print(ex)

apply()
eg_1 = mycol.find_one({'type': 'int'})
print("-------------------\n")
print("inttype:",eg_1)
eg_2 = mycol.find_one({'type': 'float'})
print("float:",eg_2)
print("-------------------\n")
eg_3 = mycol.find_one({'type': 'str'})
print("strtype:",eg_3
print("-------------------\n"))
