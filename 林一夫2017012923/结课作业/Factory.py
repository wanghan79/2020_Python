#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Factory.py
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18 20:30   Linyf      1.0         None
'''
import random
import string
import sys

def isLegalNumList(dataRange):
    '''
    :param dataRange:数据范围
    :return: 是否合法
    '''
    if type(dataRange) is not list:
        raise Exception("DataRange must be a list.")
    if len(dataRange)!=2:
        raise Exception("The len of dataRange must be two.")

    it = iter(dataRange);
    x = next(it);
    y = next(it);

    if x>=y:
        raise Exception("The second number must larger than the first number")

def isLegalStrList(dataRange,len):
    '''
    :param dataRange: 数据范围
    :param len: 字符串长度
    :return: 是否合法
    '''
    if len<=0:
        raise Exception("len muat larger than zero")

class elementSamplingFactory:
    def __init__(self,dataRange,tot,len=6):
        '''
        :param dataRange:数据范围
        :param tot: 数据量
        :param len: 若生成字符串，字符串长度
        '''
        self.randomSampling=[]
        self.dataRange=dataRange
        self.tot=tot
        self.len=len

    def randomIntSampling(self):
        '''
        :return: 生成数据
        '''
        try:
            isLegalNumList(self.dataRange)
        except Exception as err:
            print("An exception happened: "+str(err))
            sys.exit()

        self.randomSampling=[]
        while len(self.randomSampling) !=self.tot:
            it=iter(self.dataRange)
            item = random.randint(next(it), next(it))
            self.randomSampling.append(item)

        return self.randomSampling

    def randomFloatSampling(self):
        '''
        :return: 生成数据
        '''
        try:
            isLegalNumList(self.dataRange)
        except Exception as err:
            print("An exception happened: " + str(err))
            sys.exit()

        self.randomSampling=[]
        while len(self.randomSampling) !=self.tot:
            it=iter(self.dataRange)
            item = random.uniform(next(it), next(it))
            self.randomSampling.append(item)

        return self.randomSampling

    def randomStrSampling(self):
        '''
        :return: 生成数据
        '''
        try:
            isLegalStrList(self.dataRange,self.tot)
        except Exception as err:
            print("An exception happened: " + str(err))
            sys.exit()

        self.randomSampling=[]
        while len(self.randomSampling) !=self.tot:
            item = ''.join(random.SystemRandom().choice(self.dataRange) for _ in range(self.len))
            self.randomSampling.append(item)

        return self.randomSampling
