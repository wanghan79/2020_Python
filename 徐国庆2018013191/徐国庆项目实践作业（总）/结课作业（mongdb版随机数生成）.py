"""
    Author: GQ.Xu
    Purpose:Generate random data set with mongodb
    Creat:16/6/2020
"""

import random
import string
import traceback
from iserror import IsError as ie
from error import DatatypeError, DatarangeError, NumError, StrlenError, RangeError
import pymongo



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
                yield {"datatype": 'int', "data": item}#返回一个字典类型的随机整数数据
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield {"datatype": 'float', "data": item}#返回一个字典类型的随机浮点数数据
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.choice(datarange) for _ in range(strlen))
                yield {"datatype": 'str', "data": item}#返回一个字典类型的随机字符串数据
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
                if section == '[]' and value.get('data') >= datarange[0] and value.get('data') <= datarange[1]:
                    yield value
                if section == '()' and value.get('data') > datarange[0] and value.get('data') < datarange[1]:
                    yield value
                if section == '(]' and value.get('data') > datarange[0] and value.get('data') <= datarange[1]:
                    yield value
                if section == '[)' and value.get('data') >= datarange[0] and value.get('data') < datarange[1]:
                    yield value
        if datatype is str:
            substrings = condition
            for value in data:
                for substring in substrings:
                    if substring in value.get('data'):
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

#建立mongodb数据库
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["runoobdb"]

mycol = mydb["sd"]

#将生成的数据添加到数据库中
for mydict in dataSampling(int, (1, 1000), 10):#利用生成器生成10个1~1000内的随机整数的数据
    mycol.insert_one(mydict)#
for mydict in dataSampling(float, (1, 100), 10):#利用生成器生成10个1~100内的随机浮点数的数据
    mycol.insert_one(mydict)
for mydict in dataSampling(str, string.ascii_letters + string.digits, 10):#利用生成器生成10随机字母和数字组成的字符串
    mycol.insert_one(mydict)
print('1.Mongodb数据库内容：')
for x in mycol.find():
    print(x)
print('\n')


#将数据库中的数据提取出来，并进行筛选
print('2.筛选后大于200，小于等于600的整数')
int_result = mycol.find({"datatype": 'int'})#将数据库中整数类型的数据提取出来
for y in dataScreening(int_result, int, '(]', (200, 600)):#筛选其中大于200小于等于600的整数数据
    print(y)

print('3.筛选后大于20，小于等于60的浮点数')
float_result = mycol.find({"datatype": 'float'})#将数据库中浮点数数类型的数据提取出来
for y in dataScreening(float_result, float, '(]', (20, 60)):#筛选其中大于20小于等于60的浮点数数据
    print(y)

print('4.筛选后包括a,b,c字符的字符串')
str_result = mycol.find({"datatype": 'str'})#将数据库中字符串类型的数据提取出来
for y in dataScreening(str_result,  str, 'a', 'b', 'c'):#筛选其中包括a,b,c字符的字符串数据
    print(y)