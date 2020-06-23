import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    try:
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)

        elif datatype is float:
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)



    except TypeError:
        print("类型错误，请输入正确类型的数")
    except ValueError:
        print("参数错误，请输入正确的数")
    except NameError:
        print("请先输入数据类型")
    else:
        return result
    finally:
        print("生成数据 ：")


def dataScreening(data, *term):
    try:
        result = set()
        for item in data:
            if type(item) is int or type(item) is float:
                it = iter(term)
                if next(it) <= item and next(it) >= item:
                    result.add(item)
            elif type(item) is float:
                it = iter(term)
                if next(it) <= item and next(it) >= item:
                    result.add(item)
            elif type(item) is str:
                for Screening_str in term:
                    if Screening_str in item:
                        result.add(item)
    except TypeError:
        print("类型错误，请输入正确类型的数")
    except ValueError:
        print("参数错误，请输入正确的数")
    except NameError:
        print("请先输入数据类型")
    else:
        return result
    finally:
        print("筛选数据：")


def apply():


    result_int = dataSampling(int, [0,500], 50)
    print(result_int)
    int_Screening = dataScreening(result_int,10,20)
    print(int_Screening)


    result_float = dataSampling(float, [0, 500], 50)
    print(result_float)
    float_Screening = dataScreening(result_float,10,20)
    print(float_Screening)


    result_str = dataSampling(str,string.ascii_letters,20)
    print(result_str)
    str_Screening = dataScreening(result_str,'up')
    print(str_Screening)

apply()