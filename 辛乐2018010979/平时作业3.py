import random
import string
#数据生成
def dataSampling(datatype, datarange1, datarange2, num, strlen=8, item=None):
    result = set()
    try:
     if datatype == int or float:
        while (True):
            result = random.sample(range(datarange1, datarange2), num)
            yield item
            continue
     elif datatype == str:
         while (True):
            item = ''.join(random.SystemRandom().choice(datarange1,datarange2) for _ in range(strlen))
            yield item
            continue
    except Exception as e:
        print(e)
    except TypeError:
         print('TypeError')
    except ValueError:
         print('ValueError')
    except MemoryError:
         print('MemoryError')

#数据筛选
def dataScreening(data,datatype,*conditions):
    result1=set()
    try:
            for item in data:
               if datatype == int or float:
                   co1,co2=conditions
                   if (co1<=item <=co2):
                    result1.add(item)
               elif datatype == str:
                   for stb in conditions:
                    if stb in item:
                      result1.add(item)
    except Exception as e:
        print(e)
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')
    except MemoryError:
        print('MemoryError')
def apply():
   #整形：
   intresult = dataSampling(int, 0,100,10)
   intresult1=set()
   while len(intresult1)<10:
        intresult1.add(next(intresult))
   print(intresult1)
   intresult2=dataScreening(intresult1,int,0,50)
   print(intresult2)
   '''浮点型：
   floatresult = dataSampling(float, 0, 100, 10)
   floatresult1 = set()
   while len(floatresult1) < 10:
       floatresult1.add(next(floatresult))
   print(floatresult1)
   floatresult2 = dataScreening(floatresult1, int, 0, 50)
   print(intresult2)
   #字符型：
   strresult = dataSampling(str,string.ascii_letters + string.digits)
   strresult1 = set()
   while len(strresult1) < 10:
       strresult1.add(next(strresult))
   print(strresult1)
   strresult2 = dataScreening(strresult1, str,'c','d')
   print(strresult2)
   '''
apply()
