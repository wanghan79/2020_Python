#邹佳鑫第二次作业
import random
import string

def dataSampling(func):
    def wrapper(datatype, datarange, num, *conditions, strlen=10):
        result = set()
        try:        
           if dataType is int:
                it = iter(dataRange)
                low = next(it)
                high = next(it)
                while(len(rDataSet) < num):
                      rData = random.randint(low, high)
                      rDataSet.add(rData)
                elif dataType is float:
                    it = iter(dataRange)
                    low = next(it)
                    high = next(it)
                    while(len(rDataSet) < num):
                        rData = random.uniform(low, high)
                        rDataSet.add(rData)
                elif dataType is str:
                    while(len(rDataSet) < num):
                        rData = ''.join(random.sample(dataRange, strlen))
                        rDataSet.add(rData)
                return func(rDataSet, *args)
            except TypeError:
                print("The type is error.")
            except NameError:
                print("The name is error.")
            except MemoryError:
                print("The memory is error.")
            except ValueError:
                print("The value is error.")
            except IndentationError:
                print("The indentation is error.")
        return wrapper
     return decorator

def dataScreening(data, *conditions):
    result = set()
    for i in data:
        if type(i) is int:
            it = iter(conditions)
            if next(it)<=i and next(it)>=i:
                result.add(i)
        elif type(i) is float:
            it = iter(conditions)
            if next(it)<=i and next(it)>=i:
                result.add(i)
        elif type(i) is str:
            for teststr in conditions:
                if teststr in i:
                    result.add(i)
    return result
    
print(dataScreening(int, [0,536], 100, 20,60))
print(dataScreening(float, [0,536], 100, 20,60))
print(dataScreening(str,string.ascii_letters+string.digits, 1000, 'jf', 'n'))

if __name__ == '__main__':
    main()
