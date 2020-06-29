##!/usr/bin/python3
"""
  Author:  ZhengPeng.Han
  Purpose: Generate random data set.
  Created: 28/5/2020
"""
import random
import string
def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description:Using the generator generates a random data given set of conditions
    :param datatype: The type of data which include int float and string
    :param datarange: iterable data set
    :param num: Input parameters that means The final result of the number of elements
    :param strlen:The length of input strings
    :return: a dataset
    '''
    try:
        if (datatype is int):
            for i in range(num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item  #使用yield关键字以实现生成器
        elif (datatype is str):
            for i in range(num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item  #使用yield关键字以实现生成器
        elif (datatype is float):
            for i in range(num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item  #使用yield关键字以实现生成器
    except ValueError:
        print("传入参数无效")
    except TypeError:
        print("类型错误，参数可能无法迭代")
    except Exception as e:
        print(e)

a=dataSampling(int, (0,100), 5)
b=set()
for i in range(5):
    b.add(next(a))
print("生成："+b)