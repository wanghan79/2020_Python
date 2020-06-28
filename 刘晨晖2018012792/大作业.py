# -*- coding: utf-8 -*-
# @Time : 2020/6/26 11:23
# @Author : Liuchenhui
# @File : 作业4.py

import pymongo
import random
import numpy as np
import scipy.stats as st

# 连接 ，默认连接本机
clicent = pymongo.MongoClient()
# 获得数据库
db = clicent.person
# 获得集合【表】
number = db.number
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

# mongodb存储数据
def save_num():
    # 生成器1
    generator1 = generator_random1(1, 100)
    num_list = []
    for t in generator1:
        num_list.append({"num1":t})
    # 生成器2
    generator2 = generator_random2(1, 100)
    for t in generator2:
        num_list.append({"num2":t})
    # 生成器3
    generator3 = generator_random3(1, 100)
    for t in generator3:
        num_list.append({"num3":t})

    # 保存到数据库中
    number.insert(num_list)
# save_num()

# 查询再次筛选数据
def get_by_momngodb_select():
    # 查询所有的数据
    num_list = number.find()
    new_num_list = []
    for s in num_list:
        if s.get("num1"):
            new_num_list.append(s.get("num1"))
        elif s.get("num2"):
            new_num_list.append(s.get("num2"))
        elif s.get("num3"):
            new_num_list.append(s.get("num3"))
    # 如果是偶数，将数据存储到re_num字段中
    for t in new_num_list:
        if t % 2 == 0:
            number.insert({"re_num":t})
get_by_momngodb_select()