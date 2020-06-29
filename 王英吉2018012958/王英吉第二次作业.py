import string
import random
def make(func):
    def dataSampling(type, range, number,ans, strlen=8):
        result = set()
        try:
            if type is int:
                while True:
                    q = iter(range)
                    i = random.randint(next(q), next(q))
                    result.add(i)
                    if len(result) >= number:
                        break
            elif type is float:
                while True:
                    q = iter(range)
                    a = random.uniform(next(q), next(q))
                    result.add(a)
                    if len(result) >= number:
                        break
            elif type is str:
                while True:
                    a = ''.join(random.SystemRandom().choice(range) for _ in range(strlen))
                    result.add(a)
                    if len(result) >= number:
                        break
            return func(result,ans)


        except ValueError:
            print("参数错误")
        except TypeError:
            print("数据类型错误")
        except Exception as e:
            print(e)
    return dataSampling
@make
def dataScreening(data, datarange):
    result1=set()
    try:
        for b in data:
            if type(b) is int:
                it = iter(datarange)
                if next(it) <= b <= next(it):
                    result1.add(b)
                continue

            elif type(b) is float:
                it = iter(datarange)
                if next(it) <= b <= next(it):
                    result1.add(b)
                continue

            elif type(b) is str:
                if b.find(datarange) != -1:
                    result1.add(b)
                continue
    except ValueError:
     print("参数有误")
    except TypeError:
     print("类型有误")
    except Exception as e:
     print(e)
    return result1
print(dataScreening(int,{0,100},20,(20,80)),float,{0,100},20,(20,80),str,string.ascii_letters + string.digits + "pp",20,'qq')
