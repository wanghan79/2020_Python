##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Generate random data set by generator.
  Created: 21/6/2020
"""
import random
import string

class DataSampling(object):
    def __init__(self,datatype, datarange,num,strlen):
        '''
        :param datatype: basic data type including int float string
        :param datarange: iterable data set
        :param num: number of data
        :param strlen: string length
        '''
        self.datatype=datatype
        self.datarange=datarange
        self.num=num
        self.strlen=strlen
    def __iter__(self):
        length = 0
        if self.datatype is int:
            while length < self.num:
                it = iter(self.datarange)
                item = random.randint(next(it), next(it))
                length += 1
                yield item
        elif self.datatype is float:
            while length < self.num:
                it = iter(self.datarange)
                item = random.uniform(next(it), next(it))
                length += 1
                yield item
        elif self.datatype is str:
            while length < self.num:
                item = ''.join(random.SystemRandom().choice(self.datarange) for _ in range(self.strlen))
                length += 1
                yield item

def DataScreening(datatype, datarange, num, *conditions,strlen=15):
    '''
    :param datatype: basic data type including int float string
    :param datarange: iterable data set
    :param num: number of data
    :param conditions: variable-length argument
    :param strlen: string length
    :return: a data set
    '''
    try:
        result = set()
        for item in DataSampling(datatype, datarange, num, strlen):
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it) <= item <= next(it):
                    result.add(item)
            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)

    except NameError:
        print("Please input basic data type in DataScreening")
    except TypeError:
        print("Please check data type in DataScreening")
    except MemoryError:
        print("Too much data out of memory in DataScreening")
    except:
        raise Exception
    else:
        print("The result of data screening")
        print(result)
        print("Welcome to continue generating random data ")

def Apply():
    print("********************************************")
    DataScreening(int, [0, 200], 100, 60, 90)
    print("********************************************")
    DataScreening(float, [0, 100], 100, 60, 70)
    print("*********************************************")
    DataScreening(str, string.ascii_letters + string.digits, 2000, 'at', 'att', 'attt')
    print("**********************************************")
    DataScreening(int, 200, 100, 20, 50)  # Exception occurred 200 is not iterable
    print("**********************************************")

Apply()