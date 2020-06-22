"""
  Author:  jianxi.li
  Purpose: homework1:采用函数封装实现至少三种类型的随机数生成，以及随机数筛选.
  Created: 26/5/2020
"""
import string
import random
class exception1(Exception):
    def __init__(self, object):
        self.object = object
class exception2(Exception):
    def __init__(self, object1, object2):
        self.object1 = object1
        self.object2 = object2
def datasampling( type,datarangement, quantity, strlen=6):
    try:
        if quantity > 10000:
            raise OverflowError("too much datas：", quantity)
        result = list()
        if type is int:
            for i in range(0, quantity):
                options = iter(datarangement)
                item = random.randint(next(options), next(options))
                result.append(item)
        elif type is float:
            for i in range(0, quantity):
                options = iter(datarangement)
                item = random.uniform(next(options), next(options))
                result.append(item)
        elif type is str:
            for i in range(0, quantity):
                item = ''.join(random.SystemRandom().choice(datarangement) for _ in range(strlen))
                result.append(item)
        else:
            raise exception1(type)
        return result
    except exception1 as e:
        print("data type error", e.object)
    except StopIteration:
        print("can not be iterated")
    finally:
        print("results 1：")
def dataScreening(datafile, *ans):
    try:
        result = list()
        for i in datafile:
            if type(i) == type(ans[0]):
                if isinstance(i, int):
                    if i >= ans[0] and i <= ans[1]:
                        result.append(i)
                elif isinstance(i, float):
                    if i >= ans[0] and i <= ans[1]:
                        result.append(i)
                elif isinstance(i, str):
                    flag = 1
                    for x in i:
                        if x not in ans[0]:
                            flag = 0
                    if flag:
                        result.append(i)
                else:
                    raise exception1(type(i))
            else:
                raise exception2(type(i), type(ans[0]))
        return result
    except exception1 as e:
        print("doesn't support", e.object)
    except exception2 as e:
        print("The data type does not match the filter type", e.object1, e.object2)
    except Exception as e:
        print("unknown error")
    finally:
        print("results 2:")
def check():

    output1 = datasampling(int, (1, 200), 100)
    print(output1)
    output1 = dataScreening(output1, 10, 120)
    print(output1)
    output2 = datasampling(float, (1, 200), 150)
    print(output2)
    output2 = dataScreening(output2, 12.0, 150.0)
    print(output2)
    output3 = datasampling(str, string.ascii_letters + string.digits, 200, 10)
    print(output3)
    output3 = dataScreening(output3, string.ascii_letters)
    print(output3)
check()
