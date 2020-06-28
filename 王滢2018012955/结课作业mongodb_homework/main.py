##!/usr/bin/python3
"""
Author: Ying Wang
Purpose:
Created:21/6/2020
"""
import pymongo
from create_data import apply

class opr_data():
    def __init__(self):
        # mongodb数据库初始化
        client = pymongo.MongoClient('localhost', 27017)
        # 获得数据库(DB)
        db = client.Test
        # 获得集合(collection)
        self.mongo_collection1 = db.Test_01  # 或者 mongo_collection1 = db['Test_01']

    def save_string_mongodb(self):


        datas = apply()
        datas = list(datas)
        for i in range(len(datas)):
            di = {
                'id':i,
                'name':datas[i]
            }
            self.mongo_collection1.insert_one(di)

    def get_data_from_mongodb(self,key):

        result1 = self.mongo_collection1.find({'key': key})
        for res in result1:
            #print(res)
            print(res['value'])


if __name__ == '__main__':
    o = opr_data()
    o.save_string_mongodb()
    key = input('请输入查找的key值,例如（1，2，3，4）')
    o.get_data_from_mongodb(int(key))