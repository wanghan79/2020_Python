#!/usr/bin/env python
'''
@name    :   Random_screen
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/21         ZH.Peng    2018010275
'''
from functools import wraps
from Random_gener import Random_gener
class Random_screen(object):
    '''
    This class is a decorated class
    '''
    def __init__(self, datatype, datarange, num, strlen=8, *args):
        '''
        To initialize this class, you need to enter the data type,
        data range, number of data, data length (note that the
        default length is 8), and the data filter criteria
         
        Areas for improvement: self.dict = {int: tuple, float: tuple, str: str}
        '''
        self.datatype = datatype
        self.datarange = datarange
        self.num = num
        self.strlen = strlen
        self.args = args
        self.dict = {int: tuple, float: tuple, str: str}#To quickly return the type of container that stores various data

    def __call__(self, func, *args, **kwargs):
        '''
        Rewrite this function to make it a decorative class
        And then use @wraps # to keep function's own namespace
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = self.Screening(self.datatype, self.args)
            return func(res, *args, **kwargs)
        return wrapper


    def Screening(self, datatype, condition):
        '''
        'condition' will be a datarange or a series of strings.

        If 'condition' is a range,the function will chose the
        number of 'ans' in range to return.

        If 'condition' is series of strings,it will select
        string from 'ans' that contains these strings from 'condition'.

        At the end of the function, it will return the processing result in the form of set
        
        '''
        @Random_gener(self.datatype, self.datarange, self.num, self.strlen)
        def solve(ans):
            '''
            Use decorator to generate data before screen.
            '''

            '''
            'ans' will given by decorator Random_gener.
            'ans' could be set or string. 
            '''
            try:
                #print(condition)
                Random_gener.range_test(datatype, condition[0], self.dict[datatype])
                result = set()
                if datatype is int or datatype is float:
                    for item in ans:
                        fliter = iter(condition[0])
                        if next(fliter) <= item <= next(fliter):
                            result.add(item)
                elif datatype is str:
                    # strcdit = iter(condition)
                    for fliter in condition:
                        for item in ans:
                            if fliter in item:
                                result.add(item)
                return result
            except TypeError:
                print("There is TypeError occurred in dataScreening")
            except MemoryError:
                print("There is MemoryError occurred in dataScreening")
            except Exception as e:
                print(e)
                print("This Error occurred in dataScreening")
            finally:
                print("The data has been screened!")
        return solve()
