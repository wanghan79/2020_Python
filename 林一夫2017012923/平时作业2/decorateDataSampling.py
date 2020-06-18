#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   decorateDataSampling.py    
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18 21:36   Linyf      1.0         None
'''
import string

from Factory import elementSamplingFactory

randomList=[]

#修饰函数
def Sampling(fn):
    def Sampling(*args,**kwargs):
        global randomList
        Nf = elementSamplingFactory([0, 100], 1000)
        Sf = elementSamplingFactory(string.ascii_letters, 1000, 10)
        randomList.extend(elementSamplingFactory.randomFloatSampling(Nf))
        randomList.extend(elementSamplingFactory.randomIntSampling(Nf))
        randomList.extend(elementSamplingFactory.randomStrSampling(Sf))
        return fn(*args, **kwargs)
    return Sampling


