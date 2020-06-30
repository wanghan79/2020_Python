#!/usr/bin/env python
'''
@name    :   Random_screen
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/26         ZH.Peng    2018010275
'''
from functools import wraps
from Random_gener import Random_gener
import pymongo
class Random_screen(object):
    '''
    This class is a decorated class
    '''
    def __init__(self, client, db, col, datatype, *args):
        '''
        As a database filtering function, in addition to the basic filtering conditions,
        it also needs database related information to extract information from the database,
        such as:adress,database name,col name
        
        Areas for improvement: self.dic = {int: "int", float: "float", str: "str"}
        '''
        self.myclient = pymongo.MongoClient(client)
        self.mydb = self.myclient[db]
        self.mycol = self.mydb[col]
        self.datatype = datatype
        self.args = args
        self.dict = {int: tuple, float: tuple, str: str}
        self.dic = {int: "int", float: "float", str: "str"} # To quickly convert keywords to string types 
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
        By querying the data items corresponding to the 'datatype', 
        access the value of the corresponding content under each item, 
        so as to filter the data stored in the database, 
        and finally store the filtered value into set and return it 
        '''
        try:
            print(condition)
            Random_gener.range_test(datatype, condition[0], self.dict[datatype])
            result = set()
            for it in self.mycol.find({"datatype": self.dic[datatype]}):
                item = it['content']
                if datatype is int or datatype is float:
                    fliter = iter(condition[0])
                    if next(fliter) <= item <= next(fliter):
                        result.add(item)
                elif datatype is str:
                    for fliter in condition:
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