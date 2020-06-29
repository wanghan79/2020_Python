"""
Author:  liguangze 李广泽 2018013026
Create：2020/6/26
"""
import random
import string

def dataSampling(datatype,datarange,num,strlen=10):
    try:
        result1 = list()
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result1.append(item)
                continue
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result1.append(item)
                continue
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result1.append(item)
                continue
        else:
            for index in range(0, num):
                continue
        return result1

    except RuntimeError:
        print('请尝试少输入一些数据')
    except TypeError:
        print('目前没有办法处理这种类型')
    finally:
        print('随机数生成完成')


def dataScreening(data, *args):
    try:
        result2 = list()
        if data is int:
            if args is 1:
                result2 = data
            if args is 0:
                result2 = 'flase'
        elif data is float:
            if args is 1:
                result2 = data
            if args is 0:
                result2 = 'flase'
        elif data is str:
            if args is 1:
                result2 = data
            if args is 0:
                result2 = 'flase'
        else:
            pass

        return result2

    except RuntimeError:
        print('请尝试少输入一些数据')
    except TypeError:
        print('目前没有办法处理这种类型')
    finally:
        print('数据筛选完成')


def apply():
    result1 = dataSampling(str, string.ascii_letters+string.digits+"@#$!&*^%+-/=?", 5)
    result2 = dataScreening('K5pTyBh5fT', 1)#这里的1只是为了测试所用的值，在实际使用过程中要根据相应的筛选条件改变此值和dataScreening中的函数
    print(result1)
    print(result2)

apply()