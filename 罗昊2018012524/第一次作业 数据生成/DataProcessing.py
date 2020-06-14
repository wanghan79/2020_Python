##!/usr/bin/python3
"""
  Author:  LuoHao
  Purpose: Data generation and Screening
  Created: 1/5/2020
"""
class TypeException(Exception):
    pass

class NumException(Exception):
    pass

class NoneException(Exception):
    pass

import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    '''
        :Description: Generate a given condition random data set.
        :param datatype: int or float or str
        :param datarange: iterable data set
        :param num: number
        :param strlen:string length
        :return: a dataset
    '''
    try:
        result = set()
        if num < 0:
            raise NumException
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        else:
            raise TypeException
        return result
    except TypeException:
        print("Please enter the correct data type in dataSampling(int or float or str)")
    except TypeError:
        print("Please enter an iterable range of data")
    except NumException:
        print("num must >= 0")

def dataScreening(data, *args):
    '''
            :Description: Generate a given condition random data set.
            :param data: a dataset
            :param args: conditions
            :return: a dataset
        '''
    try:
        result = set()
        if data is None:
            raise NoneException
        else:
            for item in data:
                for i in args:
                    if type(i) is set or list or tuple:
                        try:
                            it = iter(i)
                            if item >= next(it) and item <= next(it):
                                result.add(item)
                                break
                        except StopIteration:
                            pass
                    elif type(i) is str:
                        if i in item:
                            result.add(item)
                            break
        return result
    except NoneException:
        print("Error in dataSampling")
    except TypeError:
        print("Please enter the correct data conditions in dataScreening")

def apply():
    "To test the program"
    data1 = dataSampling(int, (1, 100), 12)
    data2 = dataSampling(float, (1, 100), 12)
    data3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 12, 5)

    test1 = dataScreening(data1, (0, 10), (50, 100))
    test2 = dataScreening(data2, (0, 20), (40, 70))
    test3 = dataScreening(data3, 'a', 'c', 'at')

    if data1 is not None:
        print(data1)
    if test1 is not None:
        print(test1)

    if data2 is not None:
        print(data2)
    if test2 is not None:
        print(test2)

    if data3 is not None:
        print(data3)
    if test3 is not None:
        print(test3)

def applyError():
    "To test the wrong program"
    data4 = dataSampling(list, (1, 100), 12)
    test4 = dataScreening(data4, (0, 10), (50, 100))

    if data4 is not None:
        print(data4)
    if test4 is not None:
        print(test4)

    data5 = dataSampling(int, (1, 100), 12)
    test5 = dataScreening(data5, 70, 90, 20, 50)

    if data5 is not None:
        print(data5)
    if test5 is not None:
        print(test5)

apply()
applyError()