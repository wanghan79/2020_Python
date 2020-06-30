import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *conditions, strlen=8):
        result=set()
        try:
            if datatype is int:
                for index in range(1, num):
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)

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

        except TypeError:
            print("TypeError")
        except ValueError:
            print("ValueError")
        except MemoryError:
            print("MemoryError")
        except Exception as e:
            print(e)
        return func(result, *conditions)
    return wrapper


@dataSampling
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
    print(dataScreening(int, [0, 100], 50 , 40, 60))
    print(dataScreening(float, [0, 100], 50 , 40 , 60))
    print(dataScreening(str, string.ascii_letters + string.digits, 100, 'x'))

apply()