import random
import string
import pymongo
def datasampling(type,range,number,strlen=10):
    if type is int :
        for a in range(0, number):
            ans = iter(range)
            ber = random.randint(next(ans),next(ans))
            yield  ber
    elif type is float:
        for a in range(0, number):
            ans = iter(range)
            ber = random.uniform(next(ans), next(ans))
            yield ber
    elif type is str:
        for a in range(0, number):
            ber = ''.join(random.SystemRandom().choice(range) for _ in range(strlen))
            yield ber
def dataScreening(data,*item):
    result = list()
    for i in data:
        if type(i) == type(item[0]):
            if isinstance(i,int):
                if i >= item[0] and i <= item[1]:
                     result.append(i)
            elif isinstance(i, str):
                flag = 1
                for x in i:
                    if x not in item[0]:
                        flag = 0
                if flag:
                    result.append(i)
            elif isinstance(i,float):
                if i >= item[0] and i <= item[1]:
                    result.append(i)
    return result

def apply():
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["datadb"]
    mycol_int = mydb["整型"]
    mycol_float = mydb["浮点型"]
    mycol_str = mydb["字符型"]
    num = set()
    a = datasampling(str, string.ascii_letters + string.digits + string.punctuation, 20)
    for index in range(0, 10):
        mycol_str.insert_one(next(a))
    for i in mycol_str.find():
        num.add(i.get("data"))
    print(num)
    num = dataScreening(num, "str", "6")
    print(num)

    num = set()
    a = datasampling(float, (0, 100), 100)
    for index in range(0, 20):
        mycol_float.insert_one(next(a))
    for i in mycol_float.find():
        num.add(i.get("data"))
    print(num)
    num = dataScreening(num, "float", (1.0, 50.0))
    print(num)

    num = set()
    a = datasampling(int, (0, 20), 20)
    for index in range(0, 20):
        mycol_int.insert_one(next(a))
    for i in mycol_int.find():
        num.add(i.get("data"))
    print(num)
    num = dataScreening(num, "int", (1, 100), 10)
    print(num)
if __name__ == "__main__":
    apply()