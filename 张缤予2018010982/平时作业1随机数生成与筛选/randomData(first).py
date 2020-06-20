##!/usr/bin/python3
"""

Author: By.Zhang
Purpose:Generate random data set.
Created:3/5/2020
"""

import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description:Generate a given condition random data set.
    :param datatype: the data type you want to sample including int, float,str.
    :param datarange: iterable data set
    :param num: the number of data you need
    :param strlen: the length of each string you want to generate
    :return: a data set
    '''
    try:
        if num < 0:
            print("Please input correct num in dataSampling.")
        if strlen < 0:
            print("Please input correct strlen in dataSampling")
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) <num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
    except ValueError:
        print("Maybe num is not correct.")
    except NameError:
        print("Maybe your datatype is wrong.")
    except TypeError:
        print("Maybe your num is different with your datatype.")
    except MemoryError:
        print("Maybe memory is full.")
    except:
        raise
    else:
        return result
    finally:
        pass


def dataScreening(data, *conditions): #*args
    '''
    :Description: according the conditions to pick the correct data in dataSampling
    :param data: iterable data set
    :param conditions: the condition such as range or string you want to screen from a data set
    :return: a data set
    '''
    result = set()
    # Screening
    try:
        for i in data:
            if type(i) is int:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.add(i)
            elif type(i) is float:
                it = iter(conditions)
                if next(it) <= i and next(it) >= i:
                    result.add(i)
            elif type(i) is str:
                for teststr in conditions:
                    if teststr in i:
                        result.add(i)
    except Exception as e:
        print("Maybe your condition or data is not correct.")
    return result


def apply():
    # int类型例子
    result_1 = dataSampling(int, [0, 280], 100)
    print('随机生成100个在0~280内的整数:')
    print(result_1)
    print('筛选其中在10~50之间的数:')
    print(dataScreening(result_1, 10, 50))
    print('\n')

    # float类型例子
    result_2 = dataSampling(float, [0, 200], 100)
    print('随机生成100个在0~200内的浮点数:')
    print(result_2)
    print('筛选其中在20~60之间的数:')
    print(dataScreening(result_2, 20, 60))
    print('\n')

    # str类型例子
    str_ex = string.ascii_letters + string.digits + string.punctuation
    result_3= dataSampling(str, str_ex, 1000, 20)
    print('随机生成1000个字符串长度为20的字符串:')
    print(result_3)
    print('筛选其中含有‘at’或者‘no’的字符串:')
    print(dataScreening(result_3, 'at', 'no'))


apply()
