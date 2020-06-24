"""

姓名: 周铭辉    学号：2018013134
项目实践结课作业   将作业三中生成的数据放入MongoDB数据库中，并从MongoDB中查询数据进行数据筛选


"""

import random
import string
import pymongo


########################################################################################################################
def dataSampling(datatype,datarange,num,strlen=8):

        if datatype is int:
            for i in range(num):
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                yield  item
        elif datatype is float:
            for i in range(num):
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                yield  item
        elif datatype is str:
            for i in range(num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield  item


########################################################################################################################

def apply():

    # 创建数据库
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["minghuiDB"]

    # 检查'myData'是否存在
    dblist = myclient.list_database_names()
    # dblist = myclient.list_database.names()
    if 'minghuiDB' in dblist:
        print('数据库已存在！')
    print('\n')

    # 创建集合
    mycol = mydb["sites"]
    mycol.drop()

    # 集合插入文档使用insert_one方法，该方法的第一参数是字典name>=value对

    data_int = dataSampling(int, [0, 122], 20)
    data_float = dataSampling(float, [0, 122], 20)
    data_str = dataSampling(str, string.ascii_letters, 20)

    for mydict_int in data_int:
        mycol.insert_one({'data': mydict_int, 'datatype': 'int'})
    for mydict_float in data_float:
        mycol.insert_one({'data': mydict_float, 'datatype': 'float'})
    for mydict_str in data_str:
        mycol.insert_one({'data': mydict_str, 'datatype': 'str'})


    print('数据库中的数据：')
    for x in mycol.find():
        print(x)
    print('\n')
    #########################################################################################

    #MongoDB中使用find来进行查询，通过指定find的第一个参数可以实现全部和部分查询。
    #lt, lte,gt,gte,$ne和<,<=,>,>=,!=是一一对应的，它们可以组合起来以查找一个范围内的值

    print('从数据库中找出22~77之间的int型数据:')
    for i in mycol.find({"data":{"$gte": 22, "$lte": 77}, "datatype": "int"}):
        print(i)
    print('\n')
    ########################
    print('从数据库中找出22~77之间的float型数据:')
    for i in mycol.find({"data":{"$gte": 22, "$lte": 77}, "datatype": "float"}):
        print(i)
    print('\n')
    ########################
    #$regex ：为查询中的模式匹配字符串提供正则表达式功能
    #MongoDB的模糊查询可以使用 $regex运算符通过正则表达式来进行匹配查询
    print('从数据库中找出包含字符“a”的string型数据:')
    for i in mycol.find({"data": {"$regex": 'a'}, "datatype": "str"}):
        print(i)
    print('\n')
    ###########################################################################################

apply()