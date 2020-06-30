#邹佳鑫第三次作业

import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    try:
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                yield item
                continue
           elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                yield item
                continue
          elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
                continue
         return result
    except TypeError:
        print("The type is error.")
    except ValueError:
        print("The value is error.")
    except MemoryError:
        print("The memory is error.")
    except Exception as e:
        print("ERROR:",e)
def dataScreening(data, *conditions):
    result = set()
    try:
        for i in data:
           if type(i) is int:
                it = iter(datarange)
                if next(it) <= i <= next(it):
                    result.add(i)
                continue

            elif type(i) is float:
                it = iter(datarange)
                if next(it) <= i <= next(it):
                    result.add(i)
                continue

            elif type(i) is str:
                if i.find(datarange) != -1:
                    result.add(i)
                continue
        return result
    except TypeError:
        print("The type is error.")
    except ValueError:
        print("The value is error.")
    except MemoryError:
        print("The memory is error.")
    except Exception as e:
        print("ERROR:",e)
def apply():
# int型
result2 = dataSampling(int, {0,100}, 30)
result2_1 = set()
for i in range(0, 30):
     result2_1.add(next(result2))
print(result2_1)
     result2_2 = dataScreening(result2_1, (5, 50))
if (not result2_2):
        print("Filter data can't be found")
else:
        print(result2_2)
        print(dataScreening(result1, 0, 20))
# float型
result1 = dataSampling(float, {0, 100}, 30)
result1_1=set()
for i in range(0, 30):
      result1_1.add(next(result1))
print(result1_1)
      result1_2 = dataScreening(result1_1,(5, 50))
if (not result1_2):
      print("Filter data can't be found")
else:
      print(result1_2)
      print(dataScreening(result2, 0, 20))
# str型
result3 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 30)
result3_1 = set()
for i in range(0, 30):
     result3_1.add(next(result3))
print(result3_1)
     result3_2 = dataScreening(result3_1, 'ab')
if(not result3_2):
     print("Filter data can't be found")
else:
     print(result3_2) 
     print(dataScreening(result3, 'a'))

apply()
