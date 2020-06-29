##!/usr/bin/python3
"""
  Author: DY.Xu
  Purpose: Generation
  Created: 6/6/2020
"""
import random,string
from functools import wraps

def Wrapper(func):
    @wraps(func)
    def dataSampling(datatype, datarange, num, *args, strlen=12):
        '''
                :Description: Generate a given condition random data set.
                :param datatype: basic data type (int  float  str)
                :param datarange: iterable data set
                :param num: number of data
                :param strlen:string length
                :param *args:conditions
                :return func
            '''
        try:
            result = []
            if datatype is int:
                for i in range(num):
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.append(item)
            elif datatype is float:
                for i in range(num):
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.append(item)
            elif datatype is str:
                for i in range(num):
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.append(item)
            else:
                raise NameError

        except TypeError:
            print("Please enter the iterable data range in dataSampling")
        except NameError:
            print("Please enter the correct data type in dataSampling")
        except Exception:
            print("There are other errors in dataSampling")
        else:
            return func(result, *args)
    return dataSampling

@Wrapper
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
                elif type(i) is type("1"):
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
    result1 = dataScreening(int, (1, 100), 30, (0, 60))
    result2 = dataScreening(float, (1, 100), 20, (0, 50))
    result3 = dataScreening(str, string.ascii_letters + string.digits + "@#$!", 30, 'a', 'at')
    print("type:int range:(0, 60)\n", result1)
    print("type:float range:(0, 50)\n", result2)
    print("type:string range:'a' 'at'\n", result3)

if __name__ == '__main__':
    Apply()