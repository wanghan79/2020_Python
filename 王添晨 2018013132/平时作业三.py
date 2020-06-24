import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    if datatype is int:
        for i in range(num):
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item
    elif datatype is float:
        for i in range(num):
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            yield item
    elif datatype is str:
        for i in range(num):
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item


def dataScreening(data, *args):
    result = set()
    for i in data:
        if type(i) is int:
            it = iter(args)
            if next(it) <= i <= next(it):
                result.add(i)
        elif type(i) is float:
            it = iter(args)
            if next(it) <= i <= next(it):
                result.add(i)
        elif type(i) is str:
            for teststr in args:
                if teststr in i:
                    result.add(i)

    return result


def apply():
    result_int = list()
    result1 = dataSampling(int, 500), 50)
    while True:
        try:
            result1.append(next(result1))
        except StopIteration:
            break
    print("整型随机数生成：", result_int)
    int_Screening = dataScreening(result_int, 5, 27)
    print("筛选后：", int_Screening)

    result_float = list()
    result2 = dataSampling(float, (1, 500), 50)
    while True:
        try:
            result_float.append(next(result2))
        except StopIteration:
            break
    print("浮点型随机数生成：", result_float)
    float_Screening = dataScreening(result_float, 10.0, 100.0)
    print("筛选后：", float_Screening)

    result_str = list()
    result3 = dataSampling(str, string.ascii_letters + string.digits, 100, 10)
    while True:
        try:
            result_str.append(next(result3))
        except StopIteration:
            break
    print("字符型随机数生成：", result_str)
    str_Screening = dataScreening(result_str, string.ascii_letters)
    print("筛选后的字符随机数：", str_Screening)


apply()
