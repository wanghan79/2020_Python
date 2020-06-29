#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   randomElementGenerator.py    
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/19 16:56   Linyf      1.0         None
'''
import string
import dataScreening
import Factory
class generator:
    def __init__(self,eleType,condition,len=6):
        self.eleType=eleType
        self.condition=condition
        self.len=len

    def generator(self):
        '''
        :return:产生一个符合要求的随机整数，浮点数，或字符串
        '''
        if self.eleType is int:
            factory=Factory.elementSamplingFactory(self.condition,1)
            while 1:
                ele=factory.randomIntSampling()
                for x in ele:
                    yield x

        if self.eleType is float:
            factory=Factory.elementSamplingFactory(self.condition,1)
            while 1:
                ele=factory.randomFloatSampling()
                for x in ele:
                    yield x
        if self.eleType is str:
            factory=Factory.elementSamplingFactory(self.condition,1,self.len)
            while 1:
                ele=factory.randomStrSampling()
                for x in ele:
                    yield x
