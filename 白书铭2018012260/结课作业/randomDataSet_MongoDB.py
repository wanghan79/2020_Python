"""
Author: ShuMing.Bai
Purpose: final Homework:  Generate random data set by Decorators using MongDB to store data.
Created: 6/20/2020
"""
import random
import string
import pymongo

# Creating a database
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["randomDataDB"]
dblist = myClient.list_database_names()
if "randomDataDB" in dblist:
    print('randomDataDB exists!')
myIntCol = mydb["intData"]
myFloatCol = mydb["floatData"]
myStrCol = mydb["strData"]
collist = mydb.list_collection_names()
if "intData" in collist:
    print("intData exists!")
    myIntCol.delete_many({})
if "floatData" in collist:
    print("floatData exists!")
    myFloatCol.delete_many({})
if "strData" in collist:
    print("strData exists!")
    myStrCol.delete_many({})
print("These collections have been emptied")


def dataSampling(dataType, dataRange, num, strLen=8):
    """
    :Description: Generate random data set samples
    :param dataType: type of data generated
    :param dataRange: range of data generated
    :param num: the number of data in set
    :param strLen: maximum length of string( By default,it's 8)
    """
    try:
        if dataType is int:
            for i in range(0, num):
                iran = iter(dataRange)
                item = random.randint(next(iran), next(iran))
                yield item
        elif dataType is float:
            for i in range(0, num):
                iran = iter(dataRange)
                item = random.uniform(next(iran), next(iran))
                yield item
        elif dataType is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(dataRange) for _ in range(strLen))
                yield item
        else:
            pass
    except TypeError:
        print("There is TypeError occurred in dataSampling")
    except MemoryError:
        print("There is MemoryError occurred in dataSampling")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataSampling")
    finally:
        print("dataSampling finally...")


def dataScreening(dataType, *conditions):  # conditions 为可变参数*args,*args 表示任何多个无名参数，它是一个 tuple
    """
    :Description:This function can generate new data set according to the condition screen old data set
    :param dataType: type of data generated
    :param conditions:Screening conditions
    :return:filtered data set(a new data set)
    """
    result = set()
    try:
        # 判断在int和float类型的情况下，输入的conditions是否满足条件
        if (dataType is int or dataType is float) and len(conditions) > 2:
            print("Warning: There are only two numbers needed for data filtering.The first two numbers are "
                    "used as condition ranges")
            i = iter(conditions)
            if next(i) >= next(i):
                print("Warning: The filtered set will be empty because the former is larger than the latter")
            else:
                pass
        else:
            pass
        # Screening
        # Query the data in MongoDB Store the data in the result
        if dataType is int:
            num = iter(conditions)
            for item in myIntCol.find({"Value": {"$gte": next(num), "$lte": next(num)}}):
                result.add(item['Value'])
        elif dataType is float:
            num = iter(conditions)
            for item in myFloatCol.find({"Value": {"$gte": next(num), "$lte": next(num)}}):
                result.add(item['Value'])
        elif dataType is str:
            for substr in conditions:
                for item in myStrCol.find({"Value":{"$regex": substr}}):
                    result.add(item['Value'])
    except TypeError:
        print("There is TypeError occurred in dataScreening")
    except MemoryError:
        print("There is MemoryError occurred in dataScreening")
    except Exception as e:
        print(str(e))
        print("This Error occurred in dataScreening")
    else:
        return result
    finally:
        print("dataScreening finally...")


def Test():
    #  test: data Type is int
    print("data Type is int:")
    result_int = set()
    f_int = dataSampling(int, (100, 1000), 100)
    while True:
        try:
            result_int.add(next(f_int))
        except StopIteration:
            break
    for i in result_int:
        myDict = {"dataType": "int", "Value": i}
        myIntCol.insert_one(myDict)
    print("resultInt:", result_int)
    new_resultInt = dataScreening(int, 200, 600)
    print("new_resultInt", new_resultInt)
    print("===================================================\n")

    #  test: data Type is float
    print("data Type is float:")
    result_float = set()
    f_float = dataSampling(float, (10.0, 1000.0), 100)
    while True:
        try:
            result_float.add(next(f_float))
        except StopIteration:
            break
    for i in result_float:
        myDict = {"dataType": "float", "Value": i}
        myFloatCol.insert_one(myDict)
    print("resultFloat:", result_float)
    new_resultFloat=dataScreening(float, 660.0, 888.0)
    print("new_resultFloat", new_resultFloat)
    print("===================================================\n")

    #  test: data Type is str
    print("data Type is str:")
    result_str = set()
    f_str = dataSampling(str, string.ascii_letters + string.digits, 100, 20)
    while True:
        try:
            result_str.add(next(f_str))
        except StopIteration:
            break
    for i in result_str:
        myDict = {"dataType": "str", "Value": i}
        myStrCol.insert_one(myDict)
    print("resultStr:", result_str)
    new_resultStr=dataScreening(str, 'aa', 'at')
    print("new_resultStr:", new_resultStr)
    print("===================================================\n")


if __name__ == '__main__':
    Test()
