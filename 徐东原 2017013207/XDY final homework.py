##!/usr/bin/python3
"""
  Author: DY.Xu
  Purpose: mongoDB
  Created: 22/6/2020
"""
import random
import string
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.XDY
Sampleint = mydb.Sampleint
Samplefloat = mydb.Samplefloat
Samplestr = mydb.Samplestr


def dataSampling(datatype, datarange, num, strlen = 12):
    '''
            :Description: Generate a given condition random data set.
            :param datatype: basic data type (int  float  str)
            :param datarange: iterable data set
            :param num: number of data
            :param strlen:string length
            :return a data set
        '''
    try:
        if datatype is int:
            for i in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                Sampleint.insert_one({'data': item, 'type': 'int'})
                yield item
        elif datatype is float:
            for i in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                Samplefloat.insert_one({'data': item, 'type': 'float'})
                yield item
        elif datatype is str:
            for i in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                Samplestr.insert_one({'data': item, 'type': 'string'})
                yield item
        else:
            raise NameError
    except TypeError:
        print("Please enter the iterable data range in dataSampling")
    except NameError:
        print("Please enter the correct data type in dataSampling")
    except Exception:
        print("There are other errors in dataSampling")

def dataScreening(datatype,*args):
    '''
                :Description: Screen the data set
                :param data: An iterable data set
                :param args: Iterable ranges
                :return a data set
            '''
    try:
        if datatype is int:
            data = Sampleint.find({'id':0,'data':1,'type':0})
            num = Sampleint.count()
        elif datatype is float:
            data = Samplefloat.find({'id': 0, 'data': 1, 'type': 0})
            num = Samplefloat.count()
        elif datatype is str:
            data = Samplestr.find({'id': 0, 'data': 1, 'type': 0})
            num = Samplestr.count()
        else:
            raise NameError

        result = []
        for n in range (num):
            item=next(data)
            for i in args:
                if type(i) is set or list or tuple:
                    try:
                        it = iter(i)
                        if item >= next(it) and item <= next(it):
                            result.append(item)
                            break
                    except StopIteration:
                        pass
                elif type(i) is str:
                    if i in item:
                        result.append(item)
                        break
                else:
                    raise NameError
    except NameError:
        print("Please enter the correct data type in dataScreening")
    except TypeError:
        print("Please enter the correct condition type in dataScreening")
    except Exception:
        print("There are other errors in dataScreening")
    else:
        return result
def Apply():
    dataSampling(int, (0, 100), 30)
    print("type:int range:(0, 90)")
    print(dataScreening(int, (0, 90)))

    dataSampling(float, (0, 100), 20)
    print("type:float range:(0, 90)")


    dataSampling(str, string.ascii_letters + string.digits + "@#$!", 12, 5)
    print("type:string range:'at'")
    print(dataScreening(str,'at'))
if __name__ == '__main__':
    Apply()