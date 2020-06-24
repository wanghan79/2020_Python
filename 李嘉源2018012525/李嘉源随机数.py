"""
姓名：李嘉源 学号：2018012525
项目实践第一次作业  Generate random data set.
"""

import random

def dataSampling(type,min,max,N):
    if N<=0:

        print('please input the correect N(>0)')
    else:
        if type in ['int','float']:
            if max>min:
                if type=='int':

                    i = 0
                    L = []
                    while i < N:
                        elem = random.randint(min, max)
                        L.append(elem)
                        i = i + 1
                if type=='float':

                    i = 0
                    L = []
                    while i < N:
                        elem = random.uniform(min, max)
                        L.append(elem)
                        i = i + 1
                return L
            else:
                print('min max error')
        else:
            print('type error')


def dataScreening(data,flag1,flag2):

    #get type of data

    elem=data[0]
    print('type is {}'.format(type(elem)))

    L=set()
    for elem in data:
        if elem >=flag1 and elem <=flag2 and elem not in L:
            L.add(elem)
    return L


def apply():

    print('test   on  int ')
    test1=dataSampling('int',0,100,50)
    print('随机生成10个 0 到100 的数字')
    print(test1)

    #过滤
    test1 = dataScreening(test1, 50, 60)
    print('筛选50 到 60 区间的数字')
    print(test1)

    print('test   on  float ')
    test2 = dataSampling('float', 0, 100, 50)
    print('随机生成10个 0 到100 的数字')
    print(test2)

    # 过滤
    test1 = dataScreening(test2, 50, 60)
    print('筛选50 到 60 区间的数字')
    print(test2)

apply()