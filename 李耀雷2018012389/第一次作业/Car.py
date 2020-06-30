import random
import string

def dataSampling(dataType, dataRange, num, strlen=8):

    sum = set()
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
        return sum

def dataScreening(data,*args):
    result = set()
    try:
    # Screening
        for item in data:
            if type(item) is int or type(item) is float:
                num = iter(args)
                if next(num) <= item <= next(num):
                    result.add(item)
                elif type(item) is str:
                    for substr in args:
                        if substr in item:
                            result.add(item)
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
        return result


def apply():
            #   int类型
            resultInt = dataSampling(int, (0, 300), 100)
            print('随机生成100个在0~300之间的整数:')
            print(resultInt)
            print('筛选100~200之间的数:')
            new_resultInt = dataScreening(resultInt, 100, 200)
            print(new_resultInt)
            print("===================================================\n")

            #   float类型
            resultFloat = dataSampling(float, (0.0, 120.0), 100)
            print('随机生成100个在0~120之间的浮点数:')
            print(resultFloat)
            print('筛选50~100之间的数:')
            new_resultFloat = dataScreening(resultFloat, 50.0, 100.0)
            print(new_resultFloat)
            print("===================================================\n")

            #   str类型
            resultStr = dataSampling(str, string.ascii_letters + string.digits, 100, 20)
            print('随机生成100个长度为20的string')
            print(resultStr)
            print('筛选其中包含‘at’的string:')
            new_resultStr = dataScreening(resultStr, 'at')
            print(new_resultStr)
            print("===================================================\n")

if __name__ == '__main__':
    apply()

