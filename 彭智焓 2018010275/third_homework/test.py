#!/usr/bin/env python
'''
@name    :   test
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/23         ZH.Peng    2018010275
'''
from Random_yield import Random_yield
import string
@Random_yield(int, (1, 100), 5, 1, (16,61))
def test1(res):
    print(res)
@Random_yield(float, (1, 100), 5, 1, (3.14, 52.0))
def test2(res):
    print(res)
@Random_yield(str, string.ascii_letters + string.digits + "@#$!", 10, 5, 'a', 'b', 'c')
def test3(res):
    print(res)
print('test 1:')
test1()
print('############################')
print('test 2:')
test2()
print('############################')
print('test 3:')
test3()
print('############################')