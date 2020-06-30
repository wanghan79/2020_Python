##!/usr/bin/python3
"""
  Author:  RuiJia.Cao
  Purpose: Generate random data set by decorator.
  Created: 16/6/2020
"""
import random
import string

def DataSampling(datatype, datarange, num, strlen=8):
    '''
    :param datatype: basic data type including int float string
    :param datarange: iterable data set
    :param num: number of data
    :param strlen: string length
    :return: a data set
    '''
    try:
        result = set()
        if datatype is int:
            while True:
                it=iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                if len(result)>=num:
                    break
        elif datatype is float:
            while True:
               it = iter(datarange)
               item = random.uniform(next(it), next(it))
               result.add(item)
               if len(result) >= num:
                    break
        elif datatype is str:
            while True:
               item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
               result.add(item)
               if len(result)>=num:
                   break
    except NameError:
        print("请在数据采样中输入基本数据类型:")
    except TypeError:
        print("请检查数据采样中的数据类型")
    except MemoryError:
        print("数据采样时内存中的数据过多")
    except:
        raise Exception
    else:
        return result


def DataScreening(data, *conditions):
    '''
    :param data: iterable data set
    :param conditions: variable-length argument
    :return: a data set
    '''
    try:
        result=set()
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it)<=item<=next(it):
                    result.add(item)

            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)

    except TypeError:
        print("请检查数据筛选中的数据类型!")
    except:
        raise Exception
    else:
        print("数据筛选结果!")
        print(result)
        print("请继续生成随机数据：")


def Apply():
    #整型
    print("\n")
    result_1= DataSampling(int,[0,200],100)
    DataScreening(result_1,20,60)

    #浮点型
    print("\n")
    result_2 = DataSampling(float,[50,100],100)
    DataScreening(result_2,60,70)

    #字符串型
    print("\n")
    result_3 = DataSampling(str, string.ascii_letters + string.digits, 2000, 15)
    DataScreening(result_3, 'az', 'azz', 'crj')

    print("\n")
    result_4 = DataSampling(int,55, 100)
    DataScreening(result_4,20,60)
    print("\n")
    result_5 = DataSampling(float, [50, 100],"crj")
    DataScreening(result_5, 60, 70)
    print("\n")
    result_6 = DataSampling(str,100, 2000,15)
    DataScreening(result_6, 'az','azz','crj')
    print("\n")

Apply()