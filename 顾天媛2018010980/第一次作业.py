# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: Generate random data set.
  Created: 18/4/2020
"""

import random
import string

def create_set(datatype, datarange, num, strlen=8):
    old_set = set()
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                old_set.add(item)
                continue

        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                old_set.add(item)
                continue

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                old_set.add(item)
                continue

        else:
            print('请输入datatype:int、float、str!')
        return old_set
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
    try:
        for x in old_set:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_set.add(x)
                continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_set.add(x)
                continue

            elif datatype is str:
                if x.find(datarange) != -1:
                    new_set.add(x)
                continue
        print(new_set)
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