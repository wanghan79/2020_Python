##!E/Python first-homework
"""
    Author:
        BowenCao
        2018013070

    Purpose:
        finally python class homework

    Introduction:
        Generate random data set and screening and use Mongodb

    Created: 20/6/2020
"""
import random
import string
from collections.abc import Iterable

import pymongo


def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description: Generate a given condition random data set
    :param datatype:The type of random data set must be a built-in type，
    :param datarange: The range of random array,it must be a iterable data set
    :param num: The length of random array
    :param strlen: If the data type is str, this parameter can specify the length of each string in the array
    :return:Random data set constructed
    '''

    try:
        #  The following code is used to verify the error and throw an exception
        if datatype is not int and datatype is not float and datatype is not str:
            raise Exception("datatype is not a built-in type")
        if not isinstance(datarange, Iterable):
            raise Exception("datarange is not a Iterable")
        if type(num) != int:
            raise Exception("num is not int")
        elif num > 10000:
            raise Exception("num is out of processable range")
        if type(strlen) != int:
            raise Exception("strlen is not int")

        if datatype is int:
            it = iter(datarange)
            index = 0
            min = next(it)
            max = next(it)
            while index < num:
                item = random.randint(min, max)
                yield {"datatype": 'int', "data": item}
                index += 1

        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                min = next(it)
                max = next(it)
                item = random.uniform(min, max)
                yield {"datatype": 'float', "data": item}
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield {"datatype": 'str', "data": item}

    except Exception as e:
        print("ERROR:", e)
    except TypeError:
        print("TypeError occurred in dataSampling")
    except MemoryError:
        print("MemoryError occurred in dataSampling")
    finally:
        pass


def dataScreening(data, datatype, *args):
    """
    :param data: Data set waiting to be screening
    :param datatype: Types to screen
    :param args: Variable parameters，the input rule is
                 1、When the datatype is int, you can enter an iterative array
                    containing two integer numbers in args to screening the random
                    numbers with the two numbers as the upper and lower bounds,
                    or you can enter an integer numbers to screening the random
                    numbers which can divided by the number
                 2、When the datatype is float，you can enter an iterative array
                    containing two integer numbers in args to screening the random
                    numbers with the two numbers as the upper and lower bounds
                 3、When the datatype is string，You can enter characters to screening
                    the random strings that contain them
    :return:Already screening dataset
    """
    try:
        if not isinstance(data, Iterable):  # 当data非可迭代时抛出异常
            raise Exception("dataset is not a Iterable")
        if datatype is "int":
            result = set()
            for item in data:
                if isinstance(item, int):
                    result.add(item)
            data = result
            for index in args:
                if isinstance(index, Iterable):
                    result = set()
                    it = iter(index)
                    min = next(it)
                    max = next(it)
                    for item in data:
                        if (item >= min) and (item <= max):
                            result.add(item)
                    data = result
                elif isinstance(index, int):
                    result = set()
                    for item in data:
                        if item % index == 0:
                            result.add(item)
                    data = result
            return result
        elif datatype is "float":
            result = set()
            for item in data:
                if isinstance(item, float):
                    result.add(item)
            data = result
            for index in args:
                if isinstance(index, Iterable):
                    result = set()
                    it = iter(index)
                    min = next(it)
                    max = next(it)
                    for item in data:
                        if (item >= min) and (item <= max):
                            result.add(item)
                    data = result
            return result
        elif datatype is "str":
            result = set()
            for item in data:
                if isinstance(item, str):
                    result.add(item)
            for index in args:
                if index is string.ascii_letters or string.digits or string.punctuation:
                    result = set()
                    for item in data:
                        if index in item:
                            result.add(item)
                    data = result
            return result
        else:
            raise Exception("args must be int or str or float or a number")  # 当args非可处理形式时抛出异常
    except Exception as e:
        print("ERROR:", e)
    except TypeError:
        print("TypeError occurred in dataSampling")
    except MemoryError:
        print("MemoryError occurred in dataSampling")
    finally:
        print("dataScreening Exception handling call complete")


def apply():
    # 建立mongodb数据库
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["datadb"]

    mycol_int = mydb["dataint"]  # 用于存储int型数据
    mycol_float = mydb["datafloat"]  # 用于存储float型数据
    mycol_str = mydb["datastr"]  # 用于存储str型数据

    print("#-------example1 Generate string data set--------")
    result = set()
    g = dataSampling(str, string.ascii_letters + string.digits + string.punctuation, 20)
    for index in range(0, 10):
        mycol_str.insert_one(next(g))  # 向数据库中插入生成的随机数
    for x in mycol_str.find():  # 从数据库中提取数据放入result数组中以备筛选
        result.add(x.get("data"))
    print("The dataset to be screening is:", result)
    result = dataScreening(result, "str", "6")
    print("Screen out the string containing character 6:", result)
    print("\n")

    print("#-------example2 Generate float data set--------")
    result = set()
    g = dataSampling(float, (0, 100), 100)
    for index in range(0, 10):
        mycol_float.insert_one(next(g))  # 向数据库中插入生成的随机数
    for x in mycol_float.find():  # 从数据库中提取数据放入result数组中以备筛选
        result.add(x.get("data"))
    print("The dataset to be screening is:", result)
    result = dataScreening(result, "float", (1.0, 50.0))
    print("Screen out all random numbers greater than 1 and less than 10:", result)
    print("\n")

    print("#-------example3 Generate int data set--------")
    result = set()
    g = dataSampling(int, (0, 10), 10)
    for index in range(0, 10):
        mycol_int.insert_one(next(g))  # 向数据库中插入生成的随机数
    for x in mycol_int.find():  # 从数据库中提取数据放入result数组中以备筛选
        result.add(x.get("data"))
    print("The dataset to be screening is:", result)
    result = dataScreening(result, "int", (1, 100), 5)
    print("Screen out all random numbers greater than 1 but less than 10 and divisible by 5:", result)


if __name__ == "__main__":
    apply()