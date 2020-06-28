"""
Author:Chenjiaying
Purpose:Generate random data set by an Iterator.
Created:16/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    try:
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            while len(result) <num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
        return result
    except TypeError:
        print("类型错误.")
    except ValueError:
        print("参数无效.")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def dataScreening(data, *conditions):
    result = set()
    try:
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
    except TypeError:
        print("类型错误.")
    except ValueError:
        print("参数无效.")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def apply():
    result = dataSampling(int, (0, 100), 30)
    result1 = set()
    for i in range(0, 30):
        result1.add(next(result))
    print(result1)
    print(dataScreening(result1, 0, 20))

    result = dataSampling(float, (0, 100), 15)
    result2 = set()
    for i in range(0,30):
        result2.add(next(result))
    print(result2)
    print(dataScreening(result2, 0, 20))

    result = dataSampling(str, string.ascii_letters + string.digits, 100, 30)
    result3= set()
    for i in range(0,30):
        result3.add(next(result))
    print(result3)
    print(dataScreening(result3, 'a'))
apply()