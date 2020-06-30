"""
Author:JingMiao
Purpose:Generate random data set.
Create:20/6/2020
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
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                continue
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                continue
        else:
            pass
        return result
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
    result1=dataSampling(int,(1,10),3)
    print("Before Screening:")
    print(result1)
    screened_result1=dataScreening(result1,5,10)#筛选5-10的int元素
    print("After Screening:")
    print(screened_result1)

    print("\nfloat:")
    result2=dataSampling(float,(-2.0,10.0),10)
    print("Before Screening:")
    print(result2)
    screened_result2 = dataScreening(result2, 0.0, 5.0)  # 筛选>0的float
    print("After Screening:")
    print(screened_result2)

    print("\nstr:")
    result3=dataSampling(str,string.ascii_letters+string.digits,5,2)
    print("Before Screening:")
    print(result3)
    screened_result3 = dataScreening(result3, 'jm','1','2','3')  # 筛选含有jm或1,2,3的str
    print("After Screening:")
    print(screened_result3)


apply()
