#邹佳鑫第一次作业

import random
import string
from collections.abc import Iterable

def dataSampling(datatype, datarange, num, strlen=8):

    try:
        result = set()
        if dataType is int:
            while len(result) < num:
                i = iter(dataRange)
                temp = random.randint(next(i), next(i))
                result.add(temp)
        elif dataType is float:
            while len(result) <num:
                i = iter(dataRange)
                temp = random.uniform(next(i), next(i))
                result.add(temp)
        elif dataType is str:
            while len(result) < num:
                temp = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strlen))
                result.add(temp)
        else:
            pass
            
    except Exception as e:
        print("ERROR:", e)
    except TypeError:
        print("The Type is error.")
    except MemoryError:
        print("The Memory is error.")
    else:
        return result
    def dataScreening(data,*args):
    result = set()
    try:
        for item in data:
            if type(item) is int or type(item) is float:
                num = iter(args)
                if next(num) <= item <= next(num):
                    result.add(item)
                elif type(item) is str:
                    for substr in args:
                        if substr in item:
                            result.add(item)
 except TypeError:
        print("The Type is error.")
except MemoryError:
        print("The Memory is error.")
except ValueError:
        print("The value is not correct")
except Exception as e:
        print("ERROR:", e)
else:
        return result
        
def apply():
# int型
result = dataSampling(int, (0, 20), 20) 
print("The dataset to be screening is:", result)
result = dataScreening(result, "int", (1, 10), 5)
print("Screen out all random numbers greater than 1 but less than 10 and divisible by 5:", result)
#float型
result = dataSampling(float, (0, 20), 20)
print("The dataset to be screening is:", result)
result = dataScreening(result, "float", (1.0, 10.0))
print("Screen out all random numbers greater than 1 and less than 10:", result)
print("\n")
#string型
result = dataSampling(str, string.ascii_letters + string.digits + string.punctuation, 20)
print("The dataset to be screening is:", result)
result = dataScreening(result, "str", "6")
print("Screen out the string containing character 6:", result)
print("\n")

if __name__ == '__main__':
    apply()
