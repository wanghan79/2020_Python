"""
  Author:  JLH2018010984
  Created: 2020/6/26
"""

import random
import string

def print_line():
    print("*" * 100)

print_line()

def dataSampling(func):
    def wrapper(datatype,datarange,num,*args,strlen=8):
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
            while len(result)<num:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        print('随机生成：', result)
        return func(result,*args)


    return wrapper

@dataSampling

def dataScreening(data,*args):
        resultT = set()
        for i in data:
            if type(i) is int:
                T = iter(args)
                if next(T)<=i and next(T)>=i:
                    resultT.add(i)
            elif type(i) is float:
                T = iter(args)
                if next(T)<=i and next(T)>=i:
                    resultT.add(i)
            elif type(i) is str:
                for Screening_str in args:
                    if Screening_str in i:
                        resultT.add(i)
        print('筛选后：', resultT)

#set()为无符合结果

dataScreening(int,(0,101),20,5,20)
dataScreening(float,(0,101),20,5,20)
dataScreening(str,string.printable,6,'a'or'b')

print_line()