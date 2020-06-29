"""
  Author:  Yihang.Gao  高艺航
StuNumber: 2018012950
  Purpose: Generate random data set by generator.
  Created: 19/6/2020
"""
import random
import string


def DataSampling(datatype, datarange, num, strlen=8):
    if datatype is int:
        for i in range(0, num):
            it = iter(datarange)
            pg = random.randint(next(it), next(it))
            yield pg
    elif datatype is float:
        for i in range(0, num):
            it = iter(datarange)
            pg = random.uniform(next(it), next(it))
            yield pg
    elif datatype is str:
        for i in range(0, num):
            pg = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield pg


def DataScreening(data, *args):
    result = set()
    for pg in data:
        if type(pg) is int:
            it = iter(args)
            if next(it) <= pg <= next(it):
                result.add(pg)
        elif type(pg) is float:
            it = iter(args)
            if next(it) <= pg <= next(it):
                result.add(pg)
        elif type(pg) is str:
            for substr in args:
                if substr in pg:
                    result.add(pg)
    return result

def work():
#int型
    res1 = set()
    ans1 = DataSampling(int, (1, 800), 100)
    while True:
        try:
            res1.add(next(ans1))
        except StopIteration:
            break
    print("筛选前：", res1)
    res2 = DataScreening(res1, 20, 100)
    print("筛选后：", res2)
#float型
    res3 = set()
    ans2 = DataSampling(float, (1, 800), 10)
    while True:
        try:
            res3.add(next(ans2))
        except StopIteration:
            break
    print("筛选前：", res3)
    res4 = DataScreening(res3, 5.0, 55.0)
    print("筛选后：", res4)
#string型
    res5 = set()
    ans3 = DataSampling(str, string.ascii_letters+string.digits, 10,1)
    while True:
        try:
            res5.add(next(ans3))
        except StopIteration:
            break
    print("筛选前：", res5)
    res6 =DataScreening(res5, string.ascii_letters)
    print("筛选后：", res6)

work()