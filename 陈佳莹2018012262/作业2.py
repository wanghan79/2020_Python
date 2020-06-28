"""
Author:Chen Jiaying
Purpose:Generate random data set by decoration.
Created:10/6/2020
"""
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *conditions, strlen=8):
        result=set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) <num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return func(result, *conditions)
    return wrapper
@dataSampling
def dataScreening(data, *conditions):
    result = set()
    for i in data:
            if type(i) is int or type(i) is float:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.add(i)
            elif type(i) is str:
                for tstr in conditions:
                    if tstr in i:
                        result.add(i)
    return result

def apply():
    result1 = dataScreening(int, [0, 100], 30 , 0 , 20)#int
    print(result1)

    result2 = dataScreening(float, [0, 100], 30 , 0 , 20)#float
    print(result2)

    result3 = dataScreening(str, string.ascii_letters + string.digits, 100, 'a')#str
    print(result3)

apply()