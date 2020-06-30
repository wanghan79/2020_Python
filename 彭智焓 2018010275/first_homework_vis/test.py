#!/usr/bin/env python
'''
@name    :   Random_generator
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/29         ZH.Peng    2018010275
'''
from Random_generator import Random_generator
import string
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
@Random_generator(int, (1, 100), 50, 1, (16,61))
def test1(res):
    print(res)
    x = range(1, len(res)+1, 1)
    y = list(res)
    plt.scatter(x, y, color='deepskyblue', alpha=0.7)
    plt.xlabel('整数数据可视化')
    plt.show()
@Random_generator(float, (1, 100), 100, 1, (3.14, 52.0))
def test2(res):
    print(res)
    x = range(1, len(res)+1, 1)
    y = list(res)
    plt.scatter(x, y, color='lightpink', alpha=0.7)
    plt.xlabel('浮点数数据可视化')
    plt.show()
@Random_generator(str, string.ascii_letters + string.digits + "@#$!", 10, 5, 'a', 'b', 'c')
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