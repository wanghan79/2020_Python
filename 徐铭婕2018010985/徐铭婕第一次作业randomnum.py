# encoding: utf-8
'''
Author :    xumingjie 
Purpose:    Generate random data set.
Created:    2020/6/15 20:42
'''
import random
import string
def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description: Generate a given condition random data set.
    :param datatype: The data type of the random value we want to get.
    :param datarange: The data range of the random value we want to get.
    :param num: The number of random values we want to get.
    :param strlen: If we want to get a random value of type string, this parameter is the length of the string.
    :return:data list
    '''
    try:
        result = list()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.append(item)
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
        else:
                pass
    except TypeError:
        print("Type Wrong!")
    except MemoryError:
        print("Memory Exception!")
    except ValueError:
        print("num Wrong!")
    return result



def dataScreening(data, *conditions):  # *args 可变参数，可输入n个条件
    """
    :Description: Dataset filtering.
    :param data:Datasets that need to be filtered.
    :param conditions:The conditions under which we screen
    :return:data set
    """
    result = set()
    # Screening
    try:
        for i in data:
            if type(i) is int or type(i) is float:
                it = iter(conditions)
                if next(it) <= i <= next(it):
                    result.add(i)
            elif type(i) is str:
                for tmp in conditions:
                    if tmp in i:
                        result.add(i)
    except TypeError:
        print("Type Wrong!")
    except MemoryError:
        print("Memory Exception!")
    return result


def apply():
    # int
    resultint = dataSampling(int, (1,100), 20)
    print("\n随机生成20个在1到100之间的随机数")
    print(resultint)
    screenint = dataScreening(resultint, 25, 75)
    print("\n筛选出在25到75范围内的随机数")
    print(screenint)

    #float
    resultfloat = dataSampling(float, [0.1, 99.9], 20)
    print("\n随机生成20个在0.1到99.99的随机浮点数")
    print(resultfloat)
    screenfloat = dataScreening(resultfloat, 33.3, 66.6)
    print("\n筛选出在33.3到66.6范围内的随机浮点数")
    print(screenfloat)

    #str
    resultstr = dataSampling(str, string.ascii_letters+string.digits, 20, 15)
    print("\n随机生成20个长度为15的字符串")
    print(resultstr)
    screenstr = dataScreening(resultstr, 'xv','py')
    print("\n筛选出含有“xv”或”py“的字符串")
    print(screenstr)

apply()
