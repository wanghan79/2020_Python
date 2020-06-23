# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: decorator & random data set.
  Created: 18/6/2020
"""

# 平时作业3：使用生成器修改平时作业1中的随机数生成过程，并能够使用随机数筛选函数进行数据筛选；

import random
import string

def create_set(datatype, datarange, num, strlen=8):
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item

        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
        else:
            print('请输入datatype:int、float、str!')
    except OverflowError:
        print('数值运算超出最大限制')
    except TypeError:
        print('对类型无效的操作')
    except ValueError:
        print('ValueError 传入无效的参数')
    except Exception as e:
        print(e)
        print('你输入的参数有误')



def select_set(old_set, datatype, datarange):
    new_set = set()
    for i in old_set:
        new_set.add(i)
    print('old_set:\n',new_set)
    try:
        for x in new_set:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    print(x)
                continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    print(x)
                continue

            elif datatype is str:
                if x.find(datarange) != -1:
                    print(x)
                continue
    except OverflowError:
        print('数值运算超出最大限制')
    except TypeError:
        print('对类型无效的操作')
    except ValueError:
        print('ValueError 传入无效的参数')
    except Exception as e:
        print(e)
        print('你输入的参数有误')

def apply():
    base_str = string.ascii_letters + string.digits #   + string.punctuation
    old_set1 = create_set(int, (1,100), 10)
    select_set(old_set1, int, (2,50))
    old_set2 = create_set(float, (100, 200), 20)
    select_set(old_set2, float, (100, 500))
    old_set3 = create_set(str, base_str, 50,10)
    select_set(old_set3, str, 'a')

apply()