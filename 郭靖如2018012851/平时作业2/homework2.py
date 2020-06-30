"""
Author:Guojr
Purpose:封装成修饰函数
Time:5/6/2020
"""
import random
import string
def desDataScreening(func):
    def dataScreening(datatype,datarange,num,strlen=6):
        outerArray = func(datatype,datarange,num,strlen=6)
        Array = set()
        try:
            for j in outerArray:
                if type(j) is int and 20 <= j <= 60:
                    Array.add(j)
                if type(j) is float and 80 <= j <= 100:
                    Array.add(j)
                if type(j) is str and "ab" in j:
                    Array.add(j)
        except ValueError:
            print("参数有误")
        except TypeError:
            print("类型有误")
        except Exception as e:
            print(e)
        return Array
    return dataScreening
@desDataScreening
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
def apply():
    result1=dataSampling(int,[1,100],100)
    print(result1)
    result2=dataSampling(float,[1,100],50)
    print(result2)
    result3=dataSampling(str,"abcdefg",100)
    print(result3)
apply()