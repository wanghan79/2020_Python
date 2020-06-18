# coding=utf-8
"""
  Author:  Jiang Eryu 姜尔彧 2018011766
  Purpose: Generate random data set with Decorator.
  Created: 18/6/2020
"""

import random
import string


def dataSampling(func):  # 修饰
    def Wrapper(datatype, datarange, num, *conditions):
        """
        :Description: Generate a given condition random data set.
        :param datatype:int/float/str
        :param datarange: iterable data set
        :param num: number
        :param conditions:variable-length argument
        :return: a function
        """
        result = []
        if datatype is int:
            print("\nint类型示例：")
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.append(item)
                continue
        elif datatype is float:
            print("\nfloat类型示例：")
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
                continue
        elif datatype is str:
            print("\n字符串类型示例：")
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(8))
                result.append(item)
                continue
        print("随机生成数："),
        print(result)
        return func(datatype, result, *conditions)  # 执行screen函数
    return Wrapper


@dataSampling
def dataScreen(datatype, result, *conditions):  # 被修饰
    """
    :Description: Screen a given condition random data set.
    :param datatype: int/float/str
    :param result: random dataset
    :param conditions: variable-length argument
    :return: a dataset
    """
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
    print("条件筛选数："),
    print(result_scr)
    print("@@姜尔彧2018011766")


dataScreen(int, (1, 1000), 10, 10, 500)
dataScreen(float, (1, 999.9), 10, 12.3, 500.8)
dataScreen(str, string.ascii_letters + string.digits + "@#$!", 10, 'a', 'at')



