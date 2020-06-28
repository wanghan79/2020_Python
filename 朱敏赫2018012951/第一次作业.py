"""
  Author:  zhu min he 
  Purpose: Data Sampling and Screening
  Created: 24/6/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=6):

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
        else:
            return result

def dataScreening(data,*args):
    try:
        result = set()
        for item in data:
            num = 0
            for arg in args:
                if (eval(arg)):
                    num = num + 1
                if num == len(args):
                    result.add(item)
    except NameError:
        print("变量名称错误")
    except ValueError:
        print("无效参数")
    except TypeError:
        print("对类型无效操作")
    else:
        return result


def apply():
    #int
    print("int:")
    result01 = dataSampling(int,[0,100],50)
    dataScreening(result01, 10, 50)
    #float
    print("float:")
    result02 = dataSampling(float, [0,100],50)
    dataScreening(result02, 10 ,50)
    #string
    print("str:")
    result03 = dataSampling(string.ascii_letters + string.digits, 1000, 10)
    dataScreening(result03,'ab', 'aab', 'abcd')
apply()

