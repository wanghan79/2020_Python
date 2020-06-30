"""
Author:Guojr
Purpose:random data
Time:1/5/2020
"""
import random
import string

def dataSampling(datatype,datarange,num,strlen=6):
    result = set()
    for index in range(0,num):
        if datatype is float:
            it = iter(datarange)
            item=random.uniform(next(it),next(it))
            result.add(item)
            continue
        elif datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item=''.join(random.SystemRandom().choice(datarange)for _ in range(3))
            result.add(item)
        else:
            continue
    return result
def dataScreening(data,*args):
    Array=set()
    try:
        for j in data:
            it=iter(args)
            if type(j)is int and next(it)<=j<=next(it):
                Array.add(j)
            if type(j)is float and next(it)<=j<=next(it):
                Array.add(j)
            if type(j) is str and next(it) in j:
                Array.add(j)
    except ValueError:
        print("参数有误")
    except TypeError:
        print("类型有误")
    except Exception as e:
        print(e)
    return Array
def apply():
    result1=dataSampling(int,[1,100],100)
    print(result1)
    r1_screening = dataScreening(result1, 20, 60)
    print(r1_screening)
    result2=dataSampling(float,[1,100],50)
    print(result2)
    r2_screening = dataScreening(result2, 80, 100)
    print(r2_screening)
    result3=dataSampling(str,"abcdefg",5)
    print(result3)
    r3_screening = dataScreening(result3, "ab")
    print(r3_screening)
apply()