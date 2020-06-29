"""

姓名: 周铭辉    学号：2018013134
项目实践第二次作业   将作业一中的随机数生成封装为修饰函数，用于修饰随机数筛选函数进行数据筛选


"""

import random
import string


########################################################################################################################
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
        print('随机生成的数据：', result)
        return func(result,*args)

    return wrapper

@dataSampling

def dataScreening(data,*args):
        result = set()
        for i in data:
            if type(i) is int:
                it = iter(args)
                if next(it)<=i and next(it)>=i:
                    result.add(i)
            elif type(i) is float:
                it = iter(args)
                if next(it)<=i and next(it)>=i:
                    result.add(i)
            elif type(i) is str:
                for Screening_str in args:
                    if Screening_str in i:
                        result.add(i)
        print('筛选后的数据：  ', result)


        return result



########################################################################################################################


dataScreening(int,[1,122],20,7,22)
dataScreening(float,[1,122],20,7,22)
dataScreening(str,string.ascii_letters,20,'a')

