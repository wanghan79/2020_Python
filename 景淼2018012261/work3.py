"""
Author:JingMiao
Purpose:Generate random data set.
Create:27/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description:Generate a given condition random data set.
    :param datatype: int/float/str/...
    :param datarange:iterable data set
    :param num:number
    :param strlen:length of str
    :return:a dataset
    '''
    try:
        if datatype is int:
            for index in range(0,num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
                continue
        elif datatype is float:
            for index in range(0,num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue
        elif datatype is str:
            for index in range(0,num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
        else:
            pass

    except TypeError:
        print("The dataType must be int,float,str!")
    except ValueError:
        print("The dataRange is error!")
    except OverflowError:
        print("num is too large!")


def dataScreening(data,*args):
    try:
        result = set()
        for index in data:
            if type(index) is int or type(index) is float:
                it = iter(args)
                if next(it) <= index <= next(it):
                    result.add(index)

            elif isinstance(index, str):
                for it in args:
                    if it in index:
                        result.add(index)
        return result

    except TypeError:
        print("The data type is error!")
    except ValueError:
        print("The data value is error!")



def apply():
    print("int:")
    print("Before Screening:")
    old_result1=set()
    result1=dataSampling(int,(1,10),3)
    it=iter(result1)
    for i in range(0,3):
        old_result1.add(next(it))
    print(old_result1)
    print("After Screening:")
    screened_result1=dataScreening(old_result1,5,10)#筛选5-10的int元素
    print(screened_result1)

    print("\nfloat:")
    print("Before Screening:")
    old_result2 = set()
    result2=dataSampling(float,(-2.0,10.0),10)
    it = iter(result2)
    for i in range(0, 10):
        old_result2.add(next(it))
    print(old_result2)
    print("After Screening:")
    screened_result2 = dataScreening(old_result2, 0.0, 5.0)  # 筛选0<x<5的float
    print(screened_result2)

    print("\nstr:")
    print("Before Screening:")
    old_result3 = set()
    result3=dataSampling(str,string.ascii_letters+string.digits,5,2)
    it = iter(result3)
    for i in range(0, 5):
        old_result3.add(next(it))
    print(old_result3)
    print("After Screening:")
    screened_result3 = dataScreening(old_result3, 'jm','1','2','3')  # 筛选含有jm或1,2,3的str
    print(screened_result3)


apply()
