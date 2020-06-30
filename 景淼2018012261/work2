"""
Author:JingMiao
Purpose:Generate random data set.
Create:25/6/2020
"""
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *args,strlen=8):

        """
        :Description:Generate a given condition random data set.
        :param datatype: int/float/str/...
        :param datarange:iterable data set
        :param num:number
        :param strlen:length of str
        :return:a dataset
        """
        try:

            result = set()
            if datatype is int:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.randint(next(it), next(it))
                    result.add(item)
                    continue
            elif datatype is float:
                while len(result) < num:
                    it = iter(datarange)
                    item = random.uniform(next(it), next(it))
                    result.add(item)
                    continue
            elif datatype is str:
                while len(result) < num:
                    item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                    result.add(item)
                    continue
            else:
                pass
            print("Before:")
            print(result)
            print("After:")

        except TypeError:
            print("The dataType must be int,float,str!")
        except ValueError:
            print("The dataRange is error!")
        except OverflowError:
            print("num is too large!")

        return func(result, *args)

    return wrapper


@dataSampling
def dataScreening(data,*args):
    try:

        result = set()
        for index in data:
            if type(index) is int or type(index) is float:
                it = iter(args)
                if next(it) <= index <= next(it):
                    result.add(index)

            elif isinstance(index, str):
                for it in args:
                    if it in index:
                        result.add(index)
        print(result)
    except TypeError:
        print("The data type is error!")
    except ValueError:
        print("The data value is error!")



def apply():
    print("int:")
    dataScreening(int, (1, 10), 10, 5, 10)

    print("\nfloat:")
    dataScreening(float,(-2.5,10),3,0,5)

    print("\nstr:")
    dataScreening(str,string.ascii_letters+string.digits,7,'jm','1','2','3')


apply()
