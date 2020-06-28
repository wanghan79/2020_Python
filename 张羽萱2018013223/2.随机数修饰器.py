"""
Author: zhang yuxuan 2018013223
Purpose: Generate random data set by decoration.
Created: 19/6/2020

"""
import random
import string


def DataSampling(func):
    def wrapper(datatype, datarange, num, *conditions, strlen=10):
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
        print("Before selecting: ", result)
        return func(result, *conditions)
    return wrapper

@DataSampling
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

    print(result)
    print("After selecting: ", result)


dataScreening(int, [0, 200], 100, 10, 50)
dataScreening(float, [0, 100], 100, 0, 10)
dataScreening(str, string.printable, 10, 'm')