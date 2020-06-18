#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18 20:29   Linyf      1.0         None
'''
import string

from Factory import elementSamplingFactory
from dataScreening import dataScreening

#数据生成
Nf=elementSamplingFactory([0,100],50)
Sf=elementSamplingFactory(string.ascii_letters,1000,8)
result=[]
result.extend(elementSamplingFactory.randomFloatSampling(Nf))
result.extend(elementSamplingFactory.randomIntSampling(Nf))
result.extend(elementSamplingFactory.randomStrSampling(Sf))

#数据筛选
ans=[]
for x in result:
    if type(x) is int:
        if dataScreening.screeningInt(dataScreening(x,[10,30])):
            ans.append(x)
    if type(x) is float:
        if dataScreening.screeningFloat(dataScreening(x,[10,30])):
            ans.append(x)
    if type(x) is str:
        if dataScreening.screeningStr(dataScreening(x,'at')):
            ans.append(x)

#数据打印
print(ans)