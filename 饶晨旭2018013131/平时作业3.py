import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    try:
        if datatype is int:
            for i in range(0,num):
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                yield item
        elif datatype is float:
            for i in range(0,num):
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                yield item
        elif datatype is str:
            for i in range(0,num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
    except ValueError:
        print("Error: 无效参数")
    except TypeError:
        print("Error: 对类型无效的操作，无法迭代")


def dataScreening(datatype, *datarange):
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
        print("Error: 无效参数")
    except TypeError:
        print("Error: 对类型无效的操作，无法迭代")

def apply():
    ans = set()
    que = dataSampling(int, {1, 100}, 10)
    while True:
        try:
            ans.add(next(que))
        except StopIteration:
            break
    print("筛选前：", ans)
    anss = dataScreening(ans, 10, 100)
    print("筛选后：", anss)

    ans = set()
    que = dataSampling(float, {1.0, 100.0}, 10)
    while True:
        try:
            ans.add(next(que))
        except StopIteration:
            break
    print("筛选前：", ans)
    anss = dataScreening(ans, 10.0, 100.0)
    print("筛选后：", anss)

    ans = set()
    que = dataSampling(str, string.printable, 50, 10)
    while True:
        try:
            ans.add(next(que))
        except StopIteration:
            break
    print("筛选前：", ans)
    anss = dataScreening(ans, string.ascii_letters)
    print("筛选后：", anss)


apply()
