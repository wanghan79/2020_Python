# -*- coding: utf-8 -*-
# @Time : 2020/6/26 11:19
# @Author :Liuchenhui
# @File : 作业1.py
import random
import numpy as np
import scipy.stats as st

def random1(start,end):
    c = random.randint(start, end)  # 生成a,b之间的随机整数，a<= * <=b

    if c % 2 == 0:
        return "%s:符合规则1"%c
    else:
        return "%s:不符合规则1"%c
def random2(start,end):
    ori = np.random.randint(start, end)
    c = ori
    sums = 0
    while c:
        sums += c%10
        c = int(c/10)
    if sums % 2 ==0:
        return "%s:符合规则2"%ori
    else:
        return "%s:不符合规则2"%ori
def random3(loc,scale):
    # loc:均值  scale：标准差
    c = st.norm.rvs(loc=loc, scale=scale, size=[1])
    c = int(c[0])
    if c % 2 !=0 :
        return "%s:符合规则3"%c
    else:
        return "%s:不符合规则3"%c

print(random1(1,100))
print(random2(1,100))
print(random3(1,100))
