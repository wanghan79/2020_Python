#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : GaoXingyuan
# @FileName: 1-100PrimeNumbers.py
# @Software: PyCharm
def isPrimeNum(k):
    if k < 2:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        for k in range(self.start, self.end):
            if isPrimeNum(k):
                yield k

result=[]
for x in PrimeNumbers(1, 100):
    result.append(x)
print("1-100Prime Numbers are:")
for i in result:
    print(i,end=" ")