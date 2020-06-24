##!/usr/bin/python3
"""
  Author:  MinHong.Zhu
  Purpose: Using generators to generate prime numbers in any legal range.
  Created: 25/5/2020
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

result=[]
for x in PrimeNumbers(1,100):
    result.append(x)
print(result)

result=[]
for x in PrimeNumbers(100,1000):
    result.append(x)
print(result)

result=[]
for x in PrimeNumbers(1000,10000):
    result.append(x)
print(result)