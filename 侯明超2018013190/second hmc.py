import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num,*args, strlen=8):
        result = list()
        if (datatype is int):
            while len(result) < num:
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                result.append(item)
        elif (datatype is str):
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
        elif (datatype is float):
            while len(result) < num:
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                result.append(item)
        print("DATA:")
        return func(result, *args)
    return wrapper

@dataSampling
def dataScreening(data,*args):
        ansresult = list()
        for i in data:
            if (type(i) is int):
                cond = iter(args)
                if(next(cond) <= i and next(cond) >= i):
                    ansresult.append(i)
            elif (type(i) is float):
                    cond = iter(args)
                    if (next(cond) <= i and next(cond) >= i):
                        ansresult.append(i)
            elif (type(i) is str):
                for condstr in args:
                    if(condstr in i):
                        ansresult.append(i)
        print(ansresult)

dataScreening(int,(0,100),6,30,80)
dataScreening(float,(0,100),6,30,80)
dataScreening(str,string.printable,6,'a'or'b')