"""
Author: Bill Hao
Purpose: Generate random data set
Created: 6/20/2020

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
    :return: random data

    '''
    try:
        if dataType is int:
            cnt = 1
            it = iter(dataRange)
            low = next(it)
            high = next(it)
            while cnt <= num:
                rData = random.randint(low, high)
                cnt += 1
                yield rData
        elif dataType is float:
            cnt = 1
            it = iter(dataRange)
            low = next(it)
            high = next(it)
            while cnt <= num:
                rData = random.uniform(low, high)
                cnt += 1
                yield rData
        elif dataType is str:
            cnt = 1
            while cnt <= num:
                rData = ''.join(random.sample(dataRange, strlen))
                cnt += 1
                yield rData
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
    

def dataScreening(data, *condition):
    '''
    :Description:Screen data by condition
    :param dataSet: data ready to be screened
    :param condition: a series data that used to screen data, 
                      if dataSet element type is int or float, only the first two number can work
                      if dataSet element type is str, condition is string, 
                      it screeing the str in dataSet that has a substring equal to condition
    :return: if data in condition, return true else return false

    '''
    try:
        cond = iter(condition)
        if type(data) is int or type(data) is float:
            low = next(cond)
            high = next(cond)
            if low > high:
                raise ValueError('dataRange need lower limit first')
            if low <= data <= high:
                return True
            return False
        elif type(data) is str:
            substr = next(cond)
            if substr in data:
                return True
            return False
        else:
            return False
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
    gen1 = generateRandomDataSet(int, [1, 100], 50)
    for data in gen1:  # iterate the gen1
        isIn = dataScreening(data, 30, 40) # screen
        if isIn:
            print(str(data) + ' ', end="")
    print("\n")
    gen2 = generateRandomDataSet(float, [1, 100], 50)
    for data in gen2:
        isIn = dataScreening(data, 30, 40)  # screen
        if isIn:
            print(str(data) + ' ', end="")
    print("\n")
    gen3 = generateRandomDataSet(str, 'abscsdrfwdsjf', 50)
    for data in gen3:
        isIn = dataScreening(data, 'bw') # screen
        if isIn:
            print(str(data) + ' ', end="")
    print("\n")

if __name__ == '__main__':
    main()
