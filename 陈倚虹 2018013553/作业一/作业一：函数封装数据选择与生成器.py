# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Generate random data set.
    Created: 14/4/2020
"""

import random
import string

result = set()


def data_sampling(data_type, data_range, data_num, length=8):
    """
    :Description: Generate a given condition random data set.
    :param data_type: Specify the type of the data set.
    :param data_range: Specify the range of the data set.
    :param data_num: Specify the number of the data set.
    :param length: Specify the length of the elements of the data set if the type of element is string.
    :return: A set with specified data
    """
    global result

    for index in range(1, data_num+1):
        # 生成随机整数
        if data_type is int:
            it = iter(data_range)
            item = random.randint(next(it),next(it))
            result.add(item)
            continue
        # 生成随机浮点数
        elif data_type is float:
            it = iter(data_range)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        # 生成随机字符串
        elif data_type is str:
            item = ''.join(random.SystemRandom().choice(data_range) for _ in range(length))
            result.add(item)
            continue
        else:
            continue

    return result


def data_screening(data_type, mini, maxi, substring):
    """
    :Description: Filter data according to specified requirements.
    :param maxi: the maximum of the requirement.
    :param mini: the minimum of the requirement.
    :param substring: the substring of requirement.
    :return: A set after screening according to our requirement.
    """

    global result
    # 对整数和浮点数集的数据筛选
    if data_type is int or data_type is float:
        for i in result:
            if mini <= i <= maxi:
                print(i)

    # 对字符串集合进行数据筛选
    for i in result:
        if isinstance(i, str):
            if i.find(substring) != -1:
                print(i)


def apply():
    global result
    data_range = list()
    data_type = input("请输入生成随机数的数据类型：")
    # 若数据类型为整型或浮点型，定义data_range的最大和最小值
    if data_type == 'int' or data_type == 'float':
        data_range = [1, 100]
    # 若数据类型为字符串，定义字符集
    elif data_type == 'str':
        data_range = string.ascii_letters + string.digits

    # 调用data_sampling函数生成指定随机数或随机字符串
    result = data_sampling(int, data_range, 100)

    # 打印输出随机数集或字符集
    for i in result:
        print(i)

    print("=================================")
    print("筛选后的数据如下")
    data_screening(int, 20, 50, 'at')


# 测试函数
if __name__ == '__main__':
    apply()
