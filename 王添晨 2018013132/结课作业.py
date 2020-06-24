import random
import string
import pymongo


def datasampling(datatype, datarange, num, strlen=8):
    if datatype is int:
        for i in range(0, num):
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            yield item

    elif datatype is float:
    for i in range(0, num):
        it = iter(datarange)
        item = random.uniform(next(it), next(it))
        yield item

    elif datatype is str:
    for i in range(0, num):
        item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
        yield item




 def dataScreening(datatype, result, *args):


try:
    result1 = []
    if datatype is int:
        for i in result:
            it = iter(args)
            if next(it) <= i <= next(it):
                result1.append(i)

elif datatype is float:
          for i in result:
          it = iter(args)
          if next(it) <= i <= next(it):
        result1.append(i)

elif datatype is str:
for i in result:
    for sub in i:
        if sub in args:
            result1.append(i)

     return result1


def check():


  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient ["wtc2018013132"]
myint = mydb["Int"]
mydouble = mydb["Float"]
mystring = mydb["String"]

result_int = list();
f1 = datasampling(int, (1, 2222), 222)
while True:
    try:
        result = {"value": next(f1)};
        myint.insert_one(result)
    except StopIteration:
        break

# 生成整型随机数

for x in myint.find({}, {"value": 1, "_id": 0}):
    for i, j in x.items():
        result_int.append(j)
print(result_int)
results1 = dataScreening(result_int, 22, 222)
print(results1)
# 筛选


result_float = list()
f2 = datasampling(float, (1, 2222), 222)
while True:
    try:
        result = {"value": next(f2)};
        mydouble.insert_one(result)
    except StopIteration:
        break

# 生成浮点型随机数
for x in mydouble.find({}, {"value": 1, "_id": 0}):
    for i, j in x.items():
        result_float.append(j)
print(result_float)
results2 = dataScreening(result_float, 22.2, 222.2)
print(results2)
# 筛选


result_str = list()
f3 = datasampling(str, string.ascii_letters + string.digits, 222, 22)
while True:
    try:
        result = {"value": next(f3)};
        mystring.insert_one(result)
    except StopIteration:
        break

# 生成字符型随机数
for x in mystring.find({}, {"value": 1, "_id": 0}):
    for i, j in x.items():
        result_str.append(j)
print(result_str)
results3 = dataScreening(result_str, string.ascii_letters)
print(results3)
# 筛选


check()
