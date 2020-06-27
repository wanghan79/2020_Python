'''
purpose: generate and screen some random elements(try except implemented)
description: This program generates some elements, puts them into a set and screens some of them in the set by given
conditions. Try and except is used to handle errors.
Author: Yang Hao
'''
import string
import random


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


def rand_generate(elem):
    try:
        if elem.data_type is int:
            for i in range(elem.num):
                elem.collection.add(random.randint(elem.domain[0], elem.domain[1]))
        elif elem.data_type is float:
            for i in range(elem.num):
                elem.collection.add(random.uniform(elem.domain[0], elem.domain[1]))
        elif elem.data_type is str:
            for i in range(elem.num):
                elem.collection.add("".join(random.sample(elem.domain, elem.str_len)))
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
        result = set()
        if elem.data_type is int or elem.data_type is float:            # 合并float与int的情况
            if type(cond) is list:                                      # 筛选条件的类型合法
                for item in elem.collection:
                    if cond[0] <= cond[1]:                              # 筛选条件的上下界大小关系合法
                        if cond[0] <= item <= cond[1]:
                            result.add(item)
                    else:                                               # 筛选条件的上下界大小关系合法
                        cond = str(cond)
                        raise InvalidCondition(cond)
            else:                                                       # 筛选条件的类型不合法
                cond = str(cond)
                raise InvalidCondition(cond)
        else:
            if type(cond) is str:                                       # 筛选条件的类型合法
                for item in elem.collection:
                    if cond in item:
                        result.add(item)
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
rand_generate(x)
print('given set is', x.collection)
r1 = screening(x, 's')
print('screened set is', r1)


#test case 2: 选出10到20之间的数
y = Elem(int, 100, [0, 100])
rand_generate(y)
print('given set is ', y.collection)
r2 = screening(y, [10, 20])
print('screened set is', r2)

#test case 3: 选出0到1之间的浮点数
z = Elem(float, 100, [0, 10])
rand_generate(z)
print('given set is ', z.collection)
r2 = screening(z, [0, 1])
print('screened set is', r2)



