import random
import pymongo

def Generate(x,y):
    a = random.randint(x,y)
    yield a
    b = random.uniform(x,y)
    yield b
    c = ["Romance", "of", "the", "Three", "Kingdoms"]
    random.shuffle(c)
    yield c

def Datascreening(a,b,c,x,y):
    while a < (x+y)/2:
        a = random.randint(x,y)
    print("第一个随机数", a)
    while b < (x+y)/2:
        b = random.uniform(x,y)
    print("第二个随机数", b)
    while c[0]!="of":
        random.shuffle(c)
    print("第三个随机字符", c)

x = input("请输入下限 x: ")
x = int(x)
y = input("请输入上限 y: ")
y = int(y)
z = Generate(x,y)
set = {}
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["k"]
set[0] = next(z)
set[1] = next(z)
set[2] = next(z)
mydict = {"1":set[0],"2":set[1],"3":set[2]}
l = mycol.insert_one(mydict)
print(l)
for l in mycol.find():
    set2 = l
print(set2)
Datascreening(set2["1"],set2["2"],set2["3"],x,y)