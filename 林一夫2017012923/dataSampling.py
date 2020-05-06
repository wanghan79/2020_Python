import random
import string

def dataSampling(datatype, datarange, num, strlen=6):
    '''
    :param datatype:int,float,string
    :param datarange:list
    :param num:int
    :param strlen:if datatype is string,strlen is the length of data
    :return:poduce data with datarange
    '''
    result=list()
    if num<0 or type(num)!=int:
        print('illegal num')
        return result
    if datatype is int:
        if len(datarange)!=2 or type(datarange)!=list:
            print('illegal datarangr')
            return result
        while len(result)!=num:
            try:
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                result.append(item)
            except Exception:
                print('type miss match')
                return result
            continue
    elif datatype is float:
        if len(datarange)!=2 or type(datarange)!=list:
            print('illegal datarangr')
            return result
        while len(result)!=num:
            try:
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                result.append(item)
            except Exception:
                print('type miss match')
                return result
            continue
    elif datatype is str:
        if strlen<=0:
            print('illegal strlen')
            return result
        while len(result)!=num:
            try:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
            except Exception:
                print('type miss match')
                return result
            continue
    else:
        pass
    return result

