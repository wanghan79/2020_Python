import random
import string
def dataSampling(type, range, number, string=8):
      try:
         result = set()
         if type is int:
             while len(result) < number:
                 it = iter(range)
                 item = random.randint(next(it), next(it))
                 result.add(item)
         elif type is float:
            while len(result) < number:
                it = iter(range)
                item = random.uniform(next(it), next(it))
                result.add(item)
         elif type is str:
            while len(result) < number:
                item = ''.join(random.SystemRandom().choice(range) for _ in range(string))
                result.add(item)
      except TypeError:
        print("错误数据类型")
      except ValueError:
        print("错误数据")
      except NameError:
        print("未输入数据类型")
      else:
         return result
      finally:
        print("生成数据：")
def dataScreening(data, *s):
    try:
        rage = set()
        for num in data:
            if type(num) is int or type(num) is float:
                it = iter(s)
                if next(it) <= num <= next(it):
                    rage.add(num)
            elif type(num) is str:
                for Screening_num in s:
                    if Screening_num in num:
                        rage.add(num)
    except TypeError:
        print("错误数据类型")
    except ValueError:
        print("错误数据")
    except NameError:
        print("未输入数据类型")
    else:
        return rage
    finally:
        print("生成数据：")
def apply():
    result_int = dataSampling(int, [0, 100], 20)
    print(result_int)
    int_Screening = dataScreening(result_int, 20, 30)
    print(int_Screening)#整型数据
    result_float = dataSampling(float, [0, 100], 20)
    print(result_float)
    float_Screening = dataScreening(result_float, 10, 20)
    print(float_Screening)#浮点型数据
    result_str = dataSampling(str, string.ascii_letters, 30)
    print(result_str)
    str_Screening = dataScreening(result_str, 'up')
    print(str_Screening)#字符型数据
apply()