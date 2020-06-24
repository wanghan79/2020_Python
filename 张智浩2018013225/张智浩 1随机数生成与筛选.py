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
    print("整形筛选前：",end='')
    result1 = genVal(int, 20, {1, 100})
    print(result1)
    print("整型筛选后：", end='')
    result1 = screen(int, result1, 20, 50)
    print(result1)
    print("浮点型筛选前：", end='')
    result1 = genVal(float, 10, {1, 100})
    print(result1)
    print("浮点型筛选后：", end='')
    result1 = screen(float, result1, 30.2, 70.6)
    print(result1)
    print("字符串筛选前：", end='')
    result1 = genVal(str, 20)
    print(result1)
    print("字符串筛选后：", end='')
    result1 = screen(str, result1, 'a', 'z')
    print(result1)
main()