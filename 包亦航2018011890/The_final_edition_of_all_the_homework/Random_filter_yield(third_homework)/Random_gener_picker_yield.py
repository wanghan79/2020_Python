# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Third python class homework in spring semester, 2020
        This edtion was for the third homework. In this edition we support int float and string generation.
        Compared to the third homework, here I modified the Random_gener.py to make it a generator and I modified
        some details in the function named pick accordingly
    
    Introduction:
        A class for generate some random numbers or strings and pick some of them owing to your need
        
    Special Tips:
        Using examples please look at Random_gener_picker_yield_test.py
        
    Created: 22/4/2020
    
    Last modified: 15/6/2020
    
    *********** Modified ***********
    Date: 15/6/2020
    Content: This file was modified to meet the requirement of the homework3
    Modified by Yihang Bao
"""

from functools import wraps
from Random_gener_yield import Random_gener


######################################################################################################################
class Random_gener_picker(object):
    '''
    Attentions:
    This is a decorated class, you may use it by '@', examples please look at Random_gener_picker_test.py 
    at the same dictionary. 
    
    Please check all the using details below and in Random_gener_picker_test.py before using
    '''
    
    #-------------------------------------------------------------------------------------------------------------------  
    def __init__(self,datatype,datarange,num,strlen,*args):
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
        
        *args: variable parameter, the conditions you need. For datatype in int or float, you should 
        begin with '<' or '>', following a number behind. Just like '>100', '<500'.
        If the datatype is str, it begins with 'A' or 'O', A means and, we should meet all the conditions
        O means or, we only need to meet one of the conditions. String followed are the substrings you
        want them to have. Just like 'Aat', 'Oyh'. And pay attention, the condtions in one time should
        be purely A or O.
            
            
        ----------
        '''
        self.datatype = datatype
        self.datarange = datarange
        self.num = num
        self.strlen = strlen
        self.args = args
        #print(self.pick(datatype,self.genner(datatype,datarange,num,strlen),args))
        
    #-------------------------------------------------------------------------------------------------------------------
    def __call__(self, func, *args, **kwargs):
        '''
        Introduction
        ------------
        Rewrite __call__ function in order to make it a decorative class
        
        '''
        @wraps(func)  # To keep its own namespace
        def wrapper(*args, **kwargs):
            result = self.pick(self.datatype,self.args)
            return func(result, *args, **kwargs)
        return wrapper
            
    #-------------------------------------------------------------------------------------------------------------------
    def pick(self, datatype, ar):
        '''
        Introduction
        ------------
        find numbers and strings that meet the requiement, format showed in Random_gener_picker_test.py
        
        Parameters
        ----------
        Initailly ar is *args, but the ar here we just recieve the args temple from __init__.
        Others are introduced in  __init__

        '''
        @Random_gener(self.datatype,self.datarange,self.num,self.strlen) #This is the core difference compared with the first homework
        def run_p(dataset):
            try:
                tempset = set() #it a temporary set using in picking
                flag = True
                if datatype is int:
                    while(flag):
                        try:
                            cand = next(dataset) #next item
                        except StopIteration: #if no more items in generator then break
                            flag = False # we should break now 
                        if flag == False:
                            break
                        ok = False
                        for com in ar:
                            numb = int(com[1:]) #the first character is > or < so we should splite them
                            ok = False
                            if com[0]=='>':
                                if cand>numb: # pick numbers bigger than numb
                                    ok = True
                            elif com[0]=='<':
                                if cand<numb: # pick numbers bigger than numb
                                    ok = True
                            else: #the first character must  >  or <
                                raise Exception("Unsupported operator '" + com[0] + "'")
                            if ok == False:
                                break
                        if ok:
                            tempset.add(cand)
                    return tempset
                elif datatype is float: #do the same to float
                    while(flag):
                        try:
                            cand = next(dataset) #next item
                        except StopIteration: #if no more items in generator then break
                            flag = False # we should break now 
                        if flag == False:
                            break
                        ok = False
                        for com in ar:
                            numb = float(com[1:]) #the first character is > or < so we should splite them
                            ok = False
                            if com[0]=='>':
                                if cand>numb: # pick numbers bigger than numb
                                    ok = True
                            elif com[0]=='<':
                                if cand<numb: # pick numbers bigger than numb
                                    ok = True
                            else: #the first character must  >  or <
                                raise Exception("Unsupported operator '" + com[0] + "'")
                            if ok == False:
                                break
                        if ok:
                            tempset.add(cand)
                    return tempset
                elif datatype is str:
                    tempset.clear()
                    flag1 = False
                    flag2 = False
                    while(flag):
                        try:
                            cand = next(dataset) #next item
                        except StopIteration: #if no more items in generator then break
                            flag = False # we should break now 
                        if flag == False:
                            break
                        flag3 = True
                        for com in ar: #list all the condition
                            strb = str(com[1:]) #the first character is > or < so we should splite them
                            if com[0]=='O':
                                flag1=True
                                flag3 = False
                                if flag2:
                                    raise Exception("It should all be A or all be O!")
                                if strb in cand: #find the given string
                                    flag3 = True
                                    break
                            elif com[0]=='A':
                                flag2=True
                                if flag1:
                                    raise Exception("It should all be A or all be O!")
                                if strb not in cand: #find the given string
                                    flag3 = False
                            else:
                                flag3 = False
                                raise Exception("Unsupported operator '" + com[0] + "'")
                        if flag3: #add it
                            tempset.add(cand)
                    return tempset
                
                else:
                    raise Exception("Unsupported Type!",datatype)
            except Exception as e:
                print(str(e))
                print('This Error occured when picking!!!!!')
        
        final_result = run_p()
        return final_result
        
