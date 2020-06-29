##!/usr/bin/python3
"""
  Author:  Y wang
  Purpose: Generate random data set.
  Created: 10/6/2020
"""
#随机数生成
import random
import string
def dataSampling(datatype, datarange, num, strlen=8):#固定参数；可变参数 *args；默认参数；关键字参数 **kwargs
    '''
    :Description: Generate a given condition random data set.
    :param datatype: dddd
    :param datarange: iterable data set
    :param num: number
    :param strlen:
    :return: a dataset
    '''
    try:
        result = set()
        for index in range(0, num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
            elif datatype is float:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
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
                raise NoneException
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
        except NoneException:
            print("Error in dataSampling")
        finally:
            print("Yes")
def apply():
    result1= dataSampling(str, string.ascii_letters+string.digits+"@#$!", 10)
    print(result1)
    result2 = dataScreening(result1,string.digits)
    print(result2)
    result3 = dataSampling(float,(1,1000),100)
    print(result3)
    result4 = dataScreening(result3,10,20)
    print(result4)
    result5 = dataSampling(float,(100,150),10)
    print(result5)
    result6 = dataScreening(result5,string.digits)
    print(result6)

apply()


