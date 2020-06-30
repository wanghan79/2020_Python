"""
  Author:Mh,Zhang
  Purpose:
  StuNumber:2020/6/29
"""
import random
import string


def data_sampling(func):
    def son(data_type, data_range, num, *conditions, str_len=10):
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
            return func(result, *conditions)
        except ValueError:
            print("输入的值有误!")
        except TypeError:
            print("参数类型错误!")
        except Exception as er:
            print(er)
    return son



@data_sampling
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
        int_number_2 = data_screening(int, [0, 200], 30, 60, 90)
        print(int_number_2)

        print("float型：")
        float_number2 = data_screening(float, [0, 100], 30, 60, 70)
        print(float_number2)

        print("string型：")
        str_result2 = data_screening(str, string.ascii_letters + string.digits + "@!#@", 50, 'b')
        print(str_result2)

    except Exception as e:
        print(e)


test()
