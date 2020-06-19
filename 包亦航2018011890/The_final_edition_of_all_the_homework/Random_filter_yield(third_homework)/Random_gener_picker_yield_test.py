# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Part of the third python class homework in spring semester, 2020
    
    Introduction:
        Test functions for Random_gener_picker_yield
        
    Special Tips:
        Please put this and Random_gener_picker_yield.py in the same dictionary
        
    Created: 22/4/2020
    
    Last modified: 22/4/2020
"""

from Random_gener_picker_yield import Random_gener_picker
import string
import sys


@Random_gener_picker(int,[1,1000],200,0,'>500','<700')
def test1(result):
    '''
    gennerate 200 int digits in range(1,1000), and pick the digits smaller than 700,
    bigger than 500.
    pay attention: 0 here is meaningless but necessary. It fill the strlen parameter
    '''
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " numbers meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!")
#-------------------------------------------------------------------------------------------------------------------

@Random_gener_picker(float,[1,1000],300,0,'>500','<700','>400','<900')
def test2(result):
    '''
    gennerate 300 float digits in range(1,1000), and pick the digits smaller than 700,900 ,
    bigger than 500,400
    pay attention: 0 here is meaningless but necessary. It fill the strlen parameter
    '''
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " numbers meet your requirement")
    print("The finding rate is " + str(len(result)/300 *100) + "%")
    print("Thank you for using my method!")

#-------------------------------------------------------------------------------------------------------------------
    
@Random_gener_picker(str, string.ascii_letters+string.digits+"@#$!", 2000,5,'Aa','Ab')
def test3(result):
    '''
    gennerate 2000 strings and its length is 5. Pick the strings with 'a' and 'b'
    '''
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/2000 *100) + "%")
    print("Thank you for using my method!")
    
#-------------------------------------------------------------------------------------------------------------------
    
@Random_gener_picker(str, string.ascii_letters+string.digits+"@#$!", 500,5,'Oa','Ob','Oc')
def test4(result):
    '''
    gennerate 500 strings and its length is 5. Pick the strings with 'a' or 'b' or 'c'
    '''
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/500 *100) + "%")
    print("Thank you for using my method!")

#-------------------------------------------------section-----------------------------------------------------------
# file output section, once enabled, the output will be redirected to file out.txt

# savedStdout = sys.stdout
# f = open('out.txt','w')
# sys.stdout = f
#-------------------------------------------------------------------------------------------------------------------
test1()
print('\n#---------------------------------------------------------------------------------\n')
test2()
print('\n#---------------------------------------------------------------------------------\n')
test3()
print('\n#---------------------------------------------------------------------------------\n')
test4()
