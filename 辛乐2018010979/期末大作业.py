import random
import string
import pymongo as pg
myclient = pg.MongoClient('mongodb://localhost:27017/')
mydb = myclient['runoobdb']
dblist = myclient.list_database_names()
mycol = mydb["sites"]
# dblist=myclient.database_names()
if "renoobdb" in dblist:
    print('数据库已存在！')
def dataSampling(datatype, datarange1,datarange2, num, strlen=8):
    result = set()
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
    #整型：
    intresult1=dataSampling(int ,0,100,10)
    intresult2=dataScreening(intresult1,int,10,10)
    mydict={'type':'int','info':intresult2}
    mycol.insert_one(mydict)
    x1=mycol.find_one({'type':'int'})
    print(x1)
    '''
    #浮点型：
    floatresult1 = dataSampling(float, 0, 100, 10)
    floatresult2 = dataScreening(floatresult1, float, 10, 10)
    mydict = {'type': 'float', 'info': floatresult2}
    pg.mycol.insert_one(mydict)
    x2 = pg.mycol.find_one({'type': 'float'})
    print(x2)
    #字符型：
    strresult1 = dataSampling(str, string.ascii_letters + string.digits + string.punctuation,str,10)
    strresult2 = dataScreening(strresult1, str, 'c', d)
    mydict = {'type': 'str', 'info': strresult2}
    pg.mycol.insert_one(mydict)
    x3 = pg.mycol.find_one({'type': 'float'})
    print(x3)
    '''
apply()