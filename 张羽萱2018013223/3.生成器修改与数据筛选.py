"""
Author: Zhang yuxuan 2018013223
Purpose: Generate random data set by generator.
Created: 19/6/2020

"""
import random
import string


def DataSampling(datatype, datarange, num, strlen=8):
    if datatype is int:
        for i in range(0, num):
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item
    elif datatype is float:
        for i in range(0, num):
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
    elif datatype is str:
        for i in range(0, num):
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item



def dataScreening(data, *conditions):
    result = set()
    for item in data:
        if type(item) is int:
            it = iter(conditions)
            if next(it) <= item <= next(it):
                result.add(item)
        elif type(item) is float:
            it = iter(conditions)
            if next(it) <= item <= next(it):
                result.add(item)
        elif type(item) is str:
            for substr in conditions:
                if substr in item:
                    result.add(item)
    return result


def Generator():
#int
    result1 = set()
    r1 = DataSampling(int, (1, 1000), 100)
    while True:
        try:
            result1.add(next(r1))
        except StopIteration:
            break
    print("Before selecting：", result1)
    result2 = dataScreening(result1, 10, 100)
    print("After selecting：", result2)
#float
    result3 = set()
    r2 = DataSampling(float, (1, 100), 10)
    while True:
        try:
            result3.add(next(r2))
        except StopIteration:
            break
    print("Before selecting：", result3)
    result4 = dataScreening(result3, 1.0, 10.0)
    print("After selecting：", result4)
#string
    result5 = set()
    r3 = DataSampling(str, string.ascii_letters+string.digits, 10,1)
    while True:
        try:
            result5.add(next(r3))
        except StopIteration:
            break
    print("Before selecting：", result5)
    result6 = dataScreening(result5, string.ascii_letters)
    print("After selecting：", result6)


Generator()
