'''
    Author: XudongWang
    Purpose: Third Homework: Generate random data set
    Data: 25/6/2020
'''

import random
import string

def dataSampling(datatype,datarange,strlen=8):
    # try:
        if datatype is int:
            while(1):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            while(1):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is str:
            while(1):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
    # except Exception as ex:
    #     print(ex)

def dataSelect(result,datatype,*args):
    # try:  
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
    # except Exception as ex:
    #     print(ex)
    # else:
        return newresult

def apply():
    # try:
        #test: data Type is int
        result=dataSampling(int,(0,100))
        result_1=set()
        while len(result_1) < 8:
            result_1.add(next(result))
        print("生成的整形随机数为：",result_1)
        newresult_1=dataSelect(result_1,int,20,80)
        print("筛选后的整形随机数为：",newresult_1)
        print("-------------------\n")
        #test: data Type is float
        result = dataSampling(float, (0, 100))
        result_2=set()
        while len(result_2) < 8:
            result_2.add(next(result))
        print("生成的浮点型随机数为：",result_2)
        newresult_2 = dataSelect(result_2, float,20,50)
        print("筛选后的浮点型随机数为：",newresult_2)
        print("-------------------\n")
        #test: data Type is str
        result = dataSampling(str,string.ascii_letters + string.digits)
        result_3=set()
        while len(result_3) < 8:
            result_3.add(next(result))
        print("生成的随机字符串为：",result_3)
        newresult_3 = dataSelect(result_3,str,'W','a')
        print("筛选后的随机字符串为：",newresult_3)
        print("-------------------\n")
    # except Exception as ex:
    #     print(ex)

apply()