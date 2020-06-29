'''
    Author: XudongWang
    Purpose: Second Homework: Generate random data set
    Data: 20/6/2020
'''

import random
import string

def DataSampling(func):
    def wrapper(datatype,datarange_1,num,datarange_2,strlen=8):
        result=set()
        if datatype is int:
            while len(result)<num:
                it=iter(datarange_1)
                item=random.randint(next(it),next(it))
                result.add(item)
        elif datatype is float:
            while len(result)<num:
                it=iter(datarange_1)
                item=random.uniform(next(it),next(it))
                result.add(item)
        elif datatype is str:
            while len(result)<num:
                item=''.join(random.SystemRandom().choice(datarange_1) for _ in range(strlen))
                result.add(item)
        print(result)
        return func(result,datatype,datarange_2)
    return wrapper

@DataSampling
def dataSelect(data,datatype,datarange_2):
    # try:
        newresult=set()
        
        for it in data:
            if datatype is int:
                Range = iter(datarange_2)
                if next(Range)<=it and it<=next(Range):
                    newresult.add(it)
            elif datatype is float:
                Range = iter(datarange_2)
                if (next(Range)<=it<=next(Range)):
                    newresult.add(it)
            elif datatype is str:
                for target in datarange_2:
                    if(target in it):
                        newresult.add(it)
    # except Exception as ex:
    #     print(ex)
    # else :
        print(newresult)
        return newresult
dataSelect(str, string.ascii_letters + string.digits + "w", 8,'a')
dataSelect(int,(100,200),10,(100,140))
dataSelect(float,(100,200),10,(100,140))