'''
purpose: generate and screen some random elements(generator implemented)
description: This program generates one random element after each yield one by one, and if the element satisfies the
given condition it will be put into the result set. Given set doesn't actually exist as the variable in the program like
the first program, each element of it was printed as soon as the yield produced one element just as the reference to the
result set when checking the output.
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
                yield random.randint(elem.domain[0], elem.domain[1])
        elif elem.data_type is float:
            for i in range(elem.num):
                yield random.uniform(elem.domain[0], elem.domain[1])
        elif elem.data_type is str:
            for i in range(elem.num):
                yield "".join(random.sample(elem.domain, elem.str_len))
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
    '''except:
        print('Other type of error occurred in rand_generate')'''


def screening(elem, cond):
    try:
        result = set()
        if elem.data_type is int or elem.data_type is float:  #合并int和float的筛选的情况，由于只有int与float的筛选条件是list，
            if type(cond) is list:                            #所以可以根据list进行判定
                item = rand_generate(elem)
                print('given set is {', end='')
                for i in range(elem.num):
                    try:
                        temp = next(item)
                        print(temp, end=', ')
                        if cond[0] <= temp <= cond[1]:
                            result.add(temp)
                    except StopIteration:
                        break
                print('}')
            else:
                cond = str(cond)
                raise InvalidCondition(cond)
        else:
            if type(cond) is str:
                item = rand_generate(elem)
                print('given set is {', end='')
                for i in range(elem.num):
                    try:
                        temp = next(item)
                        print(temp, end=', ')
                        if cond in temp:
                            result.add(temp)
                    except StopIteration:
                        break
                print('}')
            else:
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


#test case 3: 选出0到1之间的浮点数
z = Elem(float, 100, [0, 10])
r2 = screening(z, [0, 1])
print('screened set is', r2)
