'''
purpose: generate and screen some random elements(mongodb implemented)
description: This program generates some random elements, puts them into a database and selects some elements by the
find method of pymongo package with screening condition embedded into it.
Author: Yang Hao
'''


import string
import random
import pymongo


class Elem:                                                    #把生成随机元素的各种属性封装到elem类中
    def __init__(self, data_type, num, domain, str_len = 8):   #domain为生成随机元素的取值范围
        self.data_type = data_type
        self.num = num
        self.domain = domain
        self.str_len = str_len
        self.collection = set()


class UndefinedDataType(Exception):                           #定义一个异常类，实现对rand_generate（）中未定义的数据类型的异常处理
    def __init__(self, undefined):
        self.undefined = undefined


class InvalidCondition(Exception):                           #定义一个异常类，实现对rand_generate（）中筛选条件不合法的异常处理
    def __init__(self, cond):
        self.cond = cond


myclient = pymongo.MongoClient('mongodb://localhost:27017/')  #创建数据库
mydb = myclient["random_db"]
mycol_num = mydb["random_collection_num"]
mycol_string = mydb["random_collection_string"]


def rand_generate(elem):
    try:
        if elem.data_type is int:
            for i in range(elem.num):
                temp = random.randint(elem.domain[0], elem.domain[1])
                row = {"value": temp}
                mycol_num.insert_one(row)
            print('given set is ', end='')
            for i in mycol_num.find():
                print(i, end='')
        elif elem.data_type is float:
            for i in range(elem.num):
                temp = random.uniform(elem.domain[0], elem.domain[1])
                row = {"value": temp}
                mycol_num.insert_one(row)
            print('given set is ', end='')
            for i in mycol_num.find():
                print(i, end='')
        elif elem.data_type is str:
            for i in range(elem.num):
                temp = "".join(random.sample(elem.domain, elem.str_len))
                row = {"value": temp}
                mycol_string.insert_one(row)
            print('given set is ', end='')
            for i in mycol_string.find():
                print(i, end='')
        else:
            elem.data_type = str(elem.data_type)
            raise UndefinedDataType(elem.data_type)                         #抛出未定义的数据类型的异常
    except UndefinedDataType:                                               #处理未定义的数据类型的异常
        print('Type ' + elem.data_type + ' is not defined in rand_generate')
    except NameError:
        print('NameError occurred in rand_generate')
    except TypeError:
        print('TypeError occurred in rand_generate')
    except ValueError:
        print('ValueError occurred in rand_generate')
    except SyntaxError:
        print('SyntaxError occurred in rand_generate')
    except:
        print('Other type of error occurred in rand_generate')


def screening(elem, cond):
    try:
        result = dict()
        if elem.data_type is int or elem.data_type is float:            # 合并float与int的情况
            if type(cond) is list:                                      # 筛选条件的类型合法
                if cond[0] <= cond[1]:                                  # 筛选条件的上下界大小关系合法
                     myquery = {"value":{"$gte": cond[0], "$lte": cond[1]}}
                     result = mycol_num.find(myquery)                   # 在mycol中筛选符合条件数据并放入result中
                else:                                                   # 筛选条件的上下界大小关系不合法
                    cond = str(cond)
                    raise InvalidCondition(cond)
            else:                                                       # 筛选条件的类型不合法
                cond = str(cond)
                raise InvalidCondition(cond)
        else:
            if type(cond) is str:                                       # 筛选条件的类型合法
                myquery = {"$contains":{"value":cond}}
                result = mycol_string.find(myquery)                     # 在mycol中筛选符合条件数据并放入result中
            else:                                                       # 筛选条件的类型不合法
                cond = str(cond)
                raise InvalidCondition(cond)
    except InvalidCondition:
        print('Condition ' + cond + ' is invalid in screening')
    except NameError:
        print('NameError occurred in screening')
    except TypeError:
        print('TypeError occurred in screening')
    except ValueError:
        print('ValueError occurred in screening')
    except SyntaxError:
        print('SyntaxError occurred in screening')
    except:
        print('Other type of error occurred in screening')
    else:
        return result


#test case 1: 选出包含s的字符串
x = Elem(str, 100, string.ascii_letters)
r1 = screening(x, 's')
print('screened set is', r1)


#test case 2: 选出10到20之间的数
y = Elem(int, 100, [0, 100])
r2 = screening(y, [10, 20])
print('screened set is', r2)




