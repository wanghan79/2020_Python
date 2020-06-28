"""
Author: Bill Hao
Purpose: Generate random numbers and add them to mongodb
Created: 6/22/2020
Warning:This program need a running MongoDB local server to run
"""

import random
import pymongo


def generateRandomDataSet(dataType, dataRange, num, strlen = 6):
    '''
    :Description:Generate a given condition random data set
    :param dataType: Type of data that you want to generate
    :param dataRange: Range of data that you want to generate, 
                    if dataType == int or float, dataRange is a iterable data type 
                    and use the first two numbers as lower limit and upper limit
                    if dataType is str, dataRange is a string
    :param num: Number of data that you want to generate
    :param strlen: if datatype is str, strlen is length of every random string
    :return: random data

    '''
    try:
        if dataType is int:
            cnt = 1
            it = iter(dataRange)
            low = next(it)
            high = next(it)
            while cnt <= num:
                rData = random.randint(low, high)
                cnt += 1
                yield rData
        elif dataType is float:
            cnt = 1
            it = iter(dataRange)
            low = next(it)
            high = next(it)
            while cnt <= num:
                rData = random.uniform(low, high)
                cnt += 1
                yield rData
        elif dataType is str:
            cnt = 1
            while cnt <= num:
                rData = ''.join(random.sample(dataRange, strlen))
                cnt += 1
                yield rData
    except TypeError:
        print('One of params is not this function needed type')
    except NameError:
        print("Cannot find variable in both global and local")
    except MemoryError:
        print('Params is out of memory')
    except ValueError:
        print('dataRange need lower limit first')
    except IndentationError:
        print('the number of dataRange you give that less than two numbers')
    

def dataScreening(data, *condition):
    '''
    :Description:Screen data by condition
    :param dataSet: data ready to be screened
    :param condition: a series data that used to screen data, 
                      if dataSet element type is int or float, only the first two number can work
                      if dataSet element type is str, condition is string, 
                      it screeing the str in dataSet that has a substring equal to condition
    :return: if data in condition, return true else return false

    '''
    try:
        cond = iter(condition)
        if type(data) is int or type(data) is float:
            low = next(cond)
            high = next(cond)
            if low > high:
                raise ValueError('dataRange need lower limit first')
            if low <= data <= high:
                return True
            return False
        elif type(data) is str:
            substr = next(cond)
            if substr in data:
                return True
            return False
        else:
            return False
    except TypeError:
        print('One of params is not this function needed type')
    except NameError:
        print("Cannot find variable in both global and local")
    except MemoryError:
        print('Params is out of memory')
    except ValueError:
        print('dataRange need lower limit first')
    except IndentationError:
        print('the number of dataRange you give that less than two numbers')

def createDB():
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myClient['randomNumDB']
    return mydb

def insertDataToDB(mycol, dataType, dataRange, num):
    '''
    :Description:generate random data and insert them to DB
    :param mycol: the database collection
    :param dataType: Type of data that you want to generate
    :param dataRange: Range of data that you want to generate, 
                    if dataType == int or float, dataRange is a iterable data type 
                    and use the first two numbers as lower limit and upper limit
                    if dataType is str, dataRange is a string
    :param num: Number of data that you want to generate

    '''
    insertList = list()
    gen = generateRandomDataSet(dataType, dataRange, num)
    if dataType is int:
        dType = 'int'
    elif dataType is float:
        dType = 'float'
    elif dataType is str:
        dType = 'str'
    for data in gen:
        insertList.append({'value':data, 'type':dType})
    mycol.insert_many(insertList)

def searchAndScreenData(mycol, dataType, *cond):
    '''
    :Description:search data from database and screen data by condition
    :param mycol: database set
    :param dataType: used to find data in database
    :cond: a series screen condition
    :return: result set
    '''
    dataSet = mycol.find({'type':dataType}) # search data
    condit = iter(cond)
    filterRes = set()
    if dataType == 'int' or dataType == 'float':
        low = next(condit)
        high = next(condit)
        for data in dataSet:
            value = data['value']
            isIn = dataScreening(value, low, high) # screen
            if isIn:
                filterRes.add(value)
    elif dataType == 'str':
        con = next(condit)
        for data in dataSet:
            value = data['value']
            isIn = dataScreening(value, con) # screen
            if isIn:
                filterRes.add(value)
    return filterRes


def main():
    mydb = createDB() # create database
    mycol = mydb['randDataSet'] # create database collection
    
    #generate and insert data to DB
    insertDataToDB(mycol, int, [1, 100], 50) #generate and insert rand integer to database
    insertDataToDB(mycol, float, [1, 100], 50) #float
    insertDataToDB(mycol, str, 'abcdefghijklmnopqrstuvwxyz', 50) #string

    # search and screen data
    print(searchAndScreenData(mycol, 'int', 30, 40))  #int
    print(searchAndScreenData(mycol, 'float', 30, 40)) # float
    print(searchAndScreenData(mycol, 'str', 'bw'))  # string
    mycol.drop() #remove this collection
    
if __name__ == '__main__':
    main()
