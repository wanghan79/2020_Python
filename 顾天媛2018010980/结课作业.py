# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: random data set & MongoDB
  Created: 24/6/2020
"""
# 结课作业：使用MongoDB存储平时作业3中生成的随机数，并能从MongoDB中查询数据进行数据筛选。
import random
import string
import pymongo
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017")   # 生成mongodb对象
mydb = myclient["test"]
mycol = mydb["t1"]

def create_set(datatype, datarange, num, strlen=8):
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item

        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
        else:
            print('请输入datatype:int、float、str!')
    except OverflowError:
        print('数值运算超出最大限制')
    except TypeError:
        print('对类型无效的操作')
    except ValueError:
        print('ValueError 传入无效的参数')
    except Exception as e:
        print(e)
        print('你输入的参数有误')



def select_set(old_set, datatype, datarange):
    mycol.drop()
    for i in old_set:
        mycol.insert_one({'num':i})
    try:
        for x in mycol.find({},{'num':1}):
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x['num'] <= next(it):
                    print(x['num'])
                continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x['num'] <= next(it):
                    print(x['num'])
                continue

            elif datatype is str:
                if x['num'].find(datarange) != -1:
                    print(x['num'])
                continue
    except OverflowError:
        print('数值运算超出最大限制')
    except TypeError:
        print('对类型无效的操作')
    except ValueError:
        print('ValueError 传入无效的参数')
    except Exception as e:
        print(e)
        print('你输入的参数有误')

def apply():
    base_str = string.ascii_letters + string.digits
    old_set1 = create_set(int, (1,100), 10)
    select_set(old_set1, int, (2,50))
    old_set2 = create_set(float, (100, 200), 20)
    select_set(old_set2, float, (100, 500))
    old_set3 = create_set(str, base_str, 50,10)
    select_set(old_set3, str, 'a')

apply()