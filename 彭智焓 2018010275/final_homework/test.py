#!/usr/bin/env python
'''
@name    :   test
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/26         ZH.Peng    2018010275
'''
from mongo import mongo
import string
def test():
    '''
    After connecting to the database, data of type int,
    float and string are first generated and displayed,
    then filtered and displayed, and finally the data
    in the database is deleted
    '''
    zB = mongo()
    zB.get_Data(int, (1, 50), 8)
    zB.get_Data(float, (1, 100), 5, 1)
    zB.get_Data(str, string.ascii_letters + string.digits + "@#$!", 10, 5)
    zB.find_many()
    zB.screen_Data(int, (16, 61))
    zB.screen_Data(float, (3.14, 52.0))
    zB.screen_Data(str, 'a', 'b', 'c')
    zB.find_many()
    zB.delete_mycol()
test()