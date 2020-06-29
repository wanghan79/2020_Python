import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
        #result = set()
        if datatype is int:
            for k in range(num):
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                yield item
        elif datatype is float:
            for k in range(num):
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                yield item
        elif datatype is str:
            for k in range(num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item


def dataScreening(data,*args):
        ansresult = set()
        for i in data:
            if (type(i) is int):
                it = iter(args)
                if(next(it) <= i and next(it) >= i):
                    ansresult.add(i)
            elif (type(i) is float):
                    it = iter(args)
                    if next(it) <= i and next(it) >= i:
                        ansresult.add(i)
            elif (type(i) is str):
                for Screening in args:
                    if(Screening in i):
                        ansresult.add(i)
        return ansresult

def apply():
    result_int=set()
    result = dataSampling(int,(0,100), 6)
    while True:
        try:
            result_int.add(next(result))
        except StopIteration:
            break
    print(result_int)
    result_a =dataScreening(result_int,30,80)
    print(result_a)

    result_float=set()
    result = dataSampling(float, (0, 100), 6)
    while True:
        try:
            result_float.add(next(result))
        except StopIteration:
            break
    print(result_float)
    result_b = dataScreening(result_float,30,80)
    print(result_b)

    result_str = set()
    result = dataSampling(str, string.printable,6)
    while True:
        try:
            result_str.add(next(result))
        except StopIteration:
            break
    print(result_str)
    result_c = dataScreening(result_str,'a'or'b'or'c'or'd')
    print(result_c)
    #出现 set() 说明没有相符的结果

apply()