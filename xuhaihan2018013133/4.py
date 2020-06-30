import random
import string
import pymongo
import random
def randomInt(minnum,maxnum):
    return random.randint(minnum,maxnum)

def randomDouble(minnum,maxnum):
    return random.uniform(minnum,maxnum)

def randomStr(maxlen):
    s = ''
    ch = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(maxlen):
        index = random.randint(0,len(ch) - 1)
        s = s + ch[index]
    return s


def dataScreening(data,*args):
    result = list()
    for i in data:
        if isinstance(i,int):
            if i >= args[0] and i <= args[1]:
                    result.append(i)
        elif isinstance(i,float):
            if i >= args[0] and i <= args[1]:
                result.append(i)
        elif isinstance(i,str):
            if args[0] not in i:
                result.append(i)
    return result



def main():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["number"]
    myint = mydb["intnumber"]
    mydouble = mydb["doublenumber"]
    mystring = mydb["strings"]

    result1 = list()
    f1 = list()
    for i in range(5):
        ret = randomInt(10,100)
        f1.append(ret)
    
    for i in f1:
        result={"value":i}
        myint.insert_one(result)
    
    for x in myint.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result1.append(n)
    print(result1)
    results1s = dataScreening(result1, 50, 100)
    print(results1s)



    result2=list()
    f2 = list()
    for i in range(5):
        ret = randomDouble(0.9,99.9)
        f2.append(ret)
    
    for i in f2:
        result={"value":i}
        mydouble.insert_one(result)
    
    for x in mydouble.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result2.append(n)
    print(result2)
    results2s = dataScreening(result2, 10.0, 69.9)
    print(results2s)

    result3 = list()
    f3 = list()
    for i in range(5):
        s = randomStr(10)
        f3.append(s)

    for i in f3:
        result = {"value": i};
        mystring.insert_one(result)
    
    for x in mystring.find({},{ "value": 1, "_id": 0 }):
        for m,n in x.items():
            result3.append(n)
    print(result3)
    results3s = dataScreening(result3, 'o')
    print(results3s)

main()