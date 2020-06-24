import random
import string

def DataSampling(func):
    def wrapper(datatype,datarange,num,condition,strlen=8):
        result = set()
        if datatype is int:
            for index in range(0,num):
                it = iter(datarange)
                item = random.randint(next(it),next(it))
                result.add(item)
        elif datatype is float:
            for index in range(0,num):
                it = iter(datarange)
                item = random.uniform(next(it),next(it))
                result.add(item)
        elif datatype is str:
            for index in range(0,num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return func(result,condition)
    return wrapper

@DataSampling
def DataScreening(data,condition):
    result = set()
    for i in data:
        if type(i) is int:
            if i>=condition[0] and i<=condition[1]:
                result.add(i)
        elif type(i) is float:
            if i>=condition[0] and i<=condition[1]:
                result.add(i)
        elif type(i) is str:
            for item in condition:
                if item in i:
                    result.add(i)
    return result

def apply():
    print(DataScreening(int,[0,200],100,(0,100)))
    print(DataScreening(float,[0,200],100,(0,100)))
    print(DataScreening(str,string.ascii_letters+string.digits,100,('in','out')))

apply()
