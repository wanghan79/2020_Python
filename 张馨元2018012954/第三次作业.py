import random
import string
def dataSampling(datatype, datarange, num, strlen=8):
    if datatype is int:
       for k in range(0, num):
            it = iter(datarange)
            i = random.randint(next(it), next(it))
            yield i
    elif datatype is float:
       for k in range(0, num):
            it = iter(datarange)
            i = random.uniform(next(it), next(it))
            yield i
    elif datatype is str:
       for k in range(0, num):
            i = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield i



def dataScreening(data,*ange):
    aresult = set()
    try:
        for j in data:
            if type(j) is int or type(j) is float:
                it = iter(ange)
                if next(it) <= j <= next(it):
                    aresult.add(j)
            elif type(j) is str:
                for substr in ange:
                    if substr in j:
                        aresult.add(j)
    except ValueError:
        print("参数有误")
    except TypeError:
        print("类型有误")
    except Exception as e:
        print(e)
    return aresult


def apply():
    try:
        result1 = set()
        t1 = dataSampling(int, (0, 200), 100)
        for x in range(0, 100):
         result1.add(next(t1))
        print(result1)
        aresult1=dataScreening(result1, 10, 50)
        print(aresult1)

        result2 = set()
        t2 = dataSampling(float, (0, 200), 100)
        for x in range(0, 100):
            result2.add(next(t2))
        print(result2)
        aresult2=dataScreening(result2, 10, 50)
        print(aresult2)

        result3 = set()
        t3 = dataSampling(str, string.ascii_letters + string.digits + string.punctuation, 1000, 10)
        for x in range(0, 1000):
            result3.add(next(t3))
        print(result3)
        aresult3=dataScreening(result3, 'ai', 'bm')
        print(aresult3)
    except Exception as ex:
        print(ex)


apply()

