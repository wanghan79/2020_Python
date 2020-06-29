import random
import string


def dataSampling(func):
    def wrapper(datatype, datarange, num, *args, strlen=8):
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                if len(result) >= num:
                    break

        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                if len(result) >= num:
                    break

        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                if len(result) >= num:
                    break

        print('筛选前：', result)
        return func(result, *args)

    return wrapper


@dataSampling
def dataScreening(data, *args):
    result = set()
    for i in data:
        if isinstance(i, int):
            it = iter(args)
            if i >= next(it) >= i:
                result.add(i)

        elif isinstance(i, float):
            it = iter(args)
            if i >= next(it) >= i:
                result.add(i)

        elif isinstance(i, str):
            for x in args:
                if x in i:
                    result.add(i)

    print('筛选后：', result)


dataScreening(int, [0, 200], 100, 50, 100)
dataScreening(float, [0, 200], 100, 50, 100)
dataScreening(str, string.ascii_letters, 100, 'at')
