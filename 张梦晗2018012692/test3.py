"""
  Author:Mh,Zhang
  Purpose:
  StuNumber:2020/6/29
"""
import random
import string


def data_sampling(data_type, data_range, num, begin, end, str_len=10):
    result = set()
    try:
        if data_type is int:
            while True:
                it = iter(data_range)
                i = random.randint(next(it), next(it))
                if data_screening(i, begin, end) is not None:
                    result.add(i)
                if len(result) >= num:
                    break
        elif data_type is float:
            while True:
                it = iter(data_range)
                i = random.uniform(next(it), next(it))
                if data_screening(i, begin, end) is not None:
                    result.add(i)
                if len(result) >= num:
                    break
        elif data_type is str:
            while True:
                i = ''.join(random.SystemRandom().choice(data_range) for _ in range(str_len))
                if data_screening(i, begin, end) is not None:
                    result.add(i)
                if len(result) >= num:
                    break
        return result
    except ValueError:
        print("输入的值有误!")
    except TypeError:
        print("参数类型错误!")
    except Exception as er:
        print(er)


def data_screening(data, *ange):
    try:
        it = iter(ange)
        if type(data) is int or type(data) is float:
            if next(it) <= data <= next(it):
                return data
        elif type(data) is str:
            for val in ange:
                if val in data:
                    return data
    except ValueError:
        print("输入的值有误!")
    except TypeError:
        print("参数类型错误!")
    except Exception as er:
        print(er)
    return None


def test():
    try:
        print("int型：")
        int_number = data_sampling(int, (1, 100), 5, 20, 90)
        print(int_number)


        print("float型：")
        float_number = data_sampling(float, (1, 100), 5, 20, 90)
        print(float_number)


        print("string型：")
        str_result = data_sampling(str, string.ascii_letters + string.digits + "@!#@", 10, 'ae', 'bc')
        print(str_result)


    except Exception as e:
        print(e)


test()
