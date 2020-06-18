"""
    Author: GQ.Xu
    Purpose:Generate random data set
    Creat:15/6/2020
"""

import random
import string
import traceback
from iserror import IsError as ie
from error import DatatypeError, DatarangeError, NumError, StrlenError, RangeError


def DataError(datatype, datarange, num, strlen):
    '''
    dataSampling函数的异常生成函数
    :param datatype:Type of random data
    :param datarange:
    :param num:Random number
    :param strlen:length of string
    :return: a data set
    '''
    if ie('Type', datatype, (int, str, float)).ErrorSelection():
        raise DatatypeError(datatype)
    if ie('Iter', datarange).ErrorSelection():
        raise DatarangeError(datarange)
    if ie('Range', datarange).ErrorSelection():
        raise RangeError
    if type(num) is not int:
        raise NumError
    if type(strlen) is not int:
        raise StrlenError


def dataSampling(datatype, datarange, num, strlen=8):
    '''

    :param datatype:Type of random data
    :param datarange:range of data
    :param num:Random number
    :param strlen:length of string
    :return: a data set
    '''
    try:
        DataError(datatype, datarange, num, strlen)
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.choice(datarange) for _ in range(strlen))
                yield item
        else:
            pass
    except DatatypeError as e:
        print("Type", e.datatype, "is not include")
    except DatarangeError as e:
        print("Datarange can't be iterated.   Datarange:", e.datarange)
    except NumError:
        print("num'type must be 'int'")
    except StrlenError:
        print("strlen'type must be 'int'")
    except ValueError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
        traceback.print_exc()


def dataScreening(data, datatype, *condition):
    '''

    :param data:Iterative random data type
    :param condition:
    if type of the values in data is 'int' or 'float':
        condition[0] uses '[]','()','(]' and '[)' to represent the opening or closing condition of the section
        condition[1] is a tuple which represents the upper and lower boundaries of data
    if type of the values in data is 'str':
        conditions means substrings of string
    :return:Filter results
    '''
    try:
        if ie('Iter', data).ErrorSelection():
            raise DatarangeError(data)
        if datatype is int or datatype is float:
            section = condition[0]
            datarange = condition[1]
            for value in data:
                if section == '[]' and value >= datarange[0] and value <= datarange[1]:
                    yield value
                if section == '()' and value > datarange[0] and value < datarange[1]:
                    yield value
                if section == '(]' and value > datarange[0] and value <= datarange[1]:
                    yield value
                if section == '[)' and value >= datarange[0] and value < datarange[1]:
                    yield value
        if datatype is str:
            substrings = condition
            for value in data:
                for substring in substrings:
                    if substring in value:
                        yield value
    except DatarangeError as e:
        print("Type", e.datatype, "is not include")
    except ValueError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
        traceback.print_exc()


#1.生成50个1~1000内的随机整数，并筛选其中大于200小于等于600的数
print('1.利用生成器生成50个1~1000内的随机整数,并筛选其中大于200小于等于600的数：')
result1_1 = set()
result1_2 = set()
for x in dataSampling(int, (1, 1000), 50):
    result1_1.add(x)
print(result1_1)
for y in dataScreening(result1_1, int, '(]', (200, 600)):
    result1_2.add(y)
print(result1_2)
print('\n')
#2.生成100个1~100内的随机浮点数，并筛选其中大于20小于等于60的数
print('2.利用生成器生成100个1~100内的随机浮点数，并筛选其中大于20小于等于60的数：')
result2_1 = set()
result2_2 = set()
for x in dataSampling(float, (1, 100), 100):
    result2_1.add(x)
print(result2_1)
for y in dataScreening(result2_1, float, '(]', (20, 60)):
    result2_2.add(y)
print(result2_2)
print('\n')
#3.利用生成器生成100个随机字母和数字组成的字符串，并筛选出其中包括a,b,c字符的字符串
print('3.生成100个随机字母和数字组成的字符串，并筛选出其中包括a,b,c字符的字符串：')
result3_1 = set()
result3_2 = set()
for x in dataSampling(str, string.ascii_letters + string.digits, 100):
    result3_1.add(x)
print(result3_1)
for y in dataScreening(result3_1, str, 'a', 'b', 'c'):
    result3_2.add(y)
print(result3_2)
