#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   getSamplingGraph.py
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/22 21:43   Linyf      1.0         None
'''
import matplotlib.pyplot as plt

def SamplingGraph(SamplingList):
    '''
    :param SamplingList:筛选的随机数列表
    :return: 显示统计图
    '''
    tot = []
    totInt = []
    totFloat = []
    cnt = 0
    while cnt != 20:
        tot.append(0)
        totInt.append(0)
        totFloat.append(0)
        cnt = cnt + 1


    for i in SamplingList:
        if type(i) is int or type(i) is float:
            tot[int(i / 5)] = tot[int(i / 5)] + 1
        if type(i) is int:
            totInt[int(i / 5)] = totInt[int(i / 5)] + 1
        if type(i) is float:
            totFloat[int(i / 5)] = totFloat[int(i / 5)] + 1
    plt.figure()

    plt.subplot(2,2,1)
    plt.bar(range(20), tot, align='center', color='steelblue', alpha=0.8)
    plt.ylabel('tot')
    plt.title('Screening Random number statistics')
    plt.xticks(range(20),
               ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60',
                '60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-95', '95-100'], rotation=60)
    plt.ylim([0, 300])
    for x, y in enumerate(tot):
        plt.text(x, y + 5, '%s' % round(y, 1), ha='center')
    plt.plot()

    plt.subplot(2,2,2)
    plt.bar(range(20), totInt, align='center', color='red', alpha=0.8)
    plt.ylabel('tot')
    plt.title('Screening Random Int number statistics')
    plt.xticks(range(20),
               ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60',
                '60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-95', '95-100'], rotation=60)
    plt.ylim([0, 300])
    for x, y in enumerate(totInt):
        plt.text(x, y + 5, '%s' % round(y, 1), ha='center')
    plt.plot()

    plt.subplot(2,2,3)
    plt.bar(range(20), totFloat, align='center', color='orange', alpha=0.8)
    plt.ylabel('tot')
    plt.title('Screening Random Float number statistics')
    plt.xticks(range(20),
               ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60',
                '60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-95', '95-100'], rotation=60)
    plt.ylim([0, 300])
    for x, y in enumerate(totFloat):
        plt.text(x, y + 5, '%s' % round(y, 1), ha='center')
    plt.plot()

    plt.show()