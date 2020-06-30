"""
  Author:  Jiaza.Xin
  Purpose: Generate random data set.Random number generation is encapsulated as a modifier function,
            which is used to modify random number filtering function for data filtering
  Created: 18/6/2020
"""

import random
import string

result = set()
def dataSampling(datatype, datarange, num, strlen=5):
    '''
    :Description: Generate a given condition random data set.
    :param datatype: type;int,float,str
    :param datarange: iterable data set,len(datarange) == 2
    :param num: number
    :param strlen:length of string
    :return: a dataset
    '''
    def decorator(func):
         def wrapper(result, datatype, *range):
            #result = set()
            try:
                if datatype is int:
                    it = iter(datarange)
                    if len(datarange) != 2:
                        print("TypeError:incorrect filter condition for input in dataSampling")
                    elif num > -next(it) + next(it) + 1:
                        print("IOError:the parameter 'num' was entered incorrectly in dataSampling")
                    else:
                        while (len(result) < num):
                            it = iter(datarange)
                            item = random.randint(next(it), next(it))
                            result.add(item)
                elif datatype is float:
                    if len(datarange) != 2:
                        print("TypeError:incorrect filter condition for input in dataSampling")
                    else:
                        while len(result) < num:
                            it = iter(datarange)
                            item = random.uniform(next(it), next(it))
                            result.add(item)

                elif datatype is str:
                    while len(result) < num:
                        item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                        result.add(item)
                else:
                    pass
            except TypeError:
                print("TypeError :wrong type parameter entered in dataSampling")
            except MemoryError:
                print("MemoryError:Memory overflow error (not fatal to Python interpreter) in dataSampling")
            except Exception as e:
                print(str(e))
                print("Error in dataSampling")
            #finally:
                #return result
            return func(result, datatype, *range)
         return wrapper
    return decorator

@dataSampling(int, (1, 100), 10)
def dataScreening(result, datatype, *range):
    '''
    :Description:Data filtering
    :param data:a set the result of dataSampling
    :param datatype:type,int,float,str
    :param range:condition for data filtering,len(range) <= 2 when type is int or float
    :return:a set
       '''
    try:
        if type(range) is int or float:
            if len(range) > 2:
                print("TypeError:incorrect filter condition for input in dataScreening")
            elif len(range) == 1:
                print("Warning:the filter result is greater than the given condition in dataScreening")
        # Screening---------------------------------------------
        if datatype is int or float:
            if len(range) == 2:
                a, b = range
                result = {x for x in result if a <= x <= b}
            elif len(range) == 1:
                a = range
                result = {x for x in result if a <= x}
        elif datatype is str:
            st = iter(range)
            result = {x for x in result if next(st) in x}
    except TypeError:
        print("TypeError :wrong type parameter entered in dataScreening")
    except MemoryError:
        print("MemoryError:Memory overflow error (not fatal to Python interpreter) in dataScreening")
    except Exception as e:
        print(str(e))
        print("Error in dataScreening")
    else:
        return result

afresult1 = dataScreening(result, int, 20, 40)
print(afresult1)