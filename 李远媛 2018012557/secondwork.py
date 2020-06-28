'''
    Author: Yy.Li
    Purpose:The random number generation is encapsulated as a modifier function, which is used to modify the random number filtering function for data filtering
    Created:20/6/2020
'''

import random
import string


def create(func):
    def dataSampling(datatype, datarange, num, condition, strlen=8):  # 固定参数；默认参数
        '''
        :Description:Generate a gievn condition random data set.
        :param datatype:
        :param datarange:iterable data set
        :param num:number
        :param condition:
        :param strlen:
        :return:a dataset
        '''

        result = set()
        try:
            if datatype is int:
                while len(result) < num:
                    it = iter(datarange)  # 返回迭代器
                    item = random.randint(next(it), next(it))
                    result.add(item)
                    continue

            elif datatype is float:
                while len(result) < num:
                    it = iter(datarange)  # 返回迭代器
                    item = random.uniform(next(it), next(it))
                    result.add(item)
                    continue

            elif datatype is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
                    continue
            else:
                pass
            return func(result, datatype, condition)
        except ValueError:
            print("ValueError2:传入无效参数")
        except TypeError:
            print("TypeError2:对类型无效的参数")
        except Exception as e:
            print("error")
    return dataSampling


@create
def dataScreening(data, datatype, datarange):
    new_result = set()
    try:
        for i in data:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= i <= next(it):
                    new_result.add(i)
                    continue

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= i <= next(it):
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


new_result = dataScreening(int, (0, 100), 15, (10, 30))
print(new_result)

new_result = dataScreening(float, (0, 100), 15, (10, 50))
print(new_result)

result = string.ascii_letters + string.digits + "@#$!"
new_result = dataScreening(str, result, 30, 'a', 10)
#print(result)
print(new_result)
