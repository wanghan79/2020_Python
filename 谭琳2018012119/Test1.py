# python3
"""
  Author:  Tanlin
  Purpose: 作业一：采用python函数封装实现至少三种类型的随机数生成，以及随机数筛选；
  Created: 2020.6.15
"""
import random
import string
def dataSampling(datatype, datarange, num, strlen=10):  # 生成
    try:
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
    except TypeError:
        print('The data type is error!')
    except ValueError:
        print("The data value is error!")
    except MemoryError:
        print("The data is too much!")
    except:
        raise Exception
    else:
        return result
    finally:
        print("Thanks!")

def dataScreening(data, *args):  # 筛选*args(可变参数)
    try:
        result = set()
        for index in data:
            if type(index) is int or type(index) is float:
                it = iter(args)
                if next(it) <= index <= next(it):
                    result.add(index)
            elif type(index) is str:
                for substr in args:
                    if substr in index:
                        result.add(index)
    except TypeError:
        print("The data type is error!")
    except ValueError:
        print("The data value is error!")
    except:
        raise Exception
    else:
        return result
    finally:
        print("Thanks!")

def apply():  # 输出结果
    print("INT:")
    result1 = dataSampling(int, (1, 100), 5)
    print(result1)
    item1 = dataScreening(result1, 20, 80)
    if item1:
        print(item1)
    else:
        print("Can't find!")
    print("FLOAT:")
    result2 = dataSampling(float, (1, 100), 5)
    print(result2)
    item2 = dataScreening(result2, 20, 80)
    if item2:
        print(item2)
    else:
        print("Can't find!")
    print("STR:")
    result3 = dataSampling(str, string.ascii_letters + string.digits + string.printable, 5)
    print(result3)
    item3 = dataScreening(result3,"T")
    if item3:
        print(item3)
    else:
        print("Can't find!")

apply()