#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/20 22:09   Linyf      1.0         None
'''
import databaseSamplingAndScreening
import getSamplingGraph

ans=databaseSamplingAndScreening.databaseSamplingAndScreening(totInt = 2000,totFloat = 2000,totStr = 1000,conditionInt = [10,70], conditionFloat = [50,70],conditionStr = 'at')
print(ans)
'''
图中有超出统计范围部分，是因为产生的数字恰好为上限
该统计图只显示整数和浮点数的统计结果
'''
getSamplingGraph.SamplingGraph(ans)



