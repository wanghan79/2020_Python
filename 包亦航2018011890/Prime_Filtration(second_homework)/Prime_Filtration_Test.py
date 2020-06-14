# -*- coding: utf-8 -*-
"""
    Spyder Editor
    
    Author: 
        YihangBao
        2018011890
        
    Purpose: 
        Second python class homework in spring semester, 2020
    
    Introduction:
        Test function for Prime_Filtration
        
    Special Tips:
        Please put this and Prime_Filtration.py in the same dictionary
        
    Created: 20/5/2020
    
    Last modified: 20/5/2020

"""
from Prime_Filtration import Prime_Filtration

start_num = 1
end_num = 10000

@Prime_Filtration(start_num, end_num)
def test1(gener):
    '''
    generate all the prime number in range(1,10000) and count how many are them
    '''
    tot = 0
    for item in gener:
        tot+=1
        print(item)
    if tot == 0:
        print("No prime number in this range!")
    else:
        print("Total prime number: " + str(tot))
        
if __name__ == "__main__":
    test1() #call test1
