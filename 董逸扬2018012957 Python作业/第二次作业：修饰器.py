##!/usr/bin/python3
"""
Author:YiYang.Dong
Purpose:Generate random data set
Created:16/5/2020
"""
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *conditions,strlen=6):
                # 固定参数；可变参数 *args；默认参数；关键字参数 **kwargs
        '''
        :Description: Generate a given condition random data set.
        :param datatype: int,float,string...
        :param datarange: iterable data set
        :param num: number of data
        :param strlen: string length
        :return: a function
        '''
        try:
            result = set()
            if datatype is int:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
            elif datatype is float:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
            elif datatype is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
            return func(result, *conditions)
        except NameError:
            print("数据类型错误")
        except TypeError:
            print("数据与数据类型不符")
        except MemoryError:
            print("内存已满")
        except:
            raise Exception
    return wrapper
    #finally:
            #print("请继续在数据采样中生成数据")
@dataSampling
def dataScreening(data, *conditions):
    '''
    :param data: iterable data set
    :param conditions: variable-length argument
    :return: a data set
    '''
    try:
        result = set()
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it) <= item <= next(it):
                    result.add(item)
            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)
    except TypeError:
            print("数据与数据类型不符")
    except:
            raise Exception

    else:
            print("此次数据筛选的结果是")
            print(result)
            print("本次筛选结束，请生成下一组随机数进行筛选吧！")

#int型
print("int型：")
dataScreening(int,[0,150],100,25,45)
#float型
print("float型：")
dataScreening(float,[0,200],50,35,55)
#string型
print("字符串型：")
dataScreening(str, string.ascii_letters + string.digits, 2000,'dy', 'dyy','dyygood')
