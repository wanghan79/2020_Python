##!/usr/bin/python3
"""
  Author:  QingAnLang
  Purpose: Generate random data set.
  Created: 25/6/2020
"""
import random
import string
import pymongo

def dataSampling(datatype, datarange, num, strlen=15):#固定参数；可变参数 *args；默认参数strlen；关键字参数 **kwargs
    '''
    :Description: Generate a given condition random data set.
    :param datatype: int ，float ,str
    :param datarange: rand
    :param num: number
    :param strlen:
    :return: a dataset
    '''
    result = set()#输出
    try:
        if datatype is int:
            while len(result) != num:
                it = iter(datarange)  # 顺序型可迭代的数据变量，迭代器
                item = random.randint(next(it), next(it))  # next全局函数
                result.add(item)
        elif datatype is float:
            while len(result) != num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) != num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return result

    except TypeError:
        print('数据类型无效操作')
    except ValueError:
        print('参数具有无效值')
    except NameError:
        print('变量名称错误')
    except StopIteration:
        print('迭代器的next()方法没有指向任何对象')
    except OverflowError:
        print('内存不够')
    else:
        print('no error')
    # finally:
    #     print('-'*100)
    #     raise: #返回外部访问者

def apply():#定义应用函数
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")    # 创建一个对象
        mydb = myclient["runoobdb"]                                     # 创建一个数据库
        dblist = myclient.list_database_names()                         # 判断数据库是否存在
        if "runoobdb" in dblist:
            print("数据库已存在！")
        mycol = mydb["sites"]                                           # 创建一个集合
        collist = mydb.list_collection_names()                          # 判断集合是否存在
        # collist = mydb.collection_names()
        if "sites" in collist:                                          # 判断 sites 集合是否存在
            print("集合已存在！")
        #int类型
        print("int型")
        print("生成10个在0-100之间的整数")
        result = dataSampling(int, (1, 100), 10)                        #生成整型随机数
        j = 1
        for i in result:                                                #插入数据
            mycol.insert_one({"number":j,"data":i})
            j = j+1
        for x in mycol.find():                                          # 输出集合中所有数据
            print(x)
        myquery = {"data": {"$gt": 40,"$lt":60}}                        #查询数据
        mydoc = mycol.find(myquery)
        print("筛选在40-60之间的整数")
        for x in mydoc:
            print(x)
        x = mycol.delete_many({})                                       #删除数据
        #float型
        print("float型")
        print("生成10个在0-100之间的浮点数")
        result = dataSampling(float, (1, 100), 10)                        # 生成浮点型随机数
        j = 1
        for i in result:                                                # 插入数据
            mycol.insert_one({"number": j, "data": i})
            j = j + 1
        for x in mycol.find():                                          # 输出集合中所有数据
            print(x)
        myquery = {"data": {"$gt": 40, "$lt": 60}}                      # 查询数据
        mydoc = mycol.find(myquery)
        print("筛选在40-60之间的浮点数")
        for x in mydoc:
            print(x)
        x = mycol.delete_many({})                                       # 删除数据
        #字符串
        print("字符串")
        print("生成10个长度为15的字符串")
        result = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
        j = 1
        for i in result:                                                # 插入数据
            mycol.insert_one({"number": j, "data": i})
            j = j + 1
        for x in mycol.find():                                          # 输出集合中所有数据
            print(x)
        myquery = {"data": {"$regex": "s"}}                             # 查询数据
        mydoc = mycol.find(myquery)
        print("筛选含有s的字符串")
        for x in mydoc:
            print(x)
        x = mycol.delete_many({})                                       # 删除数据
    except ValueError:
        print('参数具有无效值')
    except NameError:
        print('变量名称错误')
    except TypeError:
        print('数据类型无效操作')
apply()