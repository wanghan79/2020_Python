'''
    Author: Yy.Li
    Purpose:Use the generator to modify the random number generation process
    Created:25/6/2020
'''

import random
import string
def dataSampling(datatype,datarange,num,strlen=8): #固定参数；默认参数
    '''
    :Description:Generate a gievn condition random data set.
    :param datatype:
    :param datarange:iterable data set
    :param num:number
    :param strlen:
    :return:a dataset
    '''
    result = set()
    try:
        if datatype is int:
            while len(result)<num:
                it = iter(datarange) #返回迭代器
                item = random.randint(next(it),next(it))
                result.add(item)
                yield item
                continue

        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)  # 返回迭代器
                item = random.uniform(next(it), next(it))
                result.add(item)
                yield item
                continue

        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                yield item
                continue
        else:
            pass
    except ValueError:
        print("ValueError:传入无效参数")
    except TypeError:
        print("TypeError:对类型无效的参数")
    except Exception as e:
        print("error")
    return result

def dataScreening(data,datatype,datarange):
    new_result = set()
    try:
        for i in data:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= i <=next(it):
                    new_result.add(i)
                    continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= i <=next(it):
                    new_result.add(i)
                    continue

            elif datatype is str:
                if i.find(datarange) != -1:
                    new_result.add(i)
                    continue
            else:
                pass
    except ValueError:
        print("ValueError:传入无效参数")
    except TypeError:
        print("TypeError:对类型无效的参数")
    except Exception as e:
        print("error")
    return new_result

def apply():
    result = dataSampling(str,string.ascii_letters+string.digits+"@#$!",10)
    result2 = set()
    for i in range(0, 10):
        result2.add(next(result))
    print(result2)
    new_result = dataScreening(result2,str,'a')
    print(new_result)

    result = dataSampling(int,(0,100),15)
    result2 = set()
    for i in range(0,15):
        result2.add(next(result))
    print(result2)
    new_result = dataScreening(result2,int,(10,30))
    print(new_result)

    result = dataSampling(float, (0, 100), 15)
    result2 = set()
    for i in range(0, 15):
        result2.add(next(result))
    print(result2)
    new_result = dataScreening(result2, float, (10, 50))
    print(new_result)

apply()