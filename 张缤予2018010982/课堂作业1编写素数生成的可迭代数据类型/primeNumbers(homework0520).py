##!/usr/bin/python3
'''

Author: By.Zhang      2018010982
Purpose: generate prime numbers in a specified range
Created: 20/5/2020

'''

class PrimeNumbers:
    def __init__(self, start, end):
        '''

        :param start: the start of range
        :param end: the end of range
        '''
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        '''

        :param k: a number you should judge if it is a prime number
        :return: 'true' means prime number and 'false' means non-prime number
        '''
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        '''

        :return: the prime number in range
        '''
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1, 52):
    print(x)
