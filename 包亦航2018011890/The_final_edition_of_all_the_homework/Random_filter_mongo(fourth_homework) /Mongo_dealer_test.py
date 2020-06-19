# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Test class of the fourth python class homework in spring semester, 2020
    
    Introduction:
        Test class for Mongo_dealer.py
        
    Special Tips:
        Please put this and Mongo_dealer.py in the same dictionary
        
    Created: 17/6/2020
    
    Last modified: 17/6/2020
"""

from Mongo_dealer import Mongo_dealer
import string
import sys

#-------------------------------------------------------------------------------------------------------------------
def test1():
    '''
    here we use mongodealer to generate random string twice and pick the string owing to our need
    '''
    exp1 = Mongo_dealer("mongodb://localhost:27017/","BoilMongo","BoilMongo")
    exp1.gener(str, string.ascii_letters+string.digits+"@#$!", 2000,5) #generate 2000 strings and its length is 5
    result = exp1.pick(str,'Aa','Ab') #Pick the strings with 'a' and 'b' 
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/2000 *100) + "%") 
    print("Thank you for using my method!\n")
    exp1.gener(str, string.ascii_letters+string.digits+"@#$!", 1000,5)#generate 1000 strings and its length is 5
    result = exp1.pick(str,'Oa') #Pick the strings with 'a'
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/1000 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.dele() #delete the content

#-------------------------------------------------------------------------------------------------------------------
def test2():
    '''
    here we use mongodealer to generate random int three times and pick the string owing to our need
    '''
    exp1 = Mongo_dealer("mongodb://localhost:27017/","BoilMongo","BoilMongo")
    exp1.gener(int,[1,1000],200,0) #gennerate 200 int digits in range(1,1000)
    result = exp1.pick(int,'>500','<700') #pick the digits smaller than 700,bigger than 500
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.gener(int,[1,1000],200,0) #gennerate 200 int digits in range(1,1000)
    result = exp1.pick(int,'>550','<700','<800') #pick the digits smaller than 700 800,bigger than 550
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.gener(int,[1,1000],200,0) #gennerate 200 int digits in range(1,1000)
    result = exp1.pick(int,'>560','<600') #pick the digits smaller than 600,bigger than 560
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.dele() #delete the content

#-------------------------------------------------------------------------------------------------------------------
def test3():
    '''
    here we use mongodealer to generate random float three times and pick the string owing to our need
    '''
    exp1 = Mongo_dealer("mongodb://localhost:27017/","BoilMongo","BoilMongo")
    exp1.gener(float,[1,1000],200,0) # gennerate 200 float digits in range(1,1000)
    result = exp1.pick(float,'>500','<700','<900','<1000') #pick the digits smaller than 700 900 1000,bigger than 500
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.gener(float,[1,1000],200,0) # gennerate 200 float digits in range(1,1000)
    result = exp1.pick(float,'>550','<700','<800') #pick the digits smaller than 700 800,bigger than 550
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.gener(float,[1,1000],200,0) # gennerate 200 float digits in range(1,1000)
    result = exp1.pick(float,'>560','<600') #pick the digits smaller than 600,bigger than 560
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.dele() #delete the content

#-------------------------------------------------------------------------------------------------------------------
def test4():
    '''
    here we generate different type of items and pick them
    '''
    exp1 = Mongo_dealer("mongodb://localhost:27017/","BoilMongo","BoilMongo")
    exp1.gener(str, string.ascii_letters+string.digits+"@#$!", 1000,5) #generate 1000 strings and its length is 5
    exp1.gener(int,[1,1000],200,0) #gennerate 200 int digits in range(1,1000)
    exp1.gener(float,[1,1000],200,0) # gennerate 200 float digits in range(1,1000)
    result = exp1.pick(int,'>550','<700','<800') #pick the digits smaller than 700 800,bigger than 550
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    result = exp1.pick(float,'>400','>560','<600') #pick the digits smaller than 600,bigger than 560 400
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/200 *100) + "%")
    print("Thank you for using my method!\n")
    result = exp1.pick(str,'Oa') #Pick the strings with 'a'
    print(result)
    print("====")
    print("As showed above, we find " + str(len(result)) + " strings meet your requirement")
    print("The finding rate is " + str(len(result)/1000 *100) + "%")
    print("Thank you for using my method!\n")
    exp1.dele() #delete the content


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