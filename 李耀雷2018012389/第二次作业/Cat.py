import random
import string

def dataSampling(func):
    def wrapper(dataType,dataRange,num,*conditions,strlen = 8):

        sum = set()
        print("dataType is",dataType)
        try:
            if dataType is int:
                while len(sum) < num:
                    i = iter(dataRange)
                    temp = random.randint(next(i), next(i))
                    sum.add(temp)
            elif dataType is float:
                while len(sum) <num:
                    i = iter(dataRange)
                    temp = random.uniform(next(i), next(i))
                    sum.add(temp)
            elif dataType is str:
                while len(sum) < num:
                    temp = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                    sum.add(temp)
            else:
                pass

        except TypeError:
            print("The Type is error.")
        except MemoryError:
            print("The Memory is error.")
        except ValueError:
            print("The value is not correct")
        except Exception as e:
            print(e)
            print("ERROR")
        else:
            print("筛选：",sum)
            return func(sum,*conditions)
        finally:
            print('筛选结果：')
    return wrapper

@dataSampling
def dataScreening(data,*args):
    result = set()
    for item in data:
        if type(item) is int or type(item) is float:
            num = iter(args)
            if next(num) <= item <= next(num):
                result.add(item)
        elif type(item) is str:
            for substr in args:
                if substr in item:
                    result.add(item)
    return result

def apply():
    str_ex = string.ascii_letters + string.digits + string.punctuation
    # int 类型
    print(dataScreening(int, (0, 300), 100, 100, 200))
    print('————————————————————————————————————————————————\n')

    # float  类型
    print(dataScreening(float, (0.0,200.0), 100, 50.0, 100.0))
    print('—————————————————————————————————————————————————\n')

    # str  类型

    print(dataScreening(str, str_ex, 100, 'at'))


apply()

