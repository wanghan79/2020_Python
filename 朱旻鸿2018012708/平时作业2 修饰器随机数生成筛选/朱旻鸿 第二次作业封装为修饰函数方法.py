##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Generate random data set by decorator.
  Created: 17/5/2020
"""
import random
import string

def DataSampling(func):
    def wrapper(datatype, datarange, num, *conditions,strlen=15):
        '''
        :param datatype: basic data type including int float string
        :param datarange: iterable data set
        :param num: number of data
        :param conditions: variable-length argument
        :param strlen: string length
        :return: a function
        '''
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
            return func(result, *conditions)
        except NameError:
            print("Please check data type in DataSampling")
        except TypeError:
            print("Please check iterable data type in DataSampling")
        except MemoryError:
            print("Too much data out of memory in DataSampling")
        except:
            raise Exception
    return wrapper

@DataSampling
def DataScreening(data, *conditions):
    '''
    :param data: iterable data set
    :param conditions: variable-length argument
    :return: a data set
    '''
    try:
        result = set()
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it) <= item <= next(it):
                    result.add(item)
            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)
        print("The result of data screening")
        print(result)
        print("Welcome to continue generating random data by decorator")

    except TypeError:
        print("Please check the data type in DataScreening")
    except:
        raise Exception

print("********************************************")
DataScreening(int,[0,200],100,60,90)
print("********************************************")
DataScreening(float,[0,100],100,60,70)
print("*********************************************")
DataScreening(str,string.ascii_letters+string.digits,2000,'at','att','attt')
print("**********************************************")
DataScreening(int,200,100,20,50)    #Exception occurred 200 is not iterable
print("**********************************************")