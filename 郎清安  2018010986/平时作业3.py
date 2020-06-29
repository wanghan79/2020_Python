##!/usr/bin/python3
"""
  Author:  QingAnLang
  Purpose: Generate random data set.
  Created: 15/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=8):#固定参数；可变参数 *args；默认参数strlen；关键字参数 **kwargs
    '''
    :Description: Generate a given condition random data set.
    :param datatype: dddd
    :param datarange: iterable data set
    :param num: number
    :param strlen:
    :return: a dataset
    '''

    try:
        if datatype is int:
            while len(result) != num:
                it = iter(datarange)  # 顺序型可迭代的数据变量，迭代器
                item = random.randint(next(it), next(it))  # next全局函数
                yield item
        elif datatype is float:
            while len(result) != num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            while len(result) != num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item

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
    # finally:
    #     print('-'*100)
    #     raise: #返回外部访问者
def dataScreening(data,*args):
    result = set()
    try:
        for item in data:
            if type(item) is int:
                i = iter(args)
                if next(i) <= item <= next(i):
                    result.add(item)
            elif type(item) is float:
                i = iter(args)
                if next(i) <= item <= next(i):
                    result.add(item)
            elif type(item) is str:
                for i in args:
                    if i in item:
                        result.add(item)
    except ValueError:
        print('参数具有无效值')
    except NameError:
        print('变量名称错误')
    except TypeError:
        print('数据类型无效操作')

    return result

result = set()
a = dataSampling(int,{1,100},10)
while True:
    try:
        result.add(next(a))
    except StopIteration:
        break
print("随机生成10个在0-100之间的整数")
print(result)
result1 = dataScreening(result,40,60)
print("筛选范围在40-60的整数")
print(result1)

result = set()
a = dataSampling(float,{1,100},10)
while True:
    try:
        result.add(next(a))
    except StopIteration:
        break
print("随机生成10个在0-100之内浮点数")
print(result)
result1 = dataScreening(result,40,60)
print("筛选范围在40-60的浮点数")
print(result1)

result = set()
a = dataSampling(str,string.ascii_letters+string.digits,100)
while True:
    try:
        result.add(next(a))
    except StopIteration:
        break
print("随机生成100个长度为8的字符串")
print(result)
result1 = dataScreening(result,'s')
print("筛选含s的字符串")
print(result1)