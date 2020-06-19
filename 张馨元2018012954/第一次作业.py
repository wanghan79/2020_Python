##!/usr/bin/python3
"""
  Author:  XinYuan.Zhang
  Purpose: Generate random data set.
  Created: 19/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    try:
        if datatype is int:
            while True:
                it=iter(datarange)
                i = random.randint(next(it), next(it))
                result.add(i)
                if len(result)>=num:
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
               if len(result)>=num:
                   break
        return result
    except ValueError:
        print("传入参数有误")
    except TypeError:
        print("类型有误")
    except Exception as e:
        print(e)


def dataScreening(data,*ange):
    aresult = set()
    try:
        for j in data:
            if type(j) is int or type(j) is float:
                it = iter(ange)
                if next(it) <= j <= next(it):
                    aresult.add(j)
            elif type(j) is str:
                for substr in ange:
                    if substr in j:
                        aresult.add(j)
    except ValueError:
        print("参数有误")
    except TypeError:
        print("类型有误")
    except Exception as e:
        print(e)
    return aresult

def apply():
    try:
        result1 = dataSampling(int, (0, 100), 5)
        print(result1)
        aresult1 = dataScreening(result1, 10, 90)
        if not aresult1:
            print(" not found ")
        else:
            print(aresult1)

        result2 = dataSampling(float, (0, 100), 5)
        print(result2)
        aresult2 = dataScreening(result2, 10, 90)
        if not aresult2:
            print(" not found ")
        else:
            print(result2)

        result3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 5)
        print(result3)
        aresult3 = dataScreening(result3,'a')
        if not aresult3:
          print(" not found ")
        else:
          print(aresult3)

    except Exception as ex:
      print(ex)

apply()
