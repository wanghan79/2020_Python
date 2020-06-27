# python3
"""
  Author:  Tanlin
  Purpose: 作业三：使用生成器修改平时作业1中的随机数生成过程，并能够使用随机数筛选函数进行数据筛选；
  Created: 2020.6.22
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
                yield item  #yield代替return返回的是生成器
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield item
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                yield item
    except TypeError:
        print('The data type is error!')
    except ValueError:
        print("The data value is error!")
    except MemoryError:
        print("The data is too much!")
    print("The random data:\n", result)
    return result

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
    print("After filtered:")
    return result

def apply():  # 输出结果
    print("INT:")
    result1 = dataSampling(int, (1, 100), 5)
    item1 = dataScreening(result1, 20, 80)
    if item1:
        print(item1)
    else:
        print("Can't find!")
    print("FLOAT:")
    result2 = dataSampling(float, (1, 100), 5)
    item2 = dataScreening(result2, 20, 80)
    if item2:
        print(item2)
    else:
        print("Can't find!")
    print("STR:")
    result3 = dataSampling(str, string.ascii_letters + string.digits + string.printable, 5)
    item3 = dataScreening(result3,"T")
    if item3:
        print(item3)
    else:
        print("Can't find!")

apply()