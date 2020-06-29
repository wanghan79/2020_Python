#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dataScreening.py
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/18 20:28   Linyf      1.0         None
'''
import sys

def isLegalNumList(condition):
    '''
    :param condition: 筛选条件
    :return: 条件是否合法
    '''
    if type(condition) is not list:
        raise Exception("condition must be a list.")
    if len(condition)!=2:
        raise Exception("The len of dataRange must be two.")

    it = iter(condition);
    x = next(it);
    y = next(it);

    if x>=y:
        raise Exception("The second number must larger than the first number")


class dataScreening:
    def __init__(self,data,conditon):
        '''
        :param data: 筛选对象
        :param conditon: 筛选条件
        '''
        self.data=data
        self.condition=conditon

    def screeningInt(self):
        '''
        :return: int类型对象是否符合筛选条件
        '''
        try:
            isLegalNumList(self.condition)
        except Exception as err:
            print("An exception happened: " + str(err))
            sys.exit()

        it = iter(self.condition)
        lowerBound = next(it)
        upperBound = next(it)
        if self.data >= lowerBound and self.data <= upperBound:
            return True
        else:
            return False

    def screeningFloat(self):
        '''
        :return: Float对象是否符合筛选条件
        '''
        if type(self.data) is float:
            try:
                isLegalNumList(self.condition)
            except Exception as err:
                print("An exception happened: " + str(err))
                sys.exit()

            it = iter(self.condition)
            lowerBound = next(it)
            upperBound = next(it)
            if self.data >= lowerBound and self.data <= upperBound:
                return True
            else:
                return False

    def screeningStr(self):
        '''
        :return: str对象是否符合筛选条件
        '''
        if type(self.data) is str:
            if self.data.find(self.condition)!=-1:
                return True
            else:
                return False







