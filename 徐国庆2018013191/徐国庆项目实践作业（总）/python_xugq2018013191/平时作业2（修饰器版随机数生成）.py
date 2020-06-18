"""
    Author: GQ.Xu
    Purpose:Generate random data set with decorator
    Creat:10/6/2020
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
        result = set()
        DataError(datatype, datarange, num, strlen)
        if datatype is int:
            while len(result) != num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) != num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) != num:
                item = ''.join(random.choice(datarange) for _ in range(strlen))
                result.add(item)
        else:
            pass

        def deco(func):
            '''
            生成修饰器
            '''
            def wrapper(*args, **kwargs):
                return func(result, *args, **kwargs)
            return wrapper
        return deco

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


@dataSampling(int, (1, 1000), 50)#运用修饰器生成50个1~1000内的随机整数再进行筛选
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
        result = set()
        if datatype is int or datatype is float:
            section = condition[0]
            datarange = condition[1]
            for value in data:
                if section == '[]' and value >= datarange[0] and value <= datarange[1]:
                    result.add(value)
                if section == '()' and value > datarange[0] and value < datarange[1]:
                    result.add(value)
                if section == '(]' and value > datarange[0] and value <= datarange[1]:
                    result.add(value)
                if section == '[)' and value >= datarange[0] and value < datarange[1]:
                    result.add(value)
        if datatype is str:
            substrings = condition
            for value in data:
                for substring in substrings:
                    if substring in value:
                        result.add(value)
        return result
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

#利用随机生成数修饰器生成50个1~1000内的随机整数，并对其中大于200小于等于600的数进行筛选
print('利用随机生成数修饰器生成50个1~1000内的随机整数，并对其中大于200小于等于600的数进行筛选')
result = dataScreening(int, '(]', (20, 60))
print(result)