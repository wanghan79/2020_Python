##!/usr/bin/python3
# """
#   Author:  XinYuan.Zhang
#   Purpose: Decorator and Generate random data set.
#   Created: 19/6/2020
# """

import string
import random

def make (func):
    def dataSampling(datatype, datarange, num,condition, strlen=8):
        result = set()
        try:
            if datatype is int:
                while True:
                    it = iter(datarange)
                    i = random.randint(next(it), next(it))
                    result.add(i)
                    if len(result) >= num:
                        break
            elif datatype is float:
                while True:
                    it = iter(datarange)
                    i = random.uniform(next(it), next(it))
                    result.add(i)
                    if len(result) >= num:
                        break
            elif datatype is str:
                while True:
                    i = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(i)
                    if len(result) >= num:
                        break
            return func(result,condition)
        except ValueError:
            print("传入参数有误")
        except TypeError:
            print("类型有误")
        except Exception as e:
            print(e)
    return dataSampling


@make
def dataScreening(data, datarange):
    aresult=set()
    try:
        for j in data:
            if type(j) is int:
                it = iter(datarange)
                if next(it) <= j <= next(it):
                    aresult.add(j)
                continue

            elif type(j) is float:
                it = iter(datarange)
                if next(it) <= j <= next(it):
                    aresult.add(j)
                continue

            elif type(j) is str:
                if j.find(datarange) != -1:
                    aresult.add(j)
                continue
    except ValueError:
     print("参数有误")
    except TypeError:
     print("类型有误")
    except Exception as e:
     print(e)
    return aresult


print(dataScreening(int,{1,100},10,(5,80)))
print(dataScreening(float,{1,100},10,(5,80)))
print(dataScreening(str,string.ascii_letters + string.digits + "@#$!",10,'a'))