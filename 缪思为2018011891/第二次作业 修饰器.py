import random
import string

def dataSampling(func):
    def wrapper(datatype,datarange,num,*args,strlen=8):
        result=list()
        if datatype is int:
            while len(result)<num:
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                result.append(item)
        elif datatype is float:
            while len(result)<num:
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                result.append(item)
        elif datatype is str:
            while len(result)<num:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
        print('筛选前的数据为：',result)
        return func(result,*args)
    return wrapper
@dataSampling
def dataScreening(data,*args):
    result=list()
    for i in data:
        if isinstance(i,int):
            it=iter(args)
            if (i>=next(it) and i<=next(it)):
                result.append(i)
        elif isinstance(i,float):
            it=iter(args)
            if (i >= next(it) and i <= next(it)):
                result.append(i)
        elif isinstance(i,str):
            for x in args:
                if (x in i):
                    result.append(i)
    print('筛选后的数据为：',result)

dataScreening(int,[0,100],100,10,60)
dataScreening(float,[0,100],100,0,10)
dataScreening(str,string.printable,100,'s')


