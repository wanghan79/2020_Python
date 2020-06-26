# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Generate random data set.
    Created: 21/6/2020
"""

import random
import string


def data_sampling(data_type, data_range, data_num, length=8):
    """
    :Description: Generate a given condition random data set.
    :param data_type: Specify the type of the data set.
    :param data_range: Specify the range of the data set.
    :param data_num: Specify the number of the data set.
    :param length: Specify the length of the elements of the data set if the type of element is string.
    :return: A set with specified data
    """
    result = set()
    print("数据集的类型为：", data_type)
    try:
        for index in range(1, data_num+1):
            # 生成随机整数
            if data_type is int:
                it = iter(data_range)
                item = random.randint(next(it), next(it))
                result.add(item)
                msg = yield item
            # 生成随机浮点数
            elif data_type is float:
                it = iter(data_range)
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield item
            # 生成随机字符串
            elif data_type is str:
                item = ''.join(random.SystemRandom().choice(data_range) for _ in range(length))
                result.add(item)
                yield item
            else:
                pass
    except TypeError:
        print("There is TypeError occurred in dataSampling")
    except MemoryError:
        print("There is MemoryError occurred in dataSampling")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataSampling")
    finally:
        print('-----------------------------------------')


def data_screening(data_set, *condition):
    """
    :Description: Filter data according to specified requirements.
    :param data_set: the sampling set send to be screening.
    :return: A set after screening according to our requirement.
    """

    result = set()

    try:
        for item in data_set:
            if (type(item) is int or type(item) is float) and len(condition) > 2:
                print("Warning: There are only two numbers needed for data filtering.The first two numbers are "
                      "used as condition ranges")
                i = iter(condition)
                if next(i) >= next(i):
                    print("Warning: The filtered set will be empty because the former is larger than the latter")
                else:
                    pass
                break
            else:
                break
        # 数据筛选
        for item in data_set:
            if type(item) is int or type(item) is float:
                num = iter(condition)
                if next(num) <= item <= next(num):
                    result.add(item)
            elif type(item) is str:
                for substring in condition:
                    if substring in item:
                        result.add(item)
            else:
                pass
    except TypeError:
        print("There is TypeError occurred in dataScreening")
    except MemoryError:
        print("There is MemoryError occurred in dataScreening")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataScreening")
    else:
        return result
    finally:
        print("dataScreening has completed.")


def apply():

    # 若数据集为整数集
    result = set()
    sample_int = data_sampling(int, (1, 100), 1000)
    while 1:
        try:
            result.add(next(sample_int))
        except StopIteration:
            break
    result_2 = data_screening(result, 50, 70)
    print("the original result is:", result)
    print("the New Result is:", result_2)
    print("===================================================\n")

    # 若数据集为浮点数集
    result = set()
    sample_float = data_sampling(float, (1, 100), 1000)
    while 1:
        try:
            result.add(next(sample_float))
        except StopIteration:
            break
    result_2 = data_screening(result, 50, 70)
    print("the original result is:", result)
    print("the New Result is:", result_2)
    print("===================================================\n")

    # 若数据集为字符集
    result = set()
    sample_str = data_sampling(str, string.ascii_letters + string.digits, 1000)
    while 1:
        try:
            result.add(next(sample_str))
        except StopIteration:
            break
    result_2 = data_screening(result, 'a', 'ab')
    print("the original result is:", result)
    print("the New Result is:", result_2)
    print("===================================================\n")


# 测试函数
if __name__ == '__main__':
    apply()
