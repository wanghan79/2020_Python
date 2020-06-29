import random
import string

def datasampling(datatype, datarange, num, strlen=8):
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
    except ValueError:
        print("Error: 无效参数")
    except TypeError:
        print("Error: 对类型无效的操作，无法迭代")
    else:
        return result


def dataScreening(data,*args):
    try:
        result=set()
        for item in data:
            num=0
            for arg in args:
                if (eval(arg)):
                    num=num+1
            if num==len(args):
                result.add(item)
    except NameError:
        print("Error: 变量名称错误，请使用item")
    except TypeError:
        print("Error: 对类型无效的操作，无法迭代")
    except ValueError:
        print("Error: 无效参数")
    else:
        return result


def apply():
    result1 = datasampling(int, (1, 100), 10)
    print(result1)
    ans1 = datascreening(result1, 10, 100)
    print(ans1)

    result2 = datasampling(float, (1, 100), 10)
    print(result2)
    ans2 = datascreening(result2, 10.0, 100.0)
    print(ans2)

    result3 = datasampling(str, string.ascii_letters + string.digits, 50, 10)
    print(result3)
    ans3 = datascreening(result3, str, 'at')
    print(ans3)


apply()
