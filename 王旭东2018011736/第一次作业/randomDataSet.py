'''
    Author: XudongWang
    Purpose: First Homework: Generate random data set
    Data: 14/6/2020
'''

import random
import string

def DataSampling(datatype,datarange,num,strlen=8):
    try:
        result=set()
        if datatype is int:
            while len(result)<num:
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                result.add(item)
        elif datatype is float:
            while len(result)<num:
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                result.add(item)
        elif datatype is str:
            while len(result)<num:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
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
                if (next(Range)<=it and next(Range)>=it):
                    newresult.add(it)
            elif datatype is float:
                Range = iter(args)
                if (next(Range)<=it and next(Range)>=it):
                    newresult.add(it)
            elif datatype is str:
                for target in args:
                    if(target in it):
                        newresult.add(it)
    except Exception as ex:
        print(ex)
    else :
        return newresult

def apply():
    try:
        #test: data Type is int
        result_1=DataSampling(int,(100,200),8)
        print("生成的整形随机数为：",result_1)
        newresult_1=dataSelect(result_1,int,(20,80))
        print("筛选后的整形随机数为：",newresult_1)
        print("-------------------\n")
        #test: data Type is float
        result_2 = DataSampling(float, (100, 200), 8)
        print("生成的浮点型随机数为：",result_2)
        newresult_2 = dataSelect(result_2, float,(20,50))
        print("筛选后的浮点型随机数为：",newresult_2)
        print("-------------------\n")
        #test: data Type is str
        result_3 = DataSampling(str,string.ascii_letters + string.digits,8)
        print("生成的随机字符串为：",result_3)
        newresult_3 = dataSelect(result_3,str,'W','a')
        print("筛选后的随机字符串为：",newresult_3)
        print("-------------------\n")
    except Exception as ex:
        print(ex)

apply()