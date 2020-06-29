# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Part of the third python class homework in spring semester, 2020
        In this edition we use yield to generate numbers or strings
    
    Introduction:
        A class for generate some random numbers or strings
        
    Special Tips:
        This class was made for using in Random_gener_picker_yield.py
        
    Created: 22/4/2020
    
    Last modified: 15/6/2020

"""
import random
from functools import wraps


######################################################################################################################
class Random_gener(object):
    '''
    Attentions:
    This is a decorated class, you may use it by '@'
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self,datatype,datarange,num,strlen):
        '''
        Introduction
        ------------
        constructor
        
        
        Parameters
        ----------
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
        
    #-------------------------------------------------------------------------------------------------------------------
    def __call__(self, func, *args, **kwargs):
        '''
        Introduction
        ------------
        Rewrite __call__ function in order to make it a decorative class
        
        '''
        @wraps(func)  # To keep its own namespace
        def wrapper(*args, **kwargs):
            dataset = self.gener(self.datatype,self.datarange,self.num,self.strlen)
            return func(dataset, *args, **kwargs)
        return wrapper

    #-------------------------------------------------------------------------------------------------------------------    
    def Input_checker(self, datatype, datarange, num, strlen):
        '''
        Introduction
        ------------
        Check if the input parameter meet the basic requirment
        
        Parameters
        ----------
        Introduced in  __init__

        '''
        if num<=0:
            raise Exception("num should bigger than 0")
        if datatype is int:
            if isinstance(datarange,list)==False:
                raise Exception("Datarange should be a list!",type(datarange))
            if len(datarange)!=2:
                raise Exception("Datarange should have 2 numbers!")
            if datarange[1]-datarange[0]<=0:
                raise Exception("The second number should bigger than the first one!")
            if datarange[1]-datarange[0]<num:
                raise Exception("The number waiting to be chosen shouldn't less than the number you need!")
        if datatype is float:
            if isinstance(datarange,list)==False:
                raise Exception("Datarange should be a list!",type(datarange))
            if len(datarange)!=2:
                raise Exception("Datarange should have 2 numbers!")
            if datarange[1]-datarange[0]<=0:
                raise Exception("The second number should bigger than the first one!")
        if datatype is str:
            if isinstance(datarange,str)==False:
                raise Exception("Datarange should be a str!",type(datarange))    
         
    #-------------------------------------------------------------------------------------------------------------------
    def gener(self, datatype, datarange, num, strlen=10):
        '''
        Introduction
        ------------
        Core part of generate the items you need, format showed in Random_gener_picker_test.py
        
        Parameters
        ----------
        Introduced in  __init__

        '''
        try:
            self.Input_checker(datatype, datarange, num, strlen) #check the input legal or not
            ans = 0
            if datatype is float:
                while ans<num:
                    yield random.random()*(datarange[1]-datarange[0])+datarange[0] #yield them!
                    ans += 1
            elif datatype is int:
                while ans<num:
                    yield int(random.random()*(datarange[1]-datarange[0])+datarange[0])
                    ans += 1
            elif datatype is str:
                while ans<num:
                    yield ''.join(random.sample(datarange,strlen))
                    ans += 1
        except Exception as e: #print the error name
            print(str(e))
            print('This Error occured when gennerating!!!!!')
            