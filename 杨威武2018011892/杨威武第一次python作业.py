import random
import string
class MyException(Exception):
    def __init__(self,name):
        self.name = name

class MyExceptionnew(Exception):
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2

def datasampling(datatype,datarange,num,strlen=8):
    try:
        if num > 1000000:
            raise OverflowError("数据数量过大：",num)
        result = list()
        if datatype is int :
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it),next(it))
                result.append(item)
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
        else:
            raise MyException(datatype)
        return result
    except MyException as e:
        print("数据类型错误",e.name)
    except StopIteration:
        print("数据范围无法迭代")
    except Exception as e:
        print("未知错误")
    finally :
        print("随机生成结果：")

def dataScreening(data,*args):
    try:
        result = list()
        for i in data:
            if type(i) == type(args[0]):
                if isinstance(i,int):
                    if i >= args[0] and i <= args[1]:
                         result.append(i)
                elif isinstance(i,float):
                    if i >= args[0] and i <= args[1]:
                        result.append(i)
                elif isinstance(i,str):
                    flag=1
                    for x in i:
                        if x  not in args[0]:
                            flag = 0
                    if flag:
                        result.append(i)
                else:
                    raise MyException(type(i))
            else:
                raise MyExceptionnew(type(i),type(args[0]))
        return result
    except MyException as e:
        print("本函数不支持该类型的筛选", e.name)
    except MyExceptionnew as e:
        print("数据类型与筛选类型不匹配",e.name1,e.name2)
    except Exception as e:
        print("未知错误")
    finally:
        print("筛选结果：")

def check():
    result1=datasampling(int,(1,1000),100)
    print(result1)
    results1=dataScreening(result1,10,100)
    print(results1)
    result2 = datasampling(float, (1, 1000), 100)
    print(result2)
    results2 = dataScreening(result2, 10.0, 100.0)
    print(results2)
    result3 = datasampling(str, string.ascii_letters+string.digits, 100,10)
    print(result3)
    results3 = dataScreening(result3,string.ascii_letters)
    print(results3)
check()