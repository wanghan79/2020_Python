##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Generate random data set.
  Created: 3/5/2020
"""
import random
import string

def DataSampling(datatype, datarange, num, strlen=10):
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
        print("Please input basic data type in DataSampling")
    except TypeError:
        print("Please enter the correct data type in DataSampling")
    except MemoryError:
        print("Too much data out of memory in DataSampling")
    except:
        raise Exception
    else:
        return result
    finally:
        print("Welcome to continue generating data in DataSampling")

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
        print("Please enter the correct data type in DataScreening")
    except:
        raise Exception
    else:
        return result
    finally:
        print("Welcome to continue screening data in DataScreening")

def Apply():
    result1= DataSampling(int,[0,200],100)
    print(DataScreening(result1,20,50))
    result2 = DataSampling(int,55, 100)   #Exception occurred 55 is not iterable
    print(DataScreening(result2,20,50))
    result3=DataSampling(float,[0,100],100)
    print(DataScreening(result3,60,70))
    result4 = DataSampling(float, [50, 100],"hhh") #Exception occurred "hhh" is not correct type
    print(DataScreening(result4, 60, 70))
    result5= DataSampling(str,string.ascii_letters+string.digits,2000,15)
    print(DataScreening(result5,'at','att','attt'))
    result6 = DataSampling(str,100, 2000,15)   #Exception occurred 100 is not correct type
    print(DataScreening(result6, 'at','att','attt'))

Apply()











