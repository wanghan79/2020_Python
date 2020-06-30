import random
import string
#数据生成
def dataSampling(datatype, datarange1,datarange2, num, strlen=8):
    result = set()
    try:
     if datatype == int or float:
        while len(result)<num:
          result=random.sample(range(datarange1,datarange2),num)
     elif datatype == str:
        while len(result)<num:
            item = ''.join(random.SystemRandom().choice(datarange1,datarange2) for _ in range(strlen))
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

#数据筛选
def dataScreening(data,datatype,*conditions):
    result1=set()
    try:

            for item in data:
               if datatype == int or float:
                   co1,co2=conditions
                   if (co1<= item <= co2):
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
   #整形：
   intresult1 = dataSampling(int, 0,100,10)
   print(intresult1)
   intresult2=dataScreening(intresult1,int,0,50)
   print(intresult2)
   '''浮点型：
   floatresult1 = dataSampling(float, 0, 100, 10) 
   print(floatresult1)
   floatresult2 = dataScreening(intresult1, float, (0, 50),8)
   print(floatresult2)
   字符串：
   strresult1 = dataSampling(str,string.ascii_letters+string.digits+"@#$!",0,20,30)
   print(strresult1)
   strresult2 = dataScreening(intresult1, str,'c','d')
   print(strresult2)
   '''
apply()