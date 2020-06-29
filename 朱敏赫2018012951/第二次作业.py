"""
  Author:  zhu min he
  Created: 28/6/2020
"""
import string
import random

def dataSampling(func):
    def wrapper(datatype, datarange, num, *args, strlen=6):
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
            return func(result,*args)
        except TypeError:
            print("数据类型不符")
        except NameError:
            print("数据类型错误")
        except:
            raise Exception
    return wrapper
@dataSampling
def dataScreening(data, *args):
    try:
        result = set()
        for item in data:
            if isinstance(item, int):
                it = iter(args)
                if item >= next(it) >= item:
                    result.add(item)
            elif isinstance(item, float):
                it = iter(args)
                if item >= next(it) >= item:
                    result.add(item)
            elif isinstance(item, str):
                for x in args:
                    if x in item:
                        result.add(item)
    except TypeError:
        print("数据类型不符")
    except:
        raise Exception
    else:
        print(result)
#int
print('int:')
dataScreening(int,[0,100],50,20,40)
#float
print('float:')
dataScreening(float,[0,200],50,30,50)
#string
print('string:')
dataScreening(str, string.ascii_letters + string.digits, 2000,'ab', 'aab','abcdef')

