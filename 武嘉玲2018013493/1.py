import random
import string

def dataSampling(datatype,datarange,num,str_len=8):
    try:
    result=set()
    for index in range(1,num):
        if datatype is int:
            it=iter(datarange)
            item=random.randint(next(it),next(it))
            result.append(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.append(item)
            continue
        elif datatype is str:
            item=''.join(random.SystemRandom().choice(datarange) for _ in range(str_len))
            continue
        else:
            continue
    return result

    except TypeError:
        print("数据类型必须为int,float或str")
    except ValueError:
        print("参数无效")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def dataScreening(data,range):
    try:
    result=set()
    for a in data:
            if type(a) is int or type(a) is float:
                it=iter(range)
                if next(it)<=a<=next(it):
                    result.add(a)
            else type(a) is str:
                for it in range:
                    if it in a:
                        result.add(a)
    except TypeError:
        print("数据类型必须为int,float或str")
    except ValueError:
        print("参数无效")
    except MemoryError:
        print("内存错误.")
    except Exception as e:
        print(e)
        print("参数错误.")

def apply():
    result1=dataSampling(int,(1,20),3)
    print(result1)
    screen1=dataScreening(result1,(5,15))
    print(screen1)

    result2=dataSampling(float,(1,20),3)
    print(result2)
    screen2=dataScreening(result2,(5,15))
    print(screen2)

    result3=dataSampling(str, string.ascii_letters + string.digits, 20, 3)
    print(result3)
    screen3=dataScreening(result3, 'a')
    print(screen3)

apply()