'''
Description:The random number generation is encapsulated as a modifier function
            (or a modifier class) , which is used to
            modify the random number filter function for data filtering
        parameter:datarange
parameter:datatype
parameter:num
author:li tong
'''

import random
import string
from collections.abc import Iterable
class typeException(Exception):
    pass
class rangeException(Exception):
    pass
def dataSampling(func):
    def wrapper(datatype,datarange,num,*args,strlen=10):
        result = set()
        try:
            if (isinstance(datarange, Iterable) == 0):
                raise rangeException("datarange不可迭代")
            elif datatype is int:
                for index in range(1, num):
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
            elif datatype is float:
                for index in range(1, num):
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
            elif datatype is str:
                for index in range(1, num):
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
            else:
                raise typeException("datatype不可识别")

        except typeException as e:
            print(e)
        except rangeException as e:
            print(e)
        else:
            print(result)
            return func(result,*args)
    return wrapper

@dataSampling
def dataScreen(data,*args):
    result=set()
    try:
        if(isinstance(data, Iterable) == 0):
            raise Exception("data不可迭代")
        n=len(args)

        if(n==1 and isinstance(args[0],str)):
            for index in data:
                if index.find(args[0]) >= 0:
                    result.add(index)
        elif(n==2 and isinstance(args[0],int) and isinstance(args[1],int)):
            for index in data:
                if(index>=args[0] and index<=args[1]):
                    result.add(index)
        elif (n == 2 and isinstance(args[0], float) and isinstance(args[1], float)):
            for index in data:
                if (index >= args[0] and index <= args[1]):
                    result.add(index)
        else:
            raise Exception("args个数错误")
    except Exception as e:
        print(e)
    else:
        print(result)


if __name__ == "__main__":
    dataScreen(int, (10, 100), 100, 30, 50)
    dataScreen(float, (10.0, 50.0), 100, 30.0, 50.0)
    dataScreen(str, string.ascii_letters + string.digits, 15, 'w')


