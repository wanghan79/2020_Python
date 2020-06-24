"""

姓名: 周铭辉    学号：2018013134
项目实践第一次作业   函数封装随机数生成和筛选


"""

import random
import string


########################################################################################################################
def dataSampling(datatype,datarange,num,strlen=8):

    try:
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
    except ValueError:
        print("Error: 参数无效")
    except TypeError:
        print("Error: 类型错误，无法迭代")
    except NameError:
        print("Error: 初始化参数名称")
    else:
        return result
    finally:
        print("随机生成结果：")

########################################################################################################################
def dataScreening(data, *args):

    try:
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
    except ValueError:
        print("Error: 参数无效")
    except TypeError:
        print("Error: 类型错误，无法迭代")
    except NameError:
        print("Error: 初始化参数名称")
    else:
        return result
    finally:
        print("筛选生成结果：")


########################################################################################################################
def apply():


    result_int = dataSampling(int, [0,122], 20)
    print(result_int)
    int_Screening = dataScreening(result_int,7,22)
    print(int_Screening)


    result_float = dataSampling(float, [0, 122], 20)
    print(result_float)
    float_Screening = dataScreening(result_float,7,22)
    print(float_Screening)


    result_str = dataSampling(str,string.ascii_letters,20)
    print(result_str)
    str_Screening = dataScreening(result_str,'a')
    print(str_Screening)

apply()