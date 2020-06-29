"""
  Author:JLH2018010984
  Created: 2020/6/27
"""

import random
import string

def print_line():
    print("*" * 100)
print_line()

def dataSampling(datatype, datarange, num, strlen=10):
        result = set()
        if datatype is int:
            for k in range(num):
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                yield item
        elif datatype is float:
            for k in range(num):
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                yield item
        elif datatype is str:
            for k in range(num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item


def dataScreening(data,*args):
        resultT = set()
        for i in data:
            if (type(i) is int):
                T = iter(args)
                if(next(T) <= i and next(T) >= i):
                    resultT.add(i)
            elif (type(i) is float):
                    T = iter(args)
                    if next(T) <=i and next(T) >= i:
                        resultT.add(i)
            elif (type(i) is str):
                for Screening in args:
                    if(Screening in i):
                        resultT.add(i)
        return resultT


def apply():
    result1=set()
    result = dataSampling(int,(0,101), 20)
    while True:
        try:
            result1.add(next(result))
        except StopIteration:
            break
    print("随机生成：",result1)
    Screening1 =dataScreening(result1,5,20)
    print("筛选后：",Screening1)
#int
    result2=set()
    result = dataSampling(float, (0, 101), 20)
    while True:
        try:
            result2.add(next(result))
        except StopIteration:
            break
    print("随机生成：",result2)
    Screening2= dataScreening(result2,5,20)
    print("筛选后：",Screening2)
#float
    result3 = set()
    result = dataSampling(str, string.printable,20)
    while True:
        try:
            result3.add(next(result))
        except StopIteration:
            break
    print("随机生成：",result3)
    Screening3 = dataScreening(result3,'a'or'b'or'c'or'd')
    print("筛选后：",Screening3)
#str

# set()为无符合结果

apply()

print_line()