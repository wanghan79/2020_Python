"""
姓名：李嘉源 学号：2018012525
项目实践结课作业  Generate random data set with MongoDB.
"""


import random
from pymongo import MongoClient
#生成随机数
def dataSampling(type,min,max,N):
    if N<=0:

        print('please input the correect N(>0)')
    else:
        if type in ['int','float']:
            if max>min:
                if type=='int':

                    i = 0
                    L = []
                    while i < N:
                        elem = random.randint(min, max)
                        L.append(elem)
                        i = i + 1
                if type=='float':

                    i = 0
                    L = []
                    while i < N:
                        elem = random.uniform(min, max)
                        L.append(elem)
                        i = i + 1
                return L
            else:
                print('min max error')
        else:
            print('type error')

#定义连接mongdb的类
class MongodbModel:
    def __init__(self):
        """
        初始化MongoClient
        """
        self.client = MongoClient()
        # 指定端口和地址
        # self.client = MongoClient('127.0.0.1', 27017)
        self.client = MongoClient('mongodb://120.77.12.144:27017/')
        self.client.admin.authenticate("root", "123456")
        self.db = self.client['myTest']

    def __del__(self):
        """
        删除对象(del mgngomodel_obj)
        """
        self.client.close()


def apply():
    print('test   on  int ')
    test1 = dataSampling('int', 0, 100, 50)
    print('随机生成10个 0 到100 的数字')
    print(test1)


    MGbase=MongodbModel()

    mytab=MGbase['MyTestCollection']

    #插入到数据库中
    for elem in test1:
        mytab.insert_one({'data':elem,'type':type(elem)})


    print('打印数据。。。')
    for elem  in mytab.find():
        print(elem)


    print('使用数据库中的过滤筛选功能')
    #筛选 大于 50  小于100 的数据
    for elem in mytab.find({'data':{"$gte":50,"$lte":100}}):
        print(elem)

if __name__ == '__main__':
    apply()



