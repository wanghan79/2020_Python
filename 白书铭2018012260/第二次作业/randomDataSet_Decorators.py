"""
Author: ShuMing.Bai
Purpose: Second Homework:  Generate random data set by Decorators.
Created: 5/28/2020
"""
import random
import string


def dataSampling(func):
    def wrapper(dataType, dataRange, num, *conditions, strLen=8):
        """
        :Description: Generate random data set samples.It's a decorator.
        :param dataType: type of data generated
        :param dataRange: range of data generated
        :param num: the number of data in set
        :param conditions:Screening conditions
        :param strLen: maximum length of string( By default,it's 8)
        :return: a data set
        """
        result = set()
        print("data Type is ", dataType)
        try:
            if dataType is int:
                while len(result) < num:
                    iran = iter(dataRange)
                    item = random.randint(next(iran), next(iran))
                    result.add(item)
            elif dataType is float:
                while len(result) < num:
                    iran = iter(dataRange)
                    item = random.uniform(next(iran), next(iran))
                    result.add(item)
            elif dataType is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strLen))
                    result.add(item)
            else:
                pass
        except TypeError:
            print("There is TypeError occurred in dataSampling")
        except MemoryError:
            print("There is MemoryError occurred in dataSampling")
        except Exception as e:
            print(str(e))
            print("This Error occurred in dataSampling")
        else:
            print("Sampling:", result)
            return func(result, *conditions)
        finally:
            print("==================================================\n")
    return wrapper


@dataSampling
def dataScreening(data, *conditions):  # conditions 为可变参数*args,*args 表示任何多个无名参数，它是一个 tuple
    """
    :Description:This function can generate new data set according to the condition screen old data set
    :param data: Data set to be screened
    :param conditions:Screening conditions
    :return:filtered data set(a new data set)
    """
    result = set()
    try:
        # 判断在int和float类型的情况下，输入的conditions是否满足条件
        for item in data:
            if (type(item) is int or type(item) is float) and len(conditions) > 2:
                print("Warning: There are only two numbers needed for data filtering.The first two numbers are "
                      "used as condition ranges")
                i = iter(conditions)
                if next(i) >= next(i):
                    print("Warning: The filtered set will be empty because the former is larger than the latter")
                else:
                    pass
                break
            else:
                break
        # Screening
        for item in data:
            if type(item) is int or type(item) is float:
                num = iter(conditions)
                if next(num) <= item <= next(num):
                    result.add(item)
            elif type(item) is str:
                for substr in conditions:
                    if substr in item:
                        result.add(item)
            else:
                pass
    except TypeError:
        print("There is TypeError occurred in dataScreening")
    except MemoryError:
        print("There is MemoryError occurred in dataScreening")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataScreening")
    else:
        print("Screening:", result)
    finally:
        print("dataScreening finally...")


if __name__ == '__main__':
    dataScreening(str, string.ascii_letters + string.digits, 100, 'a', 'at')
    dataScreening(int, (100, 1000), 100, 200, 666)
    dataScreening(float, (100.0, 1000.0), 100, 200.0, 666.0)
