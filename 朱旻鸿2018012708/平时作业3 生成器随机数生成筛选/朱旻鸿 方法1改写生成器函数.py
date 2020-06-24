##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Generate random data set by generator.
  Created: 21/6/2020
"""
import random
import string

def DataSampling( ):
    '''
    generator function without parameters
    :yield: a random data
    '''
    try:
        msg = yield 1
        datatype=msg[0]
        datarange=msg[1]
        strlen=msg[2]
        if datatype is int:
            while True:
                it=iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            while True:
               it = iter(datarange)
               item = random.uniform(next(it), next(it))
               yield item
        elif datatype is str:
            while True:
               item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
               yield item
    except NameError:
        print("Please input basic data type in DataSampling")
    except TypeError:
        print("Please check data type in DataSampling")
    except MemoryError:
        print("Too much data out of memory in DataSampling")


def DataScreening(datatype, datarange, num, *conditions,strlen=15):
    '''

    :param datatype: basic data type including int float string
    :param datarange: iterable data set
    :param num: number of data
    :param conditions: variable length argument
    :param strlen: string length
    :return: a data set
    '''
    try:
        msg=[]
        msg.append(datatype)
        msg.append(datarange)
        msg.append(strlen)
        Randomdata=DataSampling()
        next(Randomdata)
        Randomdata.send(msg)

        result=set()
        for i in range(0,num):
            item=next(Randomdata)
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it)<=item<=next(it):
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

Apply()
