import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    try:
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item

        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item

        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item

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

def dataScreening(data, *conditions):
    result = set()
    try:
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(conditions)
                if next(it) <= item <= next(it):
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
        result = set()
        result1 = dataSampling(int, (0, 100), 10)
        for item in range(0, 10):
            result.add(next(result1))
        print(result)
        print(dataScreening(result, 40, 60))

        result = set()
        result2 = dataSampling(float, (0, 100), 10)
        for item in range(0, 10):
            result.add(next(result2))
        print(result)
        print(dataScreening(result, 40, 60))

        result = set()
        result3 = dataSampling(str, string.ascii_letters + string.digits, 10, 5)
        for item in range(0, 10):
            result.add(next(result3))
        print(result)
        print(dataScreening(result, 'x'))

apply()
