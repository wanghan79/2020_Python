"""
  Author:  Yihang.Gao  高艺航
StuNumber: 2018012950
  Purpose: Generate random data set.
  Created: 19/6/2020
"""
import random
import string

def DataSampling(datatype, datarange, num, strlen=8):
    res = set()
    try:
        if datatype is int:
            while True:
                it=iter(datarange)
                i = random.randint(next(it), next(it))
                res.add(i)
                if len(res)>=num:
                    break
        elif datatype is float:
            while True:
               it = iter(datarange)
               i = random.uniform(next(it), next(it))
               res.add(i)
               if len(res) >= num:
                    break
        elif datatype is str:
            while True:
               i = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
               res.add(i)
               if len(res)>=num:
                   break
        return res
    except ValueError:
        print("Value Error.")
    except TypeError:
        print("Type Error.")
    except Exception as er:
        print(er)


def DataScreening(data,*ange):
    res = set()
    try:
        for j in data:
            if type(j) is int or type(j) is float:
                it = iter(ange)
                if next(it) <= j <= next(it):
                    res.add(j)
            elif type(j) is str:
                for substr in ange:
                    if substr in j:
                        res.add(j)
    except ValueError:
        print("Value Error.")
    except TypeError:
        print("Type Error.")
    except Exception as er:
        print(er)
    return res

def work():
    try:
        print("int型：")
        result1 = DataSampling(int, (0, 100), 5)
        print(result1)
        res1 = DataScreening(result1, 10, 90)
        if not res1:
            print(" Not  Found .")
        else:
            print(res1)

        print("float型：")
        result2 = DataSampling(float, (0, 100), 5)
        print(result2)
        res2 = DataScreening(result2, 10, 90)
        if not res2:
            print(" Not  Found .")
        else:
            print(res2)
        print("string型：")
        result3 = DataSampling(str, string.ascii_letters + string.digits + "@#$!", 5)
        print(result3)
        res3 = DataScreening(result3,'a')
        if not res3:
          print(" Not  Found .")
        else:
          print(res3)

    except Exception as wro:
      print(wro)

work()