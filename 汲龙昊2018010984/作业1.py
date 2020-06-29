"""
  Author:JLH2018010984
  Created: 2020/6/25
"""


import random
import string

def print_line():
    print("*" * 60)
print_line()

def dataSampling(datatype, datarange, num, strlen=8):
    '''
        :Description: Generate a given condition random data set.
        :param datatype: The type of data which include int float and string
        :param datarange: iterable data set
        :param num: Input parameters that means The final result of the number of elements
        :param strlen:The length of input strings
        :return: a dataset
    '''
    try:
        result = set()
        if (datatype is int):
            while len(result) < num:    #防止重复
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                result.add(item)
        elif (datatype is float):
            while len(result) < num:
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                result.add(item)
        elif (datatype is str):
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
    except ValueError:
        print("参数是无效的")
    except TypeError:
        print("发生类型错误")
    except MemoryError:
        print("发生内存错误")
    except NameError:
        print("初始化参数名称")
    else:
        return result

def dataScreening(data,*args):
    try:
        resultT = set()
        for i in data:
            if (type(i) is int):
                T = iter(args)
                if(next(T) <= i and next(T) >= i):
                    resultT.add(i)
            elif (type(i) is float):
                    T = iter(args)
                    if (next(T) <= i and next(T) >= i):
                        resultT.add(i)
            elif (type(i) is str):
                for cstr in args:
                    if(cstr in i):
                        resultT.add(i)
    except ValueError:
        print("参数是无效的")
    except TypeError:
        print("发生类型错误")
    except MemoryError:
        print("发生内存错误")
    except NameError:
        print("初始化参数名称")
    else:
        return resultT

def apply():

    result1 = dataSampling(int, [0,101], 20)
    print(result1)
    Screening1 = dataScreening(result1,5,20)
    print(Screening1)

    result2 = dataSampling(float, [0, 101], 20)
    print(result2)
    Screening2 = dataScreening(result2,5,20)
    print(Screening2)

    result3 = dataSampling(str, string.ascii_letters + string.digits, 100,20)
    print(result3)
    Screening3 = dataScreening(result3,'a')
    print(Screening3)
apply()

print_line()