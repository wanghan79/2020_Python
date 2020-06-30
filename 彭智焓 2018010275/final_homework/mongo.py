#!/usr/bin/env python
'''
@name    :   Random_mongo
@Contact :   pengzhihan666@gmail.com
@Created Time      @Author    @Sno
------------      -------    ----------
2020/6/26         ZH.Peng    2018010275
'''
from Random_gener import Random_gener
from Random_screen import Random_screen
import pymongo
class mongo(object):
    def __init__(self, client="mongodb://localhost:27017/", db="randomEleDB", col="randomEletuple"):
        '''
         The default value can be selected during database initialization

         Areas for improvement: self.dic = {int: "int", float: "float", str: "str"}
        '''
        self.client = client
        self.db = db
        self.col = col
        self.myclient = pymongo.MongoClient(client)
        self.mydb = self.myclient[db]
        self.mycol = self.mydb[col]
        self.dic = {int: "int", float: "float", str: "str"}#  To quickly convert keywords to string types

    def input(self, data, datatype):
        '''
        The iteratable type of stored data is transformed into an iteratable object,
        which is added to the database according to the data type by traversing
        '''
        temp = iter(data)
        while True:
            try:
                item = next(temp)
            except StopIteration:
                break
            numberlist = {"datatype": self.dic[datatype], "content": item}
            self.mycol.insert_one(numberlist)

    def get_Data(self, datatype, datarange, num, strlen=8):
        '''
        Use decorator to generate random data,
        and then add it into database with set type input Get_data()
        '''
        @Random_gener(datatype, datarange, num, strlen)
        def Get_data(data):
            self.input(data, datatype)
        Get_data()

    def screen_Data(self, datatype, *args):
        '''
        Using decorator to filter the values in the database,
        and then return to the Screen_data with the type of set,
        then delete the original records with 'datatype',
        and then add the filtered data to the database
        '''
        print(args)
        @Random_screen(self.client, self.db, self.col, datatype, args[0])
        def Screen_data(ans):
            self.mycol.delete_many({"datatype": self.dic[datatype]})
            self.input(ans, datatype)
        Screen_data()

    def delete_mycol(self):
        '''
        delete mycol.
        '''
        self.mycol.delete_many({})

    def find_many(self):
        '''
        Query all entries in the database
        '''
        for x in self.mycol.find():
            print(x)
