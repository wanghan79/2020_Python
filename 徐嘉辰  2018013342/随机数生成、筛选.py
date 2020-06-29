import random
import string

def DataSampling(datatype,datarange,num,strlen=8):
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
    return result

def DataScreening(data,condition):
    result = set()
    for i in data:
        if type(i) is int:
            if i>=condition[0] and i<=condition[1]:
                result.add(i)
        if type(i) is float:
            if i>=condition[0] and i<=condition[1]:
                result.add(i)
        if type(i) is str:
            for item in condition:
                if item in i:
                    result.add(i)
    return result

def apply():
    result_int = DataSampling(int,[0,200],100)
    print(DataScreening(result_int,(0,100)))

    result_float = DataSampling(float,[0,100],100)
    print(DataScreening(result_float,(10,50)))

    result_str = DataSampling(str,string.ascii_letters+string.digits,200,20)
    print(DataScreening(result_str,('in','out')))

apply()
