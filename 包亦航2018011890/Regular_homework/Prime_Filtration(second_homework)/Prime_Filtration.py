# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Second python class homework in spring semester, 2020
    
    Introduction:
        A class for generate some all the prime numbers in the certain range 
        
    Special Tips:
        Using examples please look at Prime_Filtration_Test.py
        
    Created: 20/5/2020
    
    Last modified: 20/5/2020

"""

import math
from functools import wraps

######################################################################################################################
class Prime_Filtration(object):
    '''
    Attentions:
    This is a decorated class, you should using it by '@', examples please look at Prime_Filtration_TEST.py 
    at the same dictionary. 
    
    Please check all the using details below and in Prime_Filtration_TEST.py before using
    ''' 
    
    #------------------------------------------------------------------------------------------------------------------- 
    def __init__(self, start, end):
        '''
        Introduction
        ------------
        constructor
        
        
        Parameters
        ----------
        start: the start number of the range
        
        end : the end number of the range
        ----------
        '''
        if isinstance(start,int) and isinstance(end,int):
            pass
        else:
            print('numbers should be int!')
        self.start = start
        self.end = end
    
    #------------------------------------------------------------------------------------------------------------------- 
    def __call__(self, func, *args, **kwargs):
        """
        Introduction
        ------------
        Rewrite __call__ function in order to make it a decorative class
        
        """

        @wraps(func)  # To keep its own namespace
        def wrapper(*args, **kwargs):
            gener = self.__iter__()
            return func(gener, *args, **kwargs)
        return wrapper
    
    #------------------------------------------------------------------------------------------------------------------- 
    def __iter__(self):
        '''
        Introduction
        ------------
        try all numbers and make the class a generator
        
        Parameters
        ----------
        Introduced in  __init__

        '''
        try:
            for k in range(self.start, self.end):
                if self.isPrimeNum(k):
                    yield k
        except:
            print('Error occured when generate Prime numbers! Check again')    
    
    #------------------------------------------------------------------------------------------------------------------- 
    def isPrimeNum(self,k):
        '''
        Introduction
        ------------
        Check if a single number is a prime
        
        Parameters
        ----------
        The number need to be checked

        '''
        try:
            if k<2:
                return False
            for i in range(2,int(math.sqrt(k))+1):
                if k % i ==0:
                    return False
            return True
        except:
            print('Error occured when generate Prime numbers! Check again')
    

                

