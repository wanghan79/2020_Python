# -*- coding: utf-8 -*-
import random

import string


def gen_random(dtype, num, datatange=(10, 1000), str_num=8):
    """
    随机数生成
    :return:
    """
    try:
        start, end = datatange
        if dtype is int:
            return (random.choice(range(start, end + 1)) for _ in range(num))

        elif dtype is float:
            return (random.uniform(start, end + 1) for _ in range(num))

        elif dtype is str:
            return (''.join((random.choice(string.ascii_letters) for _ in range(str_num))) for x in range(num))

        else:
            print('请参入int、float、str类型的数据')
    except:
        print('传入参数错误')


def random_search(dtype, result, *datarange):
    """
    随机数搜索
    :return:
    """
    try:
        start, end = datarange
        if dtype is int:
            return [x for x in result if start <= x <= end]

        elif dtype is float:
            return [x for x in result if start <= x <= end]

        elif dtype is str:
            return [x for x in result if x.find(start) > -1 or x.find(end) > -1]

        else:
            print('请参入int、float、str类型的数据')
    except:
        print('传入参数错误')


result1 = gen_random(str, 10)
print(random_search(str, result1, 'a', 'at'))

result2 = gen_random(int, 10)
print(random_search(int, result2, 200, 500))

result3 = gen_random(float, 10)
print(random_search(float, result3, 100, 600))
