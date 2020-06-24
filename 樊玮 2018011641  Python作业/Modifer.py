'''
Author: WeiFan 2018011641
Aim:  Generation and filtering of random numbers——Modifer
Data: 2020/6/17
'''
import random
import string

def DataSampling(function):
    def wrapper(datatype,datarange,num,item1,item2,strlen=8):
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
            while len(result) < num:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)

        print(result)
        return function(result,datatype,item1,item2)
    return wrapper
@DataSampling

def DataSelect(result,datatype,item1,item2):
    newresult=set()
    for it in result:
     if datatype is int:
        if (it>=item1) and (it<=item2):
            newresult.add(it)
     elif datatype is float:
        if (it>=item1) and (it<=item2):
            newresult.add(it)
     elif datatype is str:
        if (item1 in it) and (item2 not in it):
            newresult.add(it)
    print(newresult)

DataSelect(int,(0,100),8,10,40)
DataSelect(float,(0.0,100.0),8,3.5,26)
DataSelect(str,string.ascii_letters + string.digits,8,'a','B')