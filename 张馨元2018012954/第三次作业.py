##!/usr/bin/python3
"""
  Author:  XinYuan.Zhang
  Purpose: Using generators to generate prime numbers in any legal range.
  Created: 19/6/2020
"""
class PrimeNumbers:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isPrimeNum(self,i):
        if i<2:
            return False
        for j in range(2,i):
            if i%j==0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k
for k in PrimeNumbers(1,10000):
    print(k)

