"""
    Author:W
    Purpose: Random data generation and data filtering
    Created:2020/4/26
"""
import random
import string
from collections.abc import Iterable

'''
    程序均需自主输入，下面是输入样例
    1、int【int和float型相同，以int为例】
    (1) Please input data type: int 【int后不能有空格，会报类型异常】
    (2) Please input data range (!Separate by space): 1 100 【输入以空格隔开的两个数即可，如果只输入一个会报异常】
    (3) Please input data screen range (!Separate by space): 20 80 【输入要求同上】
    (4) Please input the number of item: 10 【输入数字即可】
    2、str
    (1) Please input data type: str
    (2) Please input the substring required (!No more than 8 digits): 4【输入一个需要的子串】
    (3) Please input the number of item: 10
'''


class getRandomData(object):

    def __init__(self, dataType, dataRange, screenFactor, num, strlen=8):
        '''
        :param dataType: The type of data
        :param dataRange: The range of generated random number
        :param num: The number of random numbers generated
        :param strlen: Length of string
        '''
        self.dataType = dataType
        self.dataRange = dataRange
        self.screenFactor = screenFactor
        self.num = num
        self.strlen = strlen

    def dataSampling(self, dataType, dataRange, num, strlen=8):
        '''
        purpose: randomly generated data
        :param dataRange: to creat a iterator
        :param num: the number of data
        :param strlen: the length of string
        :return: set()
        '''
        result = set()
        try:
            if num < 0:
                raise Exception("Error: the number of data shoule more than 0 !")
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
            print("Error: Sorry, this type is not supported !")
        except StopIteration:
            print("Error: Cannot iterate !")
        except MemoryError:
            print("Error: Out of memory !")
        except Exception:
            print(Exception)
        finally:
            return result

    def dataScreening(self, result, dataType, screenFactor, num):
        '''
        purpose: filter the  data
        :param result: Randomly generated data result
        :param screenFactor: screening condition
        :param num: the number of data
        :return: set()
        '''
        screenResult = set()
        try:
            if (isinstance(screenFactor, Iterable) == "false"):
                raise StopIteration
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
        except StopIteration:
            print("Error: Cannot iterate !")
        finally:
            return screenResult


def main():
    '''
    Using dataSampling and dataScreening to get data
    '''
    result = set()
    screenResult = set()

    dataType = input("(1) Please input data type: ")

    # only 'int' and 'float' need dataRange and screenRange
    if dataType != 'str':
        dataRange = list(map(int, input("(2) Please input data range (!Separate by space): ").strip().split()))
        screenFactor = list(
            map(int, input("(3) Please input data screen range (!Separate by space): ").strip().split()))
        num = input("(4) Please input the number of item: ")
        # create a new object
        data = getRandomData(dataType, dataRange, screenFactor, int(num))
        result = data.dataSampling(dataType, dataRange, int(num))
        screenResult = data.dataScreening(result, dataType, screenFactor, int(num))

    # 'str' needs a substring to find
    elif dataType == 'str':
        screenFactor = input("(2) Please input the substring required (!No more than 8 digits): ")
        num = input("(3) Please input the number of item: ")
        # create a new object
        string = getRandomData(dataType, " ", screenFactor, int(num))
        result = string.dataSampling(dataType, " ", int(num))
        screenResult = string.dataScreening(result, dataType, screenFactor, int(num))

    if len(result) == 0:
        print("& Randomly generated set is empty. ")
    else:
        print("& Randomly generated set is : " + str(result))
        print("& After screening, the set is :" + str(screenResult))


if __name__ == "__main__":
    main()
