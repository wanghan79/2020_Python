import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    try:
        result = set()
        if datatype is int:
            while len(result) < num:
                it = iter(datarange) item = random.randint(next(it), next(it))
                result.add(item)
        elif datatype is float:
            while len(result) < num:
                it = iter(datarange) item = random.uniform(next(it), next(it))
                result.add(item)
        elif datatype is str:
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)


    except TypeError: print("Wrong type, please enter the correct type of data")
    except ValueError: print("Please enter the correct data")
    except NameError: print("Please enter the data type at first")
        
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
                if next(it) <= item <=next(it):
                    result.add(item)
            elif type(item) is str:
                for Screening_str in term:
                    if Screening_str in item:
                        result.add(item)
                        
                        
    except TypeError: print("Wrong type, please enter the correct type of data")
    except ValueError: print("Please enter the correct data")
    except NameError: print("Please enter the data type at first")
        
    else:
        return result
    finally:
        print("Filter data as follows：")


def apply():


    #整型
    result_int = dataSampling(int, [0,500], 50)
    print(result_int)
    int_Screening = dataScreening(result_int,10,20)
    print(int_Screening)


    #浮点型
    result_float = dataSampling(float, [0, 500], 50)
    print(result_float)
    float_Screening = dataScreening(result_float,10,20)
    print(float_Screening)

    
    #字符型
    result_str = dataSampling(str,string.ascii_letters,20)
    print(result_str)
    str_Screening = dataScreening(result_str,'up')
    print(str_Screening)

apply()
