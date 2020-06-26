"""
  Author:  Yihang.Gao  高艺航
StuNumber: 2018012950
 Purpose: Generate random data set by decoration.
 Created: 19/6/2020
"""
import random
import string
def DataSampling(func):
    def wrap(datatype, datarange, num, *conditions, strlen=10):
        res = set()
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                pg = random.randint(next(it), next(it))
                res.add(pg)
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                pg = random.uniform(next(it), next(it))
                res.add(pg)
        elif datatype is str:
            for i in range(0, num):
                pg = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                res.add(pg)
        print("筛选前: ", res)
        return func(res, *conditions)
    return wrap

@DataSampling
def DataScreening(data, *args):
    res = set()
    for item in data:
        if type(item) is int:
            it = iter(args)
            if next(it) <= item <= next(it):
                res.add(item)
        elif type(item) is float:
            it = iter(args)
            if next(it) <= item <= next(it):
                res.add(item)
        elif type(item) is str:
            for substr in args:
                if substr in item:
                    res.add(item)
    print(res)
    print("筛选后: ", res)
DataScreening(int, [0, 500], 200, 10, 50)
DataScreening(float, [0, 300], 150, 25, 60)
DataScreening(str, string.printable, 10, 'gh')