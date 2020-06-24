"""

姓名: 周铭辉    学号：2018013134
项目实践第三次作业   使用生成器修改作业一中的随机数生成过程，并能够使用随机数筛选函数进行数据筛选


"""

import random
import string


########################################################################################################################
def dataSampling(datatype,datarange,num,strlen=8):

        if datatype is int:
            for i in range(num):
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                yield  item
        elif datatype is float:
            for i in range(num):
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                yield  item
        elif datatype is str:
            for i in range(num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield  item


########################################################################################################################
def dataScreening(data, *args):

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

        return result


########################################################################################################################
def apply():
    result_int=set()
    resulti = dataSampling(int, [0,122], 20)
    while True:
        try:
            result_int.add(next(resulti))
        except StopIteration:
            break
    print("int随机生成：",result_int)
    int_Screening = dataScreening(result_int, 7,22)
    print("筛选后结果：",int_Screening)
    #########################################################
    result_float=set()
    resultf = dataSampling(float, [0, 122], 20)
    while True:
        try:
            result_float.add(next(resultf))
        except StopIteration:
            break
    print("float随机生成：",result_float)
    float_Screening = dataScreening(result_float,7,22)
    print("筛选后结果：",float_Screening)
    #########################################################
    result_str = set()
    results = dataSampling(str, string.ascii_letters, 20)
    while True:
        try:
            result_str.add(next(results))
        except StopIteration:
            break
    print("str随机生成：", result_str)
    str_Screening = dataScreening(result_str, 'a')
    print("筛选后的字符随机数：", str_Screening)
    #########################################################


apply()