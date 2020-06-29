'''
Author: WeiFan 2018011641
Aim:  Generation and filtering of random numbers
Data: 2020/6/17
'''
import random
import string

def DataSampling(datatype,datarange,num,strlen=8):
    try:
        result=set()
        if datatype is int:
            while len(result)<num:
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                result.add(item)
        elif datatype is float:
            while len(result)<num:
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                result.add(item)
        elif datatype is str:
            while len(result)<num:
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
    except ValueError:
        print("Invalid Data")
    except TypeError:
        print("Error in type,which may cause the parameter to fail to iterate")
    else :
        return result

def DataSelect(result,datatype,item1,item2):
    try:
        newresult=set()
        for it in result:
            if datatype is int:
                if (it>=item1) and (it<=item2):
                    newresult.add(it)
            elif datatype is float:
                if (it>=item1) and (it<=item2):
                    newresult.add(it)
            elif datatype is str:
                if (item1 in it) and (item2 not in it):
                    newresult.add(it)
    except ValueError:
        print("Invalid Data")
    except TypeError:
        print("Error in type,which may cause the parameter to fail to iterate")
    else :
        return newresult

def apply():
    try:
        result1=DataSampling(int,(0,100),8)
        print(result1)
        newresult1=DataSelect(result1,int,10,40)
        if not newresult1:
            print("No Found")
        else:
            print(newresult1)

        result2 = DataSampling(float, (0, 100), 8)
        print(result2)
        newresult2 = DataSelect(result2, float,20,35)
        if not newresult2:
            print("No Found")
        else:
            print(newresult2)

        result3 = DataSampling(str,string.ascii_letters + string.digits,8)
        print(result3)
        newresult3 = DataSelect(result3,str,'A','b')
        if not newresult3:
            print("No Found")
        else:
            print(newresult3)

    except Exception as e:
      print(e)

apply()




