"""
Author: Bill Hao
Purpose: Make a generateRandomDataSet decorator to decorate dataScreening
Created: 5/20/2020

"""

import random

def generateRandomDataSet(dataType, dataRange, num, strlen = 6):
    '''
    :Description:Generate a given condition random data set
    :param dataType: Type of data that you want to generate
    :param dataRange: Range of data that you want to generate, 
                    if dataType == int or float, dataRange is a iterable data type 
                    and use the first two numbers as lower limit and upper limit
                    if dataType is str, dataRange is a string
    :param num: Number of data that you want to generate
    :param strlen: if datatype is str, strlen is length of every random string
    :return: random data set

    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            rDataSet = set()
            try:
                if dataType is int:
                    while(len(rDataSet) < num):
                        it = iter(dataRange)
                        rData = random.randint(next(it), next(it))
                        rDataSet.add(rData)
                elif dataType is float:
                    while(len(rDataSet) < num):
                        it = iter(dataRange)
                        rData = random.uniform(next(it), next(it))
                        rDataSet.add(rData)
                elif dataType is str:
                    while(len(rDataSet) < num):
                        rData = ''.join(random.sample(dataRange, strlen))
                        rDataSet.add(rData)
                return func(rDataSet, *args) #dataSet由此函数获取
            except TypeError:
                print('One of params is not this function needed type')
            except NameError:
                print("Cannot find variable in both global and local")
            except MemoryError:
                print('Params is out of memory')
            except ValueError:
                print('dataRange need lower limit first')
            except IndentationError:
                print('the number of dataRange you give that less than two numbers')
        return wrapper
    return decorator
    
@generateRandomDataSet(int, [1, 100], 50) # generate integer data
# @generateRandomDataSet(float, [1, 100], 50) # generate float data
# @generateRandomDataSet(str, 'abcdefghijklmnopqrstuvwxyz1234567890', 50, 10) # generate str data
def dataScreening(dataSet, *condition):
    '''
    :Description:Screen data by condition
    :param dataSet: a iterable data type that used to be screened
    :param condition: a series data that used to screen data, 
                      if dataSet element type is int or float, only the first two number can work
                      if dataSet element type is str, condition is string, 
                      it screeing the str in dataSet that has a substring equal to condition
    :return: data set that filter from param data

    '''
    filterRes = set()
    try:
        ele = next(iter(dataSet))
        cond = iter(condition)
        if type(ele) is int or type(ele) is float:
            low = next(cond)
            high = next(cond)
            if low > high:
                raise ValueError('dataRange need lower limit first')
            for data in dataSet:
                 if low <= data <= high:
                    filterRes.add(data)
        elif type(ele) is str:
            substr = next(cond)
            for data in dataSet:
                if substr in data:
                    filterRes.add(data)
        return filterRes
    except TypeError:
        print('One of params is not this function needed type')
    except NameError:
        print("Cannot find variable in both global and local")
    except MemoryError:
        print('Params is out of memory')
    except ValueError:
        print('dataRange need lower limit first')
    except IndentationError:
        print('the number of dataRange you give that less than two numbers')


def main():
    filterRes = dataScreening(20, 30) #dataSet is int or float
    # filterRes = dataScreening('im') # dataSet is string
    print(filterRes)


if __name__ == '__main__':
    main()
