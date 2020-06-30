##!/usr/bin/python3
"""
  Author:  Jiaza.Xin
  Purpose: Generate random data set.Change to a yield.
  Created: 25/6/2020
"""
import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description: Generate a given condition random data set.As a yield, returns an iterable object
    :param datatype: int,flout,str
    :param datarange: iterable data set,len(datarange) == 2
    :param num: number
    :param strlen:length of string
    :return: a dataset
    '''
    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item
            continue
        else:
            continue


def dataScreening(data, datatype, *range):
    '''
    :Description:Data filtering
    :param data:a set the result of dataSampling
    :param datatype:type,int,float,str
    :param range:condition for data filtering,len(range) <= 2 when type is int or float
    :return:a set
    '''
    try:
        if type(range) is int or float:
            if len(range) > 2:
                print("TypeError:incorrect filter condition for input")
            elif len(range) == 1:
                print("Warning:the filter result is greater than the given condition")
        # Screening---------------------------------------------

            if datatype is int or float:
                if len(range) == 2:
                    a, b = range
                    result = {x for x in data if a <= x <= b}
                elif len(range) == 1:
                    a = range
                    result = {x for x in data if a <= x}
            elif datatype is str:
                st = iter(range)
                result = {x for x in data if next(st) in x}
    except TypeError:
        print("TypeError :wrong type parameter entered")
    except MemoryError:
        print("MemoryError:Memory overflow error (not fatal to Python interpreter)")
    except Exception as e:
        print(str(e))
        print("Error")
    else:
        return result


def apply():
    #--------------------------------------------------------------int
    result1 = dataSampling(int, (1, 100), 50)
    afresult1 = dataScreening(result1, int, 20, 40)  # ---after the screening
    print(afresult1)
    #--------------------------------------------------------------float
    result2 = dataSampling(float, (1, 100), 5)
    afresult2 = dataScreening(result2, float, 20, 40)  # ---after the screening
    print(afresult2)
    #--------------------------------------------------------------str
    result3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 200)
    afresult3 = dataScreening(result3, str, 'siywueiwwfbwwfb', 'd')  # ---after the screening
    print(afresult3)

apply()
