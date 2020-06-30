"""
  Author:  heyue.zheng
  Purpose: Generate random data set.
  Created: 21/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num):
    '''
    :Description: Generate a given condition random data set.
    :param datatype: dddd
    :param datarange: iterable data set
    :param num: number
    :return: a dataset
    '''
    try:
        result = set()
        for index in range(0, num):
            if datatype is int:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
            elif datatype is float:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                continue
            elif datatype is str:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(8))
                result.add(item)
                continue
            else:
                continue
        return result
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")


def dataScreening(data, *args):
    try:
        result = set()
        for value in data:
            if type(value) is int:
                if value in args:
                    result.add(value)
                    continue
            elif type(value) is float:
                if value in args:
                    result.add(value)
                    continue
            elif type(value) is str:
                for arg in args:
                    if arg in value:
                        result.add(value)
                        continue
            else:
                continue
        return result
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")


def apply():
    result1 = dataSampling(int, (0, 1000), 100)
    print(result1)
    result_1 = dataScreening(result1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
    print(result_1)

    result2 = dataSampling(str, string.ascii_letters+string.digits+"@#$!", 100)
    print(result2)
    result_2 = dataScreening(result2, 'a', 'x', '5')
    print(result_2)

    result3 = dataSampling(float, (1.0, 10.0), 100)
    print(result3)
    result_3 = dataScreening(result3, 1.025678990912345, 2.2222234567890987, 3.456789098754123)
    print(result_3)

apply()
