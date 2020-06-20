import random
from collections import Iterable

def random_decimal(start=0,end=1,num=10):
    """
    生成 [start,end)范围内的一个随机小数列表
    :param start:
    :param end:
    :param num:
    :return: a list of float num
    """
    if not (isinstance(start,float) or isinstance(start,int)) or not (isinstance(end,float) or isinstance(end,int)):
        raise TypeError('范围起始或终止参数类型不正确')
    if end<=start:
        raise Exception('所给范围不正确')
    res=[]
    for _ in range(num):
        n=random.random()
        y=(end-start)*n+start
        res.append(y)
    return res

def random_int(start,end,num=10):
    """
    生成 [start,end)范围内的一个随机整数列表
    :param start:
    :param end:
    :param num:
    :return: a list of int num
    """
    if not isinstance(start,int) or not isinstance(end,int):
        raise TypeError('范围起始或终止参数类型不正确')
    if end<=start:
        raise Exception('所给范围不正确')
    res=[]
    for _ in range(num):
        n = random.random()
        y = (end - start) * n + start
        res.append(int(y))
    return res

def random_range(start,end,gap=1,num=10):
    """
    生成 [start,end) 范围内gap间隔的一个随机整数列表
    :param start:
    :param end:
    :param gap:
    :param num:
    :return:a list of int num
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError('范围起始或终止参数类型不正确')
    if end <= start:
        raise Exception('所给范围不正确')
    length=int(round((end-start)/gap))
    res=[]
    for _ in range(num):
        n = int(random.random()*length)
        res.append(start+n*gap)
    return res

def filter_odd(sequence):
    """
    从随机数列中筛选出奇数
    :param sequence:
    :return: a list
    """
    if not isinstance(sequence,Iterable):
        raise TypeError('sequence 不可迭代')
    res = []
    for n in sequence:
        if n % 2 != 0:
            res.append(n)
    return res


def filter_k_multiple(sequence,k):
    """
    从随机数列中筛选出 k 的整数倍的数
    :param sequence:
    :param k:
    :return: a list
    """
    if not isinstance(sequence,Iterable):
        raise TypeError('sequence 不可迭代')
    if not isinstance(k,int) or isinstance(k,float):
        raise TypeError('k的参数类型错误')
    res=[]
    for n in sequence:
        if n%k==0:
            res.append(n)
    return res

def filter_range(sequence,start,end):
    """
    将[start,end)范围内的数筛选出来
    :param sequence:
    :param start:
    :param end:
    :return: a list
    """
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
    lst1=random_decimal()
    lst2=random_int(0,20)
    lst3= random_range(0,50,2)
    print(lst1)
    print(lst2)
    print(lst3)
    res1=filter_odd(lst2)
    res2=filter_k_multiple(lst2,3)
    res3=filter_range(lst1,0,0.5)
    print(res1)
    print(res2)
    print(res3)
