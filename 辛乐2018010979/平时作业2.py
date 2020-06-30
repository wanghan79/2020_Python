import random
import string
def dataSampling(func):
        def wrapper(datatype,datarange1,datarange2,num,*conditions,strlen=8):
            result=set()
            try:
                if datatype == int or float:
                    while len(result) < num:
                        result = random.sample(range(datarange1, datarange2), num)
                elif datatype == str:
                    while len(result) < num:
                        item = ''.join(random.SystemRandom().choice(datarange1, datarange2) for _ in range(strlen))
                        result.add(item)
                return result
            except Exception as e:
                print(e)
            except TypeError:
                print('TypeError')
            except ValueError:
                print('ValueError')
            except MemoryError:
                print('MemoryError')
            return func(result, *conditions)
        return wrapper
#数据筛选
@dataSampling
def dataScreening(data,datatype,*conditions):
    result1=set()
    try:
            for item in data:
               if datatype == int or float:
                   co=iter(conditions)
                   if (next(co)<= item <= next(co)):
                    result1.add(item)
               elif datatype == str:
                   for stb in conditions:
                    if stb in item:
                      result1.add(item)
            return result1
    except Exception as e:
        print(e)
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')
    except MemoryError:
        print('MemoryError')
def apply():
   #整型：
   intresult1 = dataScreening(int,0,100,10,0,45)
   print(intresult1)
'''
  #浮点型：
   floatresult1 = dataScreening(float, 0, 100, 10,(0,45))
   print(floatresult1)
  #字符串：
   strresult1 = dataSampling(str,string.ascii_letters+string.digits+"@#$!",0,10,('c','d'))
   print(strresult1)
'''
apply()
