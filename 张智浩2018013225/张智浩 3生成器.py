import random
import string
def genVal(type, num, limit = None,):
    result = []
    try:
        if type is int:
            for index in range(num):
                iterator = iter(limit)
                result.append(random.randint(next(iterator),next(iterator)))
        elif type is float:
            for index in range(num):
                iterator = iter(limit)
                result.append(random.uniform(next(iterator), next(iterator)))
        elif type is str:
            for index in range(num):
                strRes = ''.join(random.sample(string.ascii_letters + string.digits, num))
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    else:
        if type is int or type is float:
            return result
        else:
            return strRes

def screen(type,values,doLim,upLim):
    result = []
    try:
        for value in values:
            if value >= doLim and value <= upLim:
                result.append(value)
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    else:
        if type is not str:
            return result
        else:
            return ''.join(result)

def main():
    resultint = set()
    itint = iter(genVal(int, 5, {1,100}))
    while True:
        try:
           resultint.add(next(itint))
        except StopIteration:
            break
    print("整型筛选前：",end = '')
    print(list(resultint))
    print("整型筛选后：", end='')
    print(screen(int, resultint, 10, 50))

    resultfloat = set()
    itflaot = iter(genVal(float, 5, {1, 100}))
    while True:
        try:
            resultfloat.add(next(itflaot))
        except StopIteration:
            break
    print("浮点型筛选前：", end='')
    print(list(resultfloat))
    print("浮点型筛选后：", end='')
    print(screen(float, resultfloat, 10, 50))

    resultstr = set()
    itstr = iter(genVal(str, 20))
    while True:
        try:
            resultstr.add(next(itstr))
        except StopIteration:
            break
    print("字符串筛选前：", end='')
    print(''.join(list(resultstr)))
    print("字符串筛选后：", end='')
    print(screen(str, resultstr, 'a', 'z'))


main()