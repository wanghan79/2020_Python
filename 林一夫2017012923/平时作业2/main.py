#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18 21:51   Linyf      1.0         None
'''
from dataScreening import dataScreening
from decorateDataSampling import Sampling, randomList

#调用修饰函数
@Sampling
def Screening(needType,condition):
    '''
    :param needType: 要求筛选的数据类型
    :param condition: 筛选的范围
    :return: 包含所需数据的列表
    '''
    ans=list()
    for x in randomList:
        if needType is int and type(x) is int:
            if dataScreening.screeningInt(dataScreening(x, condition)):
                ans.append(x)
        if needType is float and type(x) is float:
            if dataScreening.screeningFloat(dataScreening(x, condition)):
                ans.append(x)
        if needType is str and type(x) is str:
            if dataScreening.screeningStr(dataScreening(x, condition)):
                ans.append(x)
    return ans

ans=Screening(str,'at')
print(ans)