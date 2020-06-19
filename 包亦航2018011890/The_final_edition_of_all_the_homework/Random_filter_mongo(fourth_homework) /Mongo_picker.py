# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Part of the fourth python class homework in spring semester, 2020
    
    Introduction:
        A class for select items in MongoDB owing to your need 
        
    Special Tips:
        This file has been utilized in 'Mongo_dealer.py'
        
    Created: 17/6/2020
    
    Last modified: 18/6/2020
    
"""

from functools import wraps
import pymongo


######################################################################################################################
class Mongo_picker(object):
    '''
    Attentions:
    This is a decorated class, you may use it by '@'
    
    Please check all the using details below and in Mongo_dealer.py before using
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self,ad,client_name,set_name,datatype,*args):
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
        
        *args: variable parameter, the conditions you need. For datatype in int or float, you should 
        begin with '<' or '>', following a number behind. Just like '>100', '<500'.
        If the datatype is str, it begins with 'A' or 'O', A means and, we should meet all the conditions
        O means or, we only need to meet one of the conditions. String followed are the substrings you
        want them to have. Just like 'Aat', 'Oyh'. And pay attention, the condtions in one time should
        be purely A or O.
            
        ----------
        '''
        self.datatype = datatype
        self.argss = args
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
            result = self.pick(self.datatype,self.argss)
            return func(result, *args, **kwargs)
        return wrapper
            
    #-------------------------------------------------------------------------------------------------------------------
    def pick(self, datatype, ar):
        '''
        Introduction
        ------------
        find numbers or strings that meet the requiement
        
        Parameters
        ----------
        Initailly ar is *args, but the ar here we just recieve the args temple from __init__.
        Others are introduced in  __init__

        '''
        try:
            ar = ar[0]
            if datatype is int:
                bline = float("-inf") #bline means baseline
                tline = float("inf") #tline means topline
                for com in ar:
                    numb = int(com[1:]) #the first character is > or < so we should splite them
                    if com[0]=='>':
                        bline = max(bline, numb) #the baseline should be highest of them
                    elif com[0]=='<':
                        tline = min(tline, numb) #the topline should be lowest of them
                    else: #the first character must > or <
                        raise Exception("Unsupported operator '" + com[0] + "'")
                for result in self.db_first.find({'type':'int','content' :{"$gt": bline, "$lt": tline}}): #advanced MongoDB search
                    yield result #yield the items meet the requirement
                    
            elif datatype is float: #do the same to float
                bline = float("-inf") #bline means baseline
                tline = float("inf") #tline means topline
                for com in ar:
                    numb = float(com[1:]) #the first character is > or < so we should splite them
                    if com[0]=='>':
                        bline = max(bline, numb)
                    elif com[0]=='<':
                        tline = min(tline, numb)
                    else: #the first character must  >  or <
                        raise Exception("Unsupported operator '" + com[0] + "'")
                for result in self.db_first.find({'type':'float','content' :{"$gt": bline, "$lt": tline}}):
                    yield result
                    
            elif datatype is str:
                flag1 = False #flag1 and flag2 are designed to check if the input start with all 'O' or all 'A'
                flag2 = False
                cmdset = ''
                for com in ar:
                    strb = str(com[1:]) #the first character is A or O so we should splite them
                    if com[0]=='O':
                        flag1=True
                        if flag2:
                            raise Exception("It should all be A or all be O!")
                        ope = 'O'
                        cmdset = cmdset + '(.*' + strb + '.*)|' #here I use Regular Expression to match in MongoDB
                    elif com[0]=='A':
                        flag2=True
                        if flag1:
                            raise Exception("It should all be A or all be O!")
                        ope = 'A'
                        cmdset = cmdset + '(?=.*' + strb + '.*)' #here I use Regular Expression to match in MongoDB
                    else:
                        raise Exception("Unsupported operator '" + com[0] + "'")
                if ope == 'O':
                    cmdset = cmdset[:-1] #the last '|' should be deleted
                for result in self.db_first.find({'type':'str','content':{"$regex": cmdset}}): #here I use Regular Expression to match in MongoDB
                    yield result
            
            else:
                raise Exception("Unsupported Type!",datatype)
        except Exception as e:
            print(str(e))
            print('This Error occured when picking!!!!!')
        
        
