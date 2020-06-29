from code1 import *

def random_decimal_decorator(func):
    def wrapper(*args,**kwargs):
        lst=random_decimal()
        return func(lst,*args,**kwargs)
    return wrapper

def random_int_decorator(func):
    def wrapper(*args,**kwargs):
        lst=random_int(0,50)
        return func(lst,*args,**kwargs)
    return wrapper

def random_range_decorator(func):
    def wrapper(*args,**kwargs):
        lst=random_range(0,50,3)
        return func(lst,*args,**kwargs)
    return wrapper

@random_range_decorator
def filter_odd(sequence):
    if not isinstance(sequence,Iterable):
        raise TypeError('sequence 不可迭代')
    res = []
    for n in sequence:
        if n % 2 != 0:
            res.append(n)
    return res

@random_int_decorator
def filter_k_multiple(sequence,k):
    if not isinstance(sequence,Iterable):
        raise TypeError('sequence 不可迭代')
    if not isinstance(k,int) or isinstance(k,float):
        raise TypeError('k的参数类型错误')
    res=[]
    for n in sequence:
        if n%k==0:
            res.append(n)
    return res

@random_decimal_decorator
def filter_range(sequence,start,end):
    if not isinstance(sequence, Iterable):
        raise TypeError('sequence 不可迭代')
    if not (isinstance(start, float) or isinstance(start, int)) or not (isinstance(end, float) or isinstance(end, int)):
        raise TypeError('范围起始或终止参数类型不正确')
    if end<=start:
        raise Exception('所给范围不正确')
    res = []
    for n in sequence:
        if start<=n <end:
            res.append(n)
    return res

if __name__ == '__main__':
    res1=filter_odd()
    res2=filter_k_multiple(3)
    res3=filter_range(0.2,0.6)
    print(res1)
    print(res2)
    print(res3)


