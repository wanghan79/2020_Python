"""
Author: Bill Hao
Purpose: Generate random data set
Created: 4/20/2020

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
        return rDataSet
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
        ele = iter(dataSet)
        cond = iter(condition)
        if type(next(ele)) is int or type(next(ele)) is float:
            low = next(cond)
            high = next(cond)
            if low > high:
                raise ValueError('dataRange need lower limit first')
            for data in dataSet:
                 if low <= data <= high:
                    filterRes.add(data)
        elif type(next(ele)) is str:
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
    set1 = generateRandomDataSet(int, [1, 100], 50)
    print(set1)
    filt1 = dataScreening(set1, 30, 40)
    print(filt1)
    set2 = generateRandomDataSet(float, [1, 100], 50)
    print(set2)
    filt2 = dataScreening(set2, 59.6, 72.8)
    print(filt2)
    set3 = generateRandomDataSet(str, 'abscsdrfwdsjf', 20)
    print(set3)
    filt3 = dataScreening(set3, 'bw')
    print(filt3)

if __name__ == '__main__':
    main()
