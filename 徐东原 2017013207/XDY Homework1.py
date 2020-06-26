##!/usr/bin/python3
"""
  Author: DY.Xu
  Purpose: Data generation and Screening
  Created: 4/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen = 12):
    '''
            :Description: Generate a given condition random data set.
            :param datatype: basic data type (int  float  str)
            :param datarange: iterable data set
            :param num: number of data
            :param strlen:string length
            :return a data set
        '''
    try:
        if datatype is int:
            result = []
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.append(item)
            return result
        elif datatype is float:
            result = []
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
            return result
        elif datatype is str:
            result = []
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
            return result
        else:
            raise NameError
    except TypeError:
        print("Please enter the iterable data range in dataSampling")
    except NameError:
        print("Please enter the correct data type in dataSampling")
    except Exception:
        print("There are other errors in dataSampling")
def dataScreening(data, *args):
    '''
                :Description: Screen the data set
                :param data: An iterable data set
                :param args: Iterable ranges
                :return a data set
            '''
    try:
        result = []
        for item in data:
            for i in args:
                if type(i) is set or list or tuple:
                    try:
                        it = iter(i)
                        if item >= next(it) and item <= next(it):
                            result.append(item)
                            break
                    except StopIteration:
                        pass
                elif type(i) is str:
                    if i in item:
                        result.append(item)
                        break
                else:
                    raise NameError
    except NameError:
        print("Please enter the correct data type in dataScreening")
    except TypeError:
        print("Please enter the correct condition type in dataScreening")
    except Exception:
        print("There are other errors in dataScreening")
    finally:
        return result

def Apply():
    a1 = dataSampling(int, (0, 100), 30)
    b1 = dataScreening(a1, (0, 60))
    a2 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10, 6)
    b2 = dataScreening(a2, 'at', 's', 'c')
    a3 = dataSampling(float, (0, 100), 20)
    b3 = dataScreening(a3, (0, 50))
    print(a1)
    print(b1)
    print(a2)
    print(b2)
    print(a3)
    print(b3)
    print('\n')
    x1 = dataSampling(int, 100, 10) #TypeError in dataSampling
    x2 = dataSampling(set, (1, 100), 10) #NameError in dataSampling
    x3 = dataSampling(int, (1, 100), 10) #TypeError in dataScreening
    y3 = dataScreening(x3, 100)
    print(x3)
    print(y3)

Apply()