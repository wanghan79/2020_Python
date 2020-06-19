"""
    Author:W
    Purpose: Use decorator to realize function
    Created:2020/5/14
"""
import random
import string
from collections.abc import Iterable


def dataSampling(dataType, dataRange, num, strlen=8):
    def dacorator(func):
        def wrapper(*args, **kwargs):
            result = set()
            try:
                if (isinstance(dataRange, Iterable) == "false"):
                    raise StopIteration
                while (len(result) < num):
                    # int type
                    if dataType == 'int':
                        it = iter(dataRange)
                        item = random.randint(next(it), next(it))
                        result.add(item)
                    # float type
                    elif dataType == 'float':
                        it = iter(dataRange)
                        item = random.uniform(next(it), next(it))
                        result.add(item)
                    # str type
                    elif dataType == 'str':
                        item = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + "@#!~") for _ in range(strlen))
                        result.add(item)
                    # Not supported type
                    else:
                        raise TypeError
            except TypeError:
                print("Error: Sorry, this type is not supported.")
            except StopIteration:
                print("Error: Cannot iterate.")
            except MemoryError:
                print("Error: Out of memory.")
            finally:
                return func(result, *args, **kwargs)
        return wrapper
    return dacorator


@dataSampling('int', [1, 100], 10)
def dataScreening(result, dataType, screenFactor):
    print("& Randomly generated set is : " + str(result))
    screenResult = set()
    # int type
    if dataType == 'int':
        for item in result:
            if item >= screenFactor[0] and item <= screenFactor[-1]:
                    screenResult.add(item)
    # float type
    elif dataType == 'float':
        for item in result:
            if item >= screenFactor[0] and item <= screenFactor[-1]:
                screenResult.add(item)
    # str type
    elif dataType == 'str':
        for item in result:
            if screenFactor in item:
                screenResult.add(item)
    print("& After screening, the set is :" + str(screenResult))
    print("----------------------------------------------------------------------")


dataScreening('int', [20, 50])




