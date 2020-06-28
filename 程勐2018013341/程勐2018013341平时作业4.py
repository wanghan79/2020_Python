import pymongo
from code3 import *

def save_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test_db"]
    mycol = mydb["random_num"]
    data={}
    lst1 = random_decimal()
    lst2 = random_int(0, 20)
    lst3 = random_range(0, 50, 2)
    data['random_decimal']=list(lst1)
    data['random_int'] = list(lst2)
    data['random_range']=list(lst3)
    mycol.insert_one(data)
    myclient.close()

def filter_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test_db"]
    mycol = mydb["random_num"]
    data=mycol.find_one()
    lst1=data['random_decimal']
    lst2=data['random_int']
    lst3=data['random_range']
    res1 = filter_odd(lst2)
    res2 = filter_k_multiple(lst3, 3)
    res3 = filter_range(lst1, 0, 0.5)
    print(res1)
    print(res2)
    print(res3)
    myclient.close()
    
if __name__ == '__main__':
    save_data()
    filter_data()

