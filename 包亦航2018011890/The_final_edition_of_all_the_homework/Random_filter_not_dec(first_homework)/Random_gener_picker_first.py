# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        First python class homework in spring semester, 2020
        This edtion was for the first homework. In this edition we support int float and string generation.
        The whole class was decorated here but the function gener and picker are seperated, which remain to be 
        combined in the second home work
    
    Introduction:
        A class for generate some random numbers or strings and pick some of them owing to your need
        
    Special Tips:
        Using examples please look at Random_gener_picker_test.py
        
    Created: 22/4/2020
    
    Last modified: 15/6/2020
    
    *********** Modified ***********
    Date: 15/6/2020
    Content: This file was modified to meet the requirement of the homework1
    Modified by Yihang Bao
"""
import random
from functools import wraps


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
            result = self.pick(self.datatype,self.gener(self.datatype,self.datarange,self.num,self.strlen),self.args)
            return func(result, *args, **kwargs)
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
            ans = set() # a set contains random results
            if datatype is float:
                while len(ans)<num:
                    ans.add(random.random()*(datarange[1]-datarange[0])+datarange[0]) #random method can generate numbers in [0..1]
            elif datatype is int:
                while len(ans)<num:
                    ans.add(int(random.random()*(datarange[1]-datarange[0])+datarange[0]))
            elif datatype is str:
                while len(ans)<num:
                    ans.add(''.join(random.sample(datarange,strlen)))
            return ans
        except Exception as e:
            print(str(e)) #print the error name
            print('This Error occured when gennerating!!!!!')
            
    #-------------------------------------------------------------------------------------------------------------------
    def pick(self, datatype, dataset, ar):
        '''
        Introduction
        ------------
        find numbers and strings that meet the requiement, format showed in Random_gener_picker_test.py
        
        Parameters
        ----------
        Initailly ar is *args, but the ar here we just recieve the args temple from __init__.
        Others are introduced in  __init__

        '''
        try:
            ans = dataset #ans contains the result
            tempset = set() #it a temporary set using in picking
            if datatype is int:
                for com in ar:
                    numb = int(com[1:]) #the first character is > or < so we should splite them
                    tempset.clear()
                    if com[0]=='>':
                        for item in filter(lambda x:x>numb, ans): # pick numbers bigger than numb
                            tempset.add(item) #add items meet the requirement
                        ans = tempset.copy() #copy it to ans
                    elif com[0]=='<':
                        for item in filter(lambda x:x<numb, ans):
                            tempset.add(item) #add items meet the requirement
                        ans = tempset.copy() #copy it to ans
                    else: #the first character must  >  or <
                        raise Exception("Unsupported operator '" + com[0] + "'")
                return ans
            elif datatype is float: #do the same to float
                for com in ar:
                    numb = float(com[1:]) #the first character is > or < so we should splite them
                    tempset.clear()
                    if com[0]=='>':
                        for item in filter(lambda x:x>numb, ans): # pick numbers bigger than numb
                            tempset.add(item) #add items meet the requirement
                        ans = tempset.copy() #copy it to ans
                    elif com[0]=='<':
                        for item in filter(lambda x:x<numb, ans):
                            tempset.add(item) #add items meet the requirement
                        ans = tempset.copy() #copy it to ans
                    else:
                        raise Exception("Unsupported operator '" + com[0] + "'")
                return ans
            elif datatype is str:
                tempset.clear()
                flag1 = False #flag1 and flag2 are designed to check if the input start with all 'O' or all 'A'
                flag2 = False
                for com in ar:
                    strb = str(com[1:]) #the first character is A or O so we should splite them
                    if com[0]=='O':
                        flag1=True
                        if flag2:
                            raise Exception("It should all be A or all be O!")
                        for item in filter(lambda x:x.find(strb)!=-1, ans): #find the given string
                            tempset.add(item) #add items meet the requirement
                    elif com[0]=='A':
                        flag2=True
                        if flag1:
                            raise Exception("It should all be A or all be O!")
                        tempset.clear()
                        for item in filter(lambda x:x.find(strb)!=-1, ans): #find the given string
                            tempset.add(item) #add items meet the requirement
                        ans = tempset.copy()
                    else:
                        raise Exception("Unsupported operator '" + com[0] + "'")
                if flag1: #flag1 means command is O
                    return tempset
                else:
                    return ans
            else:
                raise Exception("Unsupported Type!",datatype)
        except Exception as e:
            print(str(e))
            print('This Error occured when picking!!!!!')

