# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Part of the fourth python class homework in spring semester, 2020
    
    Introduction:
        A class for store the items we generate into MongoDB
        
    Special Tips:
        File 'Random_gener.py' is required
        This class has been utilized in 'Mongo_dealer.py'
        
    Created: 17/6/2020
    
    Last modified: 18/6/2020

"""
from Random_gener import Random_gener
from functools import wraps
import pymongo


######################################################################################################################
class Random_mongo_gener(object):
    '''
    Attentions:
    This is a decorated class, you may use it by '@'
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self,ad,client_name,set_name,datatype,datarange,num,strlen):
        '''
        Introduction
        ------------
        constructor
        
        
        Parameters
        ----------
        ad: the adress of your MongoDB server, default is mongodb://localhost:27017/
        
        client_name: the name of your client of MongoDB
        
        set_name: the name of your dataset of MongoDB
        
        datatype: the type of the random data you need, it now only supports int,float or str
        
        datarange: if your datatype is int or float, this will be a list of two elements, like[a,b]
        which means the random numbers generate are bigger than a, smaller than b(b not included).
        And if your datatype is str, the datarange will be a string, it will pick chars from it 
        
        num: The number of digits or strings you want to generate
        
        strlen: This one is quite special. It means how many letters in one string. Obviously we
        needn't it while the datatype is int or float. However, according to the 'args' behind, we can't
        make it an omissible parameter, so when your datatype is int or float we still need to input
        something to fill it.
        
        ----------
        '''
        self.datatype = datatype
        self.datarange = datarange
        self.num = num
        self.strlen = strlen
        self.myclient = pymongo.MongoClient(ad) # "mongodb://localhost:27017/"
        self.db = self.myclient[client_name]
        self.db_first = self.db[set_name]
        
    #-------------------------------------------------------------------------------------------------------------------
    def __call__(self, func, *args, **kwargs):
        '''
        Introduction
        ------------
        Rewrite __call__ function in order to make it a decorative class
        
        '''
        @wraps(func)  # To keep its own namespace
        def wrapper(*args, **kwargs):
            self.getmongo()
            return func(*args, **kwargs)
        return wrapper
    
    #-------------------------------------------------------------------------------------------------------------------
    def getmongo(self):
        '''
        Introduction
        ------------
        This is the core part to store the items we gener into the MongoDB
        The function below is decorated
        
        '''
        @Random_gener(self.datatype,self.datarange,self.num,self.strlen)
        def run_getmongo(dataset):
            flag = True #check the generator empty or not
            while(flag):
                try:
                    cand = next(dataset)
                except StopIteration:
                    flag = False
                if flag == False:
                    break #if run out of items, break
                if self.datatype is int:
                    numberlist = {"type":"int", "content":cand}
                if self.datatype is float:
                    numberlist = {"type":"float", "content":cand}
                if self.datatype is str:
                    numberlist = {"type":"str", "content":cand}
                self.db_first.insert_one(numberlist)
        run_getmongo()
        