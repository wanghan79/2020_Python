#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   liny051@nenu.edu.cn
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/19 18:07   Linyf      1.0         None
'''
import string

import SamplingAndScreeningFactory

ans=SamplingAndScreeningFactory.SamplingAndScreeningFactory(10000,[0,100],[10,30],10000,[0,100],[10,30],10000,string.ascii_letters,'at',8).SamplingAndScreening()
print(ans)

