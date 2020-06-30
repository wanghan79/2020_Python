import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    '''

    :param datatype:
    :param datarange:
    :param num:
    :param strlen:
    :return:
    '''

    try:
        result = set()

        if datatype is int:
            for index in range(1, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                continue
        elif datatype is float:
            for index in range(1, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            for index in range(1, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        else:
            pass
        return result

    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")
    except Exception as e:
        print(e)


def dataScreening(data, *conditions):#*args
    result = set()
    #Screening
    try:
        for item in data:

            if type(item) is int:
                i = iter(conditions)
                if next(i) <= item <= next(i):
                    result.add(item)

            elif type(item) is float:
                i = iter(conditions)
                if next(i) <= item <= next(i):
                    result.add(item)

            elif type(item) is str:
                for itemstr in conditions:
                    if itemstr in item:
                        result.add(item)

        return result


    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")
    except Exception as e:
        print(e)



def apply():
    result1 = dataSampling(int, [0, 100], 10)
    print(result1)
    print(dataScreening(result1, 20, 80))

    result2 = dataSampling(float, [0, 100], 10)
    print(result2)
    print(dataScreening(result2, 20, 80))

    result3= dataSampling(str, string.ascii_letters + string.digits, 10, 5)
    print(result3)
    print(dataScreening(result3, 'a', 'b', 'c'))

apply()