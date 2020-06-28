'''
    Author: Yy.Li
    Purpose:MangoDB is used to store random Numbers and can query data for data filtering
    Created:27/6/2020
'''

import random
import string
import pymongo

def dataSampling(datatype,datarange,num,strlen=8): #固定参数；默认参数
    '''
    :Description:Generate a gievn condition random data set.
    :param datatype:
    :param datarange:iterable data set
    :param num:number
    :param strlen:
    :return:a dataset
    '''
    result = set()
    try:
        if datatype is int:
            while len(result)<num:
                it = iter(datarange) #返回迭代器
                item = random.randint(next(it),next(it))
                result.add(item)
                yield item
                continue

        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)  # 返回迭代器
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield item
                continue

        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                yield item
                continue
        else:
            pass
    except ValueError:
        print("ValueError:传入无效参数")
    except TypeError:
        print("TypeError:对类型无效的参数")
    except Exception as e:
        print("error")
    return result

def apply():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["sq_random"]
    mycol = mydb["set_random"]

    mycol.drop()
    result = dataSampling(str,string.ascii_letters+string.digits+"@#$!",10)
    for i in result:
        mycol.insert_one({"random_data":i})
    new_result_str = set()
    for x in mycol.find():
        new_result_str.add(x['random_data'])
    print(new_result_str)
    num = 0
    new_result = set()
    for i in mycol.find({"random_data":{"$regex":'a'}}):
        new_result.add(i['random_data'])
        num += 1
    if num == 0 :
        print("没有满足条件的数据！")
    else:
        print("筛选后的结果：")
        print(new_result)

    mycol.drop()
    print("\n")
    result = dataSampling(int,(0,100),15)
    for i in result:
        mycol.insert_one({"random_data":i})
    new_result_int = set()
    for x in mycol.find():
        new_result_int.add(x['random_data'])
    print(new_result_int)
    num = 0
    new_result = set()
    for i in mycol.find({"random_data":{"$gte":10,"$lte":30}}):
        new_result.add(i['random_data'])
        num += 1
    if num == 0:
        print("没有满足条件的数据！")
    else:
        print("筛选后的结果：")
        print(new_result)

    mycol.drop()
    print("\n")
    result = dataSampling(float, (0, 100), 15)
    for i in result:
        mycol.insert_one({"random_data":i})
    new_result_float = set()
    for x in mycol.find():
        new_result_float.add(x['random_data'])
    print(new_result_float)
    num = 0
    new_result = set()
    for i in mycol.find({"random_data":{"$gte":10,"$lte":50}}):
        new_result.add(i['random_data'])
        num += 1
    if num == 0:
        print("没有满足条件的数据！")
    else:
        print("筛选后的结果：")
        print(new_result)

apply()