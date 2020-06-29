'''
Description:Using generator to modify random number generation process,
            and can use random number filter function to filter data
parameter:datarange
parameter:datatype
parameter:num
author:li tong
'''
import random
import string
from collections.abc import Iterable
class typeException(Exception):
    pass
class rangeException(Exception):
    pass

def dataSampling(datatype,datarange,num,strlen=10,**kwargs):
    result = set()
    try:

        if(isinstance(datarange,Iterable)==0):
            raise rangeException("datarange不可迭代")
        if datatype is int:
            for index in range(1, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            for index in range(1, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            for index in range(1, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
        else:
            raise typeException("datatype不可识别")

    except typeException as e:
        print(e)
    except rangeException as e:
        print(e)

def dataScreen(data,*args):
    result=set()
    try:
        if(isinstance(data, Iterable) == 0):
            raise Exception("data不可迭代")
        n=len(args)

        if(n==1 and isinstance(args[0],str)):
            for index in data:
                if index.find(args[0]) >= 0:
                    result.add(index)
        elif(n==2 and isinstance(args[0],int) and isinstance(args[1],int)):
            for index in data:
                if(index>=args[0] and index<=args[1]):
                    result.add(index)
        elif (n == 2 and isinstance(args[0], float) and isinstance(args[1], float)):
            for index in data:
                if (index >= args[0] and index <= args[1]):
                    result.add(index)
        else:
            raise Exception("args个数错误")
    except Exception as e:
        print(e)
    finally:
        return result

def main():
    result=set()
    i=dataSampling(int,(10,100),100)
    f=dataSampling(float,(10.0,50.0),100)
    s=dataSampling(str,string.ascii_letters+string.digits,15,8)
    n=input("将输出前n个整型变量")
    n=int(n)
    j=0
    while j<n:
        temp = next(i)
        result.add(temp)
        print(temp)
        j=j+1
    re=dataScreen(result,30,50)
    print("这",n,"个整型变量符合要求的有:",re)

    m = input("将输出前m个浮点型变量")
    m = int(m)
    result = set()
    j = 0
    while j < m:
        temp = next(f)
        result.add(temp)
        print(temp)
        j = j + 1
    re = dataScreen(result,30.0,50.0)
    print("这", m, "个浮点型变量符合要求的有:", re)

    k = input("将输出前k个字符串")
    k = int(k)
    result = set()
    j = 0
    while j < k:
        temp = next(s)
        result.add(temp)
        print(temp)
        j = j + 1
    re = dataScreen(result,'w')
    print("这", k, "个字符串符合要求的有:", re)



if __name__ == "__main__":
    main()
