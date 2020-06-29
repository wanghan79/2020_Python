# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Part of the fourth python class homework in spring semester, 2020
        In this edition we use MongoDB to store numbers or strings we generate and pick them owing to our need
    
    Introduction:
        A class for operating the MongoDB, operation include generation, picking and clearing
        
    Special Tips:
        Using examples please look at Mongo_dealer_test.py
        
    Created: 17/6/2020
    
    Last modified: 18/6/2020

"""

import pymongo
from Mongo_picker import Mongo_picker
from Random_mongo_gener import Random_mongo_gener


######################################################################################################################
class Mongo_dealer(object):
    '''
    Attentions:

    Please check all the using details below and in Mongo_dealer_test.py before using
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self,ad,client_name,set_name): 
        '''
        Introduction
        ------------
        constructor
        
        
        Parameters
        ----------
        ad: the adress of your MongoDB server, default is mongodb://localhost:27017/
        
        client_name: the name of your client of MongoDB
        
        set_name: the name of your dataset of MongoDB
        ----------
        '''
        self.ad = ad
        self.cname = client_name
        self.sname = set_name
        self.myclient = pymongo.MongoClient(ad) # "mongodb://localhost:27017/"
        self.db = self.myclient[client_name]
        self.db_first = self.db[set_name]
        
    #-------------------------------------------------------------------------------------------------------------------
    def gener(self,datatype,datarange,num,strlen):
        '''
        Introduction
        ------------
        generate items according to your need
        
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

        '''
        @Random_mongo_gener(self.ad, self.cname, self.sname, datatype, datarange, num, strlen)
        def run_gener():
            pass
        
        run_gener()
    
    #-------------------------------------------------------------------------------------------------------------------
    def pick(self,datatype,*args):
        '''
        Introduction
        ------------
        pick items and return them
        
        Parameters
        ----------
        *args: variable parameter, the conditions you need. For datatype in int or float, you should 
        begin with '<' or '>', following a number behind. Just like '>100', '<500'.
        If the datatype is str, it begins with 'A' or 'O', A means and, we should meet all the conditions
        O means or, we only need to meet one of the conditions. String followed are the substrings you
        want them to have. Just like 'Aat', 'Oyh'. And pay attention, the condtions in one time should
        be purely A or O.

        '''
        @Mongo_picker(self.ad, self.cname, self.sname, datatype,args)
        def run_picker(result_set):
            ans = set()
            for item in result_set:
                ans.add(item['content']) #withdraw all content
            return ans #return the items meet the requirement
        
        re = run_picker()
        return re
    
    #-------------------------------------------------------------------------------------------------------------------
    def dele(self):
        '''
        Introduction
        ------------
        delete all the items in MangoDB set

        '''
        self.db_first.delete_many({}) #delete them
        
