import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    try:
        result = set()
        if (datatype is int):
            while len(result) < num:
                i = iter(datarange)
                item = random.randint(next(i), next(i))
                result.add(item)
        elif (datatype is float):
            while len(result) < num:
                i = iter(datarange)
                item = random.uniform(next(i), next(i))
                result.add(item)
        elif (datatype is str):
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        return result
    except ValueError:
        print("error:参数无效")
    except TypeError:
        print("error:类型错误")
    ##else:
    ##    return result

def dataScreening(data,*args):
    try:
        ansresult = set()
        for i in data:
            if (type(i) is int):
                cond = iter(args)
                if(next(cond) <= i and next(cond) >= i):
                    ansresult.add(i)
            elif (type(i) is float):
                    cond = iter(args)
                    if (next(cond) <= i and next(cond) >= i):
                        ansresult.add(i)
            elif (type(i) is str):
                for condstr in args:
                    if(condstr in i):
                        ansresult.add(i)
    except ValueError:
        print("error:参数无效")
    except TypeError:
        print("error:类型错误")
    return ansresult

def apply():
    try:
      result_a = dataSampling(str, string.printable, 6)
      print(result_a)
      ansresult_a = dataScreening(result_a,'a'or'b')
      if not ansresult_a:
          print("unsuitable data")
      else:
          print("answer")
          print(ansresult_a)
          print

      result_b = dataSampling(int,(0,100),6)
      print(result_b)
      ansresult_b = dataScreening(result_b,30,80)
      if not ansresult_b:
          print("unsuitable data")
      else:
          print("answer")
          print(ansresult_b)
          print

      result_c = dataSampling(float,(0,100),6)
      print(result_c)
      ansresult_c = dataScreening(result_c,30,80)
      if not ansresult_c:
          print("unsuitable data")
      else:
          print("answer")
          print(ansresult_c)
          print
    except Exception as ex:
      print(ex)

apply()