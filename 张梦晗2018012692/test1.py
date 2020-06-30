"""
  Author:Mh,Zhang
  Purpose: Generate random data set.
  StuNumber:2020/6/29
"""
import random
import string

def data_sampling(data_type, data_range, num, str_len=10):
    '''
            :Description: Generate a given condition random data set.
            :param datatype: int/float
            :param datarange: iterable data set
            :param num: number
            :param strlen:
            :return: a dataset
            '''
    result = set()
    try:
        if data_type is int:
            while True:
                it = iter(data_range)
                i = random.randint(next(it), next(it))
                result.add(i)
                if len(result) >= num:
                    break
        elif data_type is float:
            while True:
                it = iter(data_range)
                i = random.uniform(next(it), next(it))
                result.add(i)
                if len(result) >= num:
                    break
        elif data_type is str:
            while True:
                i = ''.join(random.SystemRandom().choice(data_range) for _ in range(str_len))
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
    result = set()
    try:
        for j in data:
            if type(j) is int or type(j) is float:
                it = iter(ange)
                if next(it) <= j <= next(it):
                    result.add(j)
            elif type(j) is str:
                for val in ange:
                    if val in j:
                        result.add(j)
    except ValueError:
        print("输入的值有误!")
    except TypeError:
        print("参数类型错误!")
    except Exception as er:
        print(er)
    return result


def test():
    try:
        print("int型：")
        int_number = data_sampling(int, (1, 100), 5)
        print(int_number)
        int_number_2 = data_screening(int_number, 20, 90)
        print(int_number_2)

        print("float型：")
        float_number = data_sampling(float, (1, 100), 5)
        print(float_number)
        float_number2 = data_screening(float_number, 20, 90)
        print(float_number2)

        print("string型：")
        str_result = data_sampling(str, string.ascii_letters + string.digits + "@!#@", 5)
        print(str_result)
        str_result2 = data_screening(str_result, 'a')
        print(str_result2)

    except Exception as e:
        print(e)


test()
