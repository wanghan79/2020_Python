##!/usr/bin/python3
"""
  Author:  Ying Wang
  Purpose: Generate random data set by decorator
  Created: 15/6/2020
"""
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *conditions,strlen=10):
        result = set()
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return func(result,*conditions)
    return wrapper
@dataSampling
def dataScreening(data, *conditions):
    result = set()
    for i in data:
        if type(i) is int:
            it = iter(conditions)
            if next(it)<=i and next(it)>=i:
                result.add(i)
        elif type(i) is float:
            it = iter(conditions)
            if next(it)<=i and next(it)>=i:
                result.add(i)
        elif type(i) is str:
            for substr in conditions:
                if substr in i:
                    result.add(i)
    print(result)
#int
dataScreening(int,[0,150],150,10,40)
#float
dataScreening(float,[0,200],200,20,70)
#str
dataScreening(str,string.ascii_letters+string.digits,1000,'bc','abb')