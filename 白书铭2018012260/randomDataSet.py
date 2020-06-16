import random
import string


def dataSampling(dataType, dataRange, num, strLen=8):
    """
    :param dataType:
    :param dataRange:
    :param num:
    :param strLen:
    :return:
    """
    # try:
    # except:
    # except:
    # else:
    # finally:
    #     raise
    result = set()
    while len(result) < num:
        if dataType is int:
            iran = iter(dataRange)
            item = random.randint(next(iran), next(iran))
            result.add(item)
            continue
        elif dataType is float:
            iran = iter(dataRange)
            item = random.uniform(next(iran), next(iran))
            result.add(item)
            continue
        elif dataType is str:
            item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strLen))
            result.add(item)
            continue
    return result


def dataScreening(data, *args):  # conditions 为可变参数*args
    result = set()

    return result


def apply():
    result = dataSampling(int, string.digits + string.ascii_letters, 10)
    print(result)


apply()
