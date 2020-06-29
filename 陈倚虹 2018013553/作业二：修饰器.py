# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Author: YH.Chen
    Purpose: Generate random data set.
    Created: 30/5/2020
"""

import random
import string


def data_sampling(func):
    def wrapper(data_type, data_range, data_num, *condition, length=8):
        """
        :Description: Generate a given condition random data set.
        :param data_type: Specify the type of the data set.
        :param data_range: Specify the range of the data set.
        :param data_num: Specify the number of the data set.
        :param condition: conditions for screening
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
                # 生成随机浮点数
                elif data_type is float:
                    it = iter(data_range)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
                # 生成随机字符串
                elif data_type is str:
                    item = ''.join(random.SystemRandom().choice(data_range) for _ in range(length))
                    result.add(item)
                else:
                    pass
        except TypeError:
            print("There is TypeError occurred in dataSampling")
        except MemoryError:
            print("There is MemoryError occurred in dataSampling")
        except Exception as e:
            print(str(e))
            print("This Error occurred in dataSampling")
        else:
            print("Sampling:", result)
            return func(result, *condition)
        finally:
            print('-----------------------------------------')
    return wrapper


@data_sampling
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
        print("Screening:", result)
    finally:
        print("dataScreening has completed.")


def apply():
    # 调用data_screening函数对生成的指定随机数或随机字符串筛选

    data_screening(int, (1, 100), 1000, 20, 50, 'at')
    data_screening(float, (1,100), 1000, 20, 50, 'at')
    data_screening(str, string.ascii_letters + string.digits, 1000, 'a', 'ab')


# 测试函数
if __name__ == '__main__':
    apply()
