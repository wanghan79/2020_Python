#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SamplingAndScreeningFactory.py    
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/19 17:47   Linyf      1.0         None
'''
import randomElementGenerator
import dataScreening


class SamplingAndScreeningFactory:
    def __init__(self,intNum,samplingConditionInt,scrreningconditionInt,floatNum,samlingConditionFloat,screeningconditionFloat,strNum,samlingConditionStr,screeningConditionStr,strlen=6):
        '''
        :param intNum:产生整数随机数的个数
        :param samplingConditionInt: 整数随机数生成范围
        :param scrreningconditionInt: 整数随机数筛选范围
        :param floatNum: 产生浮点数的个数
        :param samlingConditionFloat:浮点数的生成范围
        :param screeningconditionFloat:浮点数的筛选范围
        :param strNum:产生字符串的个数
        :param samlingConditionStr:字符串的生成范围
        :param screeningConditionStr:字符串的筛选子字符串
        :param strlen:生成字符串长度
        '''
        self.scrreningconditionInt=scrreningconditionInt
        self.samlingConditionInt=samplingConditionInt
        self.screeningconditionFloat=screeningconditionFloat
        self.samlingConditionFloat=samlingConditionFloat
        self.screeningConditionStr=screeningConditionStr
        self.samlingConditionStr=samlingConditionStr
        self.strlen=strlen
        self.intNum=intNum
        self.floatNum=floatNum
        self.strNum=strNum

    def SamplingAndScreening(self):
        '''
        :return: 完成数据生成与筛选后的生成的列表
        '''
        retInt=randomElementGenerator.generator(int,self.samlingConditionInt)
        retFloat=randomElementGenerator.generator(float,self.samlingConditionFloat)
        retStr=randomElementGenerator.generator(str,self.samlingConditionStr,self.strlen)

        ans=list()
        cnt=0;

        while cnt != self.intNum:
            ele = retInt.generator().__next__()
            cnt = cnt + 1
            screening = dataScreening.dataScreening(ele,self.scrreningconditionInt)
            if screening.screeningInt():
                ans.append(ele)

        cnt = 0
        while cnt != self.floatNum:
            ele = retFloat.generator().__next__()
            cnt = cnt + 1
            screening = dataScreening.dataScreening(ele, self.screeningconditionFloat)
            if screening.screeningFloat():
                ans.append(ele)

        cnt = 0
        while cnt != self.strNum:
            ele = retStr.generator().__next__()
            cnt = cnt + 1
            screening = dataScreening.dataScreening(ele, self.screeningConditionStr)
            if screening.screeningStr():
                ans.append(ele)
        return ans

