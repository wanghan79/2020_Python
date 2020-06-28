# -*- coding: utf-8 -*-
# @Time : 2020/6/26 11:21
# @Author :Liuchenhui
# @File : 作业2.py

import random
import numpy as np
import scipy.stats as st

def decorate_random(func):
   def func_wrapper(p1,p2):
       return func(p1,p2)
   return func_wrapper
decorate_random1_object = decorate_random(random1)
dr1 = decorate_random1_object(1,100)
print(dr1)
decorate_random2_object = decorate_random(random2)
dr2 = decorate_random2_object(1,100)
print(dr2)
decorate_random3_object = decorate_random(random3)
dr3 = decorate_random3_object(1,100)
print(dr3)