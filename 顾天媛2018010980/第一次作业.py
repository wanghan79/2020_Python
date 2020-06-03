# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: Generate random data set.
  Created: 18/4/2020
"""

import random
import string

def create_set(datatype, datarange, num, strlen=8):
    old_set = set()
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                old_set.add(item)
                continue

        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                old_set.add(item)
                continue

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                old_set.add(item)
                continue
        return old_set
    except Exception as e:
        print(e)
        print('你输入的参数有误')



def select_set(old_set, datatype, datarange):
    new_set = set()
    try:
        for x in old_set:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_set.add(x)
                continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_set.add(x)
                continue

            elif datatype is str:
                if x.find(datarange) != -1:
                    new_set.add(x)
                continue
        return new_set
    except Exception as e:
        print(e)
        print('你输入的参数有误')

def apply():
    base_str = string.ascii_letters + string.digits #   + string.punctuation
    old_set1 = create_set(int, (1,100), 10)
   # print(old_set1)
    new_set1 = select_set(old_set1, int, (2,50))
    print(new_set1)
    print('---------------------------------------------')
    old_set2 = create_set(float, (100, 200), 20)
   # print(old_set2)
    new_set2 = select_set(old_set2, float, (100, 500))
    print(new_set2)
    print('---------------------------------------------')
    old_set3 = create_set(str, base_str, 50,10)
   # print(old_set3)
    new_set3 = select_set(old_set3, str, 'a')
    print(new_set3)


apply()