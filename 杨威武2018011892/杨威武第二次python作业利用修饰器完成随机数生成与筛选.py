import random
import string

def datasampling(func):
    def wrapper(datatype, datarange, num, *args,strlen=15):
        result = list()
        if datatype is int :
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it),next(it))
                result.append(item)
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
        print('筛选前:',result)
        return func(result, *args)
    return wrapper
@datasampling
def dataScreening(data,*args):
    result = list()
    for i in data:
        if isinstance(i,int):
            if i >= args[0] and i <= args[1]:
                 result.append(i)
        elif isinstance(i,float):
            if i >= args[0] and i <= args[1]:
                result.append(i)
        elif isinstance(i,str):
            flag=1
            for x in i:
                if x  not in args[0]:
                    flag = 0
            if flag:
                result.append(i)
    print('筛选后:',result)
dataScreening(int,[0,100],100,0,10)
dataScreening(float,[0,100],100,0,10)
dataScreening(str,string.ascii_letters+string.digits,100,string.ascii_letters)