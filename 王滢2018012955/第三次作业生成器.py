##!/usr/bin/python3
"""
Author: Ying Wang
Purpose:Generate random data set by an Iterator.
Created:21/6/2020
"""
import random
import string
def dataSampling(datatype, datarange, num, strlen=8):#固定参数；可变参数 *args；默认参数；关键字参数 **kwargs
    try:
        result = set()
        for index in range(0, num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
                continue
            elif datatype is float:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
            else:
                continue
    except (OverflowError,IOError):
        print('process exception')
    finally:
        return result
#随机数筛选
def dataScreening(data, *conditions):
        try:
            result = set()
            if data is None:
                raise ValueError
            else:
                for item in data:
                    if type(item) is int or type(item) is float:
                        it = iter(conditions)
                        if next(it) <= item <= next(it):
                            result.add(item)
                    elif type(item) is str:
                        for substring in conditions:
                            if substring in item:
                                result.add(item)
                                return result
        except TypeError:
            print("请输入正确类型")
        except ValueError:
            print("Error in dataSampling")
        finally:
            print("Yes")
def apply():
    try:
        #int型
        result1 = set()
        a = dataSampling(int, (0, 500), 100)
        for x in range(0, 100):
            result1.add(next(a))
        print("int型结果")
        print(result1)
        result2 = dataScreening(result1, 50,60)
        print("筛选出的int结果")
        print(result2)
        #float型
        result3 = set()
        b = dataSampling(float, (0, 500), 100)
        for x in range(0, 100):
            result3.add(next(b))
        print("float型结果")
        print(result3)
        result4 = dataScreening(result3, 50,60)
        print("筛选出的float型结果")
        print(result4)
         #字符串型
        result5 = set()
        c = dataSampling(str, string.ascii_letters + string.digits, 2000, 20)
        for x in range(0, 2000):
            result5.add(next(c))
        print("字符串型结果")
        print(result5)
        result6 = dataScreening(result5, 'bc', 'bcc')
        print("筛选出的字符串型结果")
        print(result6)
    except Exception as ex:
        print(ex)
apply()
