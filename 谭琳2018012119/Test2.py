# python3
"""
  Author:  Tanlin
  Purpose: 作业二：将平时作业1中的随机数生成封装为修饰函数（或修饰类），用于修饰随机数筛选函数进行数据筛选；
  Created: 2020.6.20
"""
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *args, strlen=10):  # 生成
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
        except TypeError:
            print('The data type is error!')
        except ValueError:
            print("The data value is error!")
        except MemoryError:
            print("The data is too much!")
        print("The random data:\n",result)
        return func(result, *args)
    return wrapper

@dataSampling
def dataScreening(data, *args):  # 筛选*args(可变参数)
    try:
        result = set()
        for index in data:
            if type(index) is int or type(index) is float:
                it = iter(args)
                if next(it) <= index <= next(it):
                    result.add(index)
            elif type(index) is str:
                for substr in args:
                    if substr in index:
                        result.add(index)
    except TypeError:
        print("The data type is error!")
    except ValueError:
        print("The data value is error!")
    print("After filtered:\n",result)
    return result

def apply():  # 输出结果
    print("INT:")
    dataScreening(int,[1,100],5,20,80)
    print("FLOAT:")
    dataScreening(float,[1,100],5,20,80)
    print("STR:")
    dataScreening(str,string.ascii_letters + string.digits + string.printable,5,"T")

apply()