import random
import string
def genVal(func):
    def wrapper(type, num, doLim, upLim, limit = None):
        result = []
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
        if type is int or type is float:
            print("筛选前：",result, end='')
            return func(type, result, doLim, upLim)
        else:
            print("筛选前：", strRes, end='')
            strRes = ''.join(strRes)
            return func(type, strRes, doLim, upLim)

    return wrapper
@genVal
def screen(type,values,doLim,upLim):
    screenRes = []
    try:
        for value in values:
            if value >= doLim and value <= upLim:
                screenRes.append(value)
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    else:
        if type is not str:
            print("\n筛选后：", screenRes)
        else:
            print("\n筛选后：", ''.join(screenRes))


def main():
    print("整形:")
    result = screen(int, 10, 10, 50, {1,100})  
    print("浮点型:")
    result = screen(float, 5, 6.2, 70.4, {1, 100})
    print("字符串：")
    result = screen(str, 20, 'a', 'z')
main()