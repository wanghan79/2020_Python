from code1 import *

def random_decimal_generator(start=0,end=1,num=10):
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
    for _ in range(num):
        n=random.random()
        y=(end-start)*n+start
        yield y

def random_int_generator(start,end,num=10):
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
    for _ in range(num):
        n = random.random()
        y = (end - start) * n + start
        yield int(y)

def random_range_generator(start,end,gap=1,num=10):
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
    for _ in range(num):
        n = int(random.random()*length)
        yield start+n*gap
        
if __name__ == '__main__':
    g1=random_decimal()
    g2=random_int(0,20)
    g3= random_range(0,50,2)
    res1=filter_odd(g2)
    res2=filter_k_multiple(g3,3)
    res3=filter_range(g1,0,0.5)
    print(res1)
    print(res2)
    print(res3)
