##!/usr/bin/python3
"""
  Author:  Ying Wang
  Purpose: Finds a prime number in a specified range
  Created: 18/6/2020
"""
class PrimeNumbers:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i==0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k

for a in PrimeNumbers(10,100):
    print(a)