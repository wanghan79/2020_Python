import random
import string


def dataSampling(func):
    def wrapper(datatype,datarange,num,*args,strlen=8):
        result=set()
        if datatype is int:
            while len(result)<num:
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                result.add(item)
        elif datatype is float:
            while len(result)<num:
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                result.add(item)
        elif datatype is str:
            while len(result)<num:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return func(result,*args)


    return wrapper



@DataSampling
def dataScreening(data,*args):
        result = set()
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(args)
                if next(it)<=item and next(it)>=item:
                    result.add(item)
            elif type(item) is float:
                it = iter(args)
                if next(it)<=item and next(it)>=item:
                    result.add(item)
            elif type(item) is str:
                for subster in args:
                    if subster in item:
                        result.add(item)
        print(result)

        return result

def apply():
    print(DataScreening(int,[0,100],50 ,(0,50)))
    print(DataScreening(float,[0,100],50,(0,50)))
    print(DataScreening(str,string.ascii_letters+string.digits,100,('a','b')))

apply()