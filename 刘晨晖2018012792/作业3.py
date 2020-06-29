# -*- coding: utf-8 -*- 
# @Time : 2020/6/26 11:22 
# @Author : Liuchenhui
# @File : 作业3.py 

import random
import numpy as np
import scipy.stats as st

def generator_random1(start,end):
    for i in range(10):
        c = random.randint(start, end)  # 生成a,b之间的随机整数，a<= * <=b
        if c % 2 == 0:
            yield c
def  generator_random2(start,end):
    for i in range(10):
        ori = np.random.randint(start, end)
        c = ori
        sums = 0
        while c:
            sums += c%10
            c = int(c/10)
        if sums % 2 ==0:
            yield ori
def  generator_random3(loc,scale):
    for i in range(10):
        # loc:均值  scale：标准差
        c = st.norm.rvs(loc=loc, scale=scale, size=[1])
        c = int(c[0])
        if c % 2 != 0:
            yield c
def get_number():   # 获得工作3的随机数
    generator1 = generator_random1(1,100)
    for t in generator1:
        print(str(t)+' ',end="")
    print()
    generator2 = generator_random2(1,100)
    for t in generator2:
        print(str(t)+' ',end="")
    print()
    generator3 = generator_random3(1,100)
    for t in generator3:
        print(str(t)+' ',end="")

# get_number()