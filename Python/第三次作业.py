##!/usr/bin/python3
"""
  Author:  yinzhixoang
  Purpose: Generate random data set.
  Created: 30/6/2020
"""
import random
import string

def dataSampling(func):
        def wrapper(datatype, datarange, num, strlen=5):
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
                except RuntimeError:
                        print("超时")
                except TypeError:
                           print("类型错误")
                finally:
                         print("正常运行")
                return wrapper


@dataSampling
def dataScreening(data,*args):
        try:
                result = set()
                for i in range(0, data):
                        if type(i) is int or type(i) is float:
                                num = iter(args)
                        elif type(i) is str:
                                for substr in args:
                                        if substr in i:
                                                result.add(i)
                return (result)
        except RuntimeError:
                print("超时")
        except TypeError:
                print("类型错误")
        finally:
                print("正常运行")


result = dataSampling(str, string.ascii_letters+string.digits+"!@#$%^&*", 10)
print(result)
