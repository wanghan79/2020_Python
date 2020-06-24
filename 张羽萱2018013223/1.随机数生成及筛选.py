"""
Author: zhang yuxuan 2018013223
Purpose: Generate random data set.
Created: 19/6/2020

"""
import random
import string

def DataSampling(datatype, datarange, num, strlen=8):
    try:
        result = set()
        if datatype is int:
            while True:
                it=iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)
                if len(result) >= num:
                    break
        elif datatype is float:
            while True:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
                if len(result) >= num:
                    break
        elif datatype is str:
            while True:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
                if len(result) >= num:
                    break
        return result
    except TypeError:
     print("Type Error")
    except NameError:
        print("Name Error")
    except:
        raise Exception
    else:
        return result
    finally:
        print("Continue:")
def dataScreening(data, *conditions):
    try:
        result = set()
        for i in data:
            if type(i) is int:
                it = iter(conditions)
                if next(it)<=i<=next(it):
                    result.add(i)
            elif type(i) is float:
                it = iter(conditions)
                if next(it) <= i <= next(it):
                    result.add(i)
            elif type(i) is str:
                for m in conditions:
                    if m in i:
                        result.add(i)
        return result
    except TypeError:
     print("Type Error")
    except:
        raise Exception
    else:
        return result
    finally:
        print("Continue:")
def Apply():
    print("int sample")
    result = DataSampling(int, [0, 1000], 10)
    print(dataScreening(result, 10, 100))

    result = DataSampling(int, 10, 100)
    print(dataScreening(result, 10, 100))
    print("float sample")
    result = DataSampling(float, [0, 100], 100)
    print(dataScreening(result, 10, 20))

    result = DataSampling(float, [10, 100], "m")
    print(dataScreening(result, 10, 20))

    print("string sample")
    result = DataSampling(str, string.ascii_letters+string.digits, 1000, 10)
    print(dataScreening(result, 'my', 'mymy', 'mymymy'))

    result = DataSampling(str, 100, 2000, 15)
    print(dataScreening(result, 'python', 'pythonn', 'pythonnn'))
Apply()