# coding=utf-8

"""
  Author:  Jiang Eryu 姜尔彧 2018011766
  Purpose: Generate random data set.
  Created: 12/6/2020
"""

import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    """
    :Description: Generate a given condition random data set.
    :param datatype:int/float/str
    :param datarange: iterable data set
    :param num: number
    :param strlen:8
    :return: a dataset
    """
    try:  # 异常处理
        result = []
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.append(item)
                continue
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
                continue
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
                continue
        return result
    except TypeError:
        print("? Type Error")
    except StopIteration:
        print("? Iteration Error")
    finally:
        print("——>"),


def dataScreening(datatype, result, *conditions):
    """
    :Description: Screen a given condition random data set.
    :param datatype: int/float/str
    :param result: random dataset
    :param datarange: iterable data set
    :return: a dataset
    """
    try:  # 异常处理
        result_scr = []
        if datatype is int:
            for i in result:
                it = iter(conditions)
                low = next(it)
                high = next(it)
                if low <= i <= high:
                    result_scr.append(i)
                continue
        elif datatype is float:
            for i in result:
                it = iter(conditions)
                low = next(it)
                mid = next(it)  # 增加一个中间值，进行迭代器数量异常处理检测（125行）
                high = next(it)
                if low <= i <= high:
                    result_scr.append(i)
                continue
        elif datatype is str:
            for i in result:
                for sub in i:
                    if sub in conditions:
                        result_scr.append(i)
                continue
        return result_scr
    except TypeError:
        print("? Type Error")
    except StopIteration:
        print("？Iteration Error")
    finally:
        print("——>"),


def apply():
    print("int类型示例：")
    print("随机生成数："),
    result = dataSampling(int, (1, 1000), 5)
    print(result)
    print("条件筛选数："),
    result_scr = dataScreening(int, result, 10, 500)  # 筛选（10，500）以内的整型随机数
    print(result_scr)
    print("@姜尔彧2018011766\n")

    print("float类型示例：")
    print("随机生成数："),
    result = dataSampling(float, (1.0, 1000.2), 5)
    print(result)
    print("条件筛选数："),
    result_scr = dataScreening(float, result, 10.8, 30, 500.9)  # 筛选(10.8, 500.9)以内的浮点随机数
    print(result_scr)
    print("@姜尔彧2018011766\n")

    print("字符串类型示例：")
    print("随机生成数："),
    result = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
    print(result)
    print("条件筛选数："),
    result_scr = dataScreening(str, result, 'a', 'at')  # 筛选带有'a'和'at'的字符串
    print(result_scr)
    print("@姜尔彧2018011766\n")

    print("数据类型异常示例：")
    print("随机生成数："),
    result = dataSampling(str, 100, 400, 10)  # 数据类型异常检测
    print(result)
    print("条件筛选数："),
    result_scr = dataScreening(str, result, 'a', 'at')
    print(result_scr)
    print("@姜尔彧2018011766\n")

    print("迭代器异常示例：")
    print("随机生成数："),
    result = dataSampling(float, (1.0, 1000.2), 5)
    print(result)
    print("条件筛选数："),
    result_scr = dataScreening(float, result, 10.8, 500.9)  # 迭代器数量异常检测
    print(result_scr)
    print("@姜尔彧2018011766\n")


apply()
