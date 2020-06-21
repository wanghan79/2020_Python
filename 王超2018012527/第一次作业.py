import random
import string


def datasampling(datatype, datarange, num, strlen=8):
    try:
        result = set()
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                if len(result) >= num:
                    break

        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                if len(result) >= num:
                    break

        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange)
                               for _ in range(strlen))
                result.add(item)
                if len(result) >= num:
                    break
        return result

    except ValueError:
        print("参数无效")
    except TypeError:
        print("类型错误")


def datascreening(datatype, *datarange):
    try:
        result = set()
        for x in result:
            if datatype is int:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    result.add(x)

            elif datatype is float:
                it = iter(datarange)
                if next(it) <= x <= next(it):
                    result.add(x)

            elif datatype is str:
                if x.find(datarange) != -1:
                    result.add(x)
        return result
    except ValueError:
        print("参数无效")
    except TypeError:
        print("类型错误")


def apply():
    result1 = datasampling(int, (1, 100), 10)
    print(result1)
    ans1 = datascreening(result1, 10, 100)
    print(ans1)

    result2 = datasampling(float, (1, 100), 10)
    print(result2)
    ans2 = datascreening(result2, 10.0, 100.0)
    print(ans2)

    result3 = datasampling(str, string.ascii_letters + string.digits, 50, 10)
    print(result3)
    ans3 = datascreening(result3, str, 'at')
    print(ans3)


apply()
