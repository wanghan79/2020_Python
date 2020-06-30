import random
import string

def dataSampling(datatype, datarange, num, str_len=8):
    result = set()
    try:
        if datatype is int:
            for index in range(1, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
        elif datatype is float:
            for index in range(1, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
        elif datatype is str:
            for index in range(0, num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(str_len))
                yield item
        else:
           continue
        return result
    except TypeError:
        print("数据类型必须为int,float或str")
    except ValueError:
        print("参数无效")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def dataScreening(data, *conditions):
    result = set()
    try:
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it)<=item<=next(it):
                    result.add(item)

            elif type(item) is str:
                for itemstr in conditions:
                    if itemstr in item:
                        result.add(item)
        return result
    except TypeError:
        print("数据类型必须为int,float或str")
    except ValueError:
        print("参数无效")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def apply():
        result1 = set()
        result = dataSampling(int, (1, 20), 3)
        for i in range(1, 15):
        result1.add(next(result))
        print(result1)
        print(dataScreening(result1, 5, 10))

        result2 = set()
        result = dataSampling(float, (1, 20), 3)
        for i in range(1, 15):
        result2.add(next(result))
        print(result2)
        print(dataScreening(result, 5, 10))

        result3 = set()
        result = dataSampling(str, string.ascii_letters + string.digits, 20, 3)
        for i in range(1, 15):
        result3.add(next(result))
        print(result3)
        print(dataScreening(result3, 'a'))

apply()