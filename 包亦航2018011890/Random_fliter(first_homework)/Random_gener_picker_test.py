# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        First python class homework in spring semester, 2020
    
    Introduction:
        Test functions for Random_gener_picker
        
    Special Tips:
        Please put this and Random_gener_picker_test.py in the same dictionary
        
    Created: 22/4/2020
    
    Last modified: 22/4/2020
"""

from Random_gener_picker_By_YihangBao import Random_gener_picker
import string


@Random_gener_picker(int,[1,1000],20,0,'>500','<700')
def test1(result):
    '''
    gennerate 20 int digits in range(1,1000), and pick the digits smaller than 700,
    bigger than 500.
    pay attention: 0 here is meaningless but necessary. It fill the strlen parameter
    '''
    print(result)
#-------------------------------------------------------------------------------------------------------------------

@Random_gener_picker(float,[1,1000],20,0,'>500','<700')
def test2(result):
    '''
    gennerate 20 float digits in range(1,1000), and pick the digits smaller than 700,
    bigger than 500
    pay attention: 0 here is meaningless but necessary. It fill the strlen parameter
    '''
    print(result)

#-------------------------------------------------------------------------------------------------------------------
    
@Random_gener_picker(str, string.ascii_letters+string.digits+"@#$!", 1000,5,'Aa','Ab')
def test3(result):
    '''
    gennerate 1000 strings and its length is 5. Pick the strings with 'a' and 'b'
    '''
    print(result)
#-------------------------------------------------------------------------------------------------------------------
    
@Random_gener_picker(str, string.ascii_letters+string.digits+"@#$!", 1000,5,'Oa','Ob')
def test4(result):
    '''
    gennerate 1000 strings and its length is 5. Pick the strings with 'a' or 'b'
    '''
    print(result)

test1()
print('#---------------------------')
test2()
print('#---------------------------')
test3()
print('#---------------------------')
test4()