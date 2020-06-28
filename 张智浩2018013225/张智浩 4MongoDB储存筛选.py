import pymongo
import random
import string

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
DB = myclient["test1"]
myInt = DB["int"]
myFlaot = DB["float"]
myStr = DB["str"]

def genVal(type, num, limit = None):
    result = []
    try:
        if type is int:
            for index in range(num):
                iterator = iter(limit)
                writeDB("int",random.randint(next(iterator),next(iterator)))
        elif type is float:
            for index in range(num):
                iterator = iter(limit)
                writeDB("float",random.uniform(next(iterator), next(iterator)))
        elif type is str:
            for index in range(num):
                strRes = ''.join(random.sample(string.ascii_letters + string.digits, num))
            writeDB("str",strRes)
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    else:
        if type is int or type is float:
            return result
        else:
            return strRes

def screen(type,values,doLim,upLim):
    result = []
    try:
        if type is not str:
            for value in values:
                if value >= doLim and value <= upLim:
                    result.append(value)
        else:
            for value in values[0]:
                if value >= doLim and value <= upLim:
                    result.append(value)
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    else:
        if type is not str:
            return result
        else:
            return ''.join(result)



def writeDB(type,data):
    if type == "int":
        intDcit = {type: data}
        myInt.insert_one(intDcit)
    elif type == "float":
        floatDict = {type: data}
        myFlaot.insert_one(floatDict)
    elif type == "str":
        srtDict = {type:data}
        myStr.insert_one(srtDict)

def readDB(type):
    ls = []
    if type == "int":
        for find in myInt.find():
            ls.append(find[type])
    if type == "float":
        for find in myFlaot.find():
            ls.append(find[type])
    if type == "str":
        for find in myStr.find():
            ls.append(find[type])
    return ls
def main():
    genVal(int, 10, {1,100})
    print("整型筛选前：",end='')
    print(readDB("int"))
    print("从数据库读出并筛选后的整形：", end='')
    print(screen(int,readDB('int'),10,50))

    genVal(float, 5, {1, 100})
    print("浮点型筛选前：", end='')
    print(readDB("float"))
    print("从数据库读出并筛选后的浮点型：", end='')
    print(screen(float, readDB('float'), 1.2, 50.3))

    genVal(str, 20)
    print("字符串筛选前：", end='')
    print(readDB("str")[0])
    print("从数据库读出并筛选后的字符串：", end='')
    print(screen(str, readDB('str'), 'a', 'z'))

    myInt.drop()
    myFlaot.drop()
    myStr.drop()

main()
