"""
  Author:JLH2018010984
  Created: 2020/6/19
"""

import random
import math

def print_line():
    print("*" * 60)
print_line()

def Primes(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def JLHPrimes():
    for elem in range(0,9999):
        if Primes(elem):
            print(elem)
if __name__ == '__main__':
    JLHPrimes()

print_line()