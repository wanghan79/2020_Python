# !/usr/bin/python3
"""
  Author:  Ty.Gu
  Purpose: decorator & random data set.
  Created: 27/5/2020
"""
import random
import string

def create_set(func):
    def wrapper(datatype, datarange, num, choice=None,strlen=8):
        old_set = set()
        try:
            if datatype is int:
                for i in range(0, num):
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    old_set.add(item)
                    continue

            elif datatype is float:
                for i in range(0, num):
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    old_set.add(item)
                    continue

            elif datatype is str:
                for i in range(0, num):
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    old_set.add(item)
                    continue
            #print(old_set)
            return func(old_set,datatype,choice)
        except OverflowError:
            print('数值运算超出最大限制')
        except TypeError:
            print('对类型无效的操作')
        except ValueError:
            print('ValueError 传入无效的参数')
        except Exception as e:
            print(e)
            print('你输入的参数有误')
    return wrapper

@create_set
def select_set(old_set, datatype, datarange):
    new_set = set()
    try:
        for x in old_set:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_set.add(x)
                continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    new_set.add(x)
                continue

            elif datatype is str:
                if x.find(datarange) != -1:
                    new_set.add(x)
                continue
        return new_set
    except OverflowError:
        print('数值运算超出最大限制')
    except TypeError:
        print('对类型无效的操作')
    except ValueError:
        print('ValueError 传入无效的参数')
    except Exception as e:
        print(e)
        print('你输入的参数有误')

base_str = string.ascii_letters + string.digits
new_set1 = select_set(int, (1,100),20,(20,50))
print(new_set1)
new_set2 = select_set(float, (100, 500),30,(200,300))
print(new_set2)
new_set3 = select_set(str,base_str,30, 'a',10)
print(new_set3)


