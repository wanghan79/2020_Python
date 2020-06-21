#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 16:06
# @Author  : liyuhan
# @File    : primenumber.py
"""
   Author:liyuhan
   Purpose:Iterative generation of prime Numbers.(复习上课代码)
   Created:2020
"""
class PrimeNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1,100):
    print(x)

