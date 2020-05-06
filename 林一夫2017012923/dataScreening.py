import string
from dataSampling import dataSampling

def dataScreening(data,condition):
    '''
    :param data:int,float,string
    :param condition:list,string
    :return:data st: condition
    '''
    if condition is list and len(condition)!=2:
        print('illegal condition')
        return
    if type(data) is int and type(condition) is list:
        try:
            it1=iter(condition)
            lowerBound=next(it1)
            upperBound=next(it1)
            if data>=lowerBound and data<=upperBound:
                return data
        except Exception:
            print('type miss match')
            return
    elif type(data) is float and type(condition) is list:
        try:
            it1 = iter(condition)
            lowerBound = next(it1)
            upperBound = next(it1)
            if data >= lowerBound and data <= upperBound:
                return data
        except Exception:
            print('type miss match')
            return
    elif type(data) is str and type(condition) is str:
        if data.find(condition)!=-1:
            return data
    else:
        pass
    return

