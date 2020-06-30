#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : GaoXingyuan
# @FileName: First Random.py
# @Software: PyCharm
import random
import string

def DataSampling(datatype, datarange, num, strlen=10):
    try:
        result = set()
        if datatype is int:
            while True:
                it=iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                if len(result)>=num:
                    break
        elif datatype is float:
            while True:
               it = iter(datarange)
               item = random.uniform(next(it), next(it))
               result.add(item)
               if len(result) >= num:
                    break
        elif datatype is str:
            while True:
               item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
               result.add(item)
               if len(result)>=num:
                   break
    except Exception as e:
        print(e)
    else:
        return result
    finally:
        print(" DataSampling rasults are:")

def DataScreening(data, *conditions):
    try:
        result=set()
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it)<=item<=next(it):
                    result.add(item)
            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)
        return result
    except Exception as e:
        print(e)
    finally:
        print(f"condition is {conditions}")
        print("DataScreening rasults are:")

def apply():
    result=DataSampling(int,[0,100],10)
    print(result)
    screening=DataScreening(result,0,50)
    print((screening))

    result = DataSampling(float, [0, 50], 10)
    print(result)
    screening = DataScreening(result, 25, 50)
    print((screening))

    base_str =string.ascii_letters+string.digits
    result = DataSampling(str,base_str, 1000)
    print(result)
    screening = DataScreening(result, 'ab','abc','abcd')
    print((screening))
apply()