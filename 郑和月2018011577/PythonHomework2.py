"""
  Author:  heyue.zheng
  Purpose: Modify functions
  Created: 24/6/2020
"""

import random
import string

def dataSampling(datatype, datarange, num):
    def decorator(func):
        try:
            result = set()
            for index in range(0, num):
                if datatype is int:
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
                    continue
                elif datatype is float:
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
                    continue
                elif datatype is str:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(8))
                    result.add(item)
                    continue
                else:
                    continue
            return result
            return func(datatype, datarange, num)
        except TypeError:
            print("TypeError")
        except ValueError:
            print("ValueError")
        except MemoryError:
            print("MemoryError")
    return decorator


@dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
def dataScreening(data, *args):
    try:
        result = set()
        for value in data:
            if type(value) is int:
                if value in args:
                    result.add(value)
                    continue
            elif type(value) is float:
                if value in args:
                    result.add(value)
                    continue
            elif type(value) is str:
               for arg in args:
                    if arg in value:
                        result.add(value)
                        continue
            else:
               continue
        return result
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    except MemoryError:
        print("MemoryError")

def apply():
    result1 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
    print(result1)
    result_1 = dataScreening(result1, 'a', 'x', '5')
    print(result_1)
apply()
