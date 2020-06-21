import string
import random
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["MuseWEI"]
myIntValue=mydb["Int"]
myFloatValue=mydb["Float"]
myStringfalue=mydb["String"]
def dataSampling(datatype,datarange,num,strlen=8):
    try:
        if datatype is int:
            for i in range(0,num):
                it=iter(datarange)
                item=random.randint(next(it),next(it))
                yield item
        elif datatype is float:
            for i in range(0,num):
                it=iter(datarange)
                item=random.uniform(next(it),next(it))
                yield item
        elif datatype is str:
            for i in range(0,num):
                item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                yield item
    except ValueError:
        print("Error: 无效参数")
    except TypeError:
        print("Error: 对类型无效的操作，无法迭代")

def dataScreening(data,*args):
    try:
        result=set()
        for item in data:
            num=0
            for arg in args:
                if (eval(arg)):
                    num=num+1
            if num==len(args):
                result.add(item)
    except NameError:
        print("Error: 变量名称错误，请使用item")
    except TypeError:
        print("Error: 对类型无效的操作，无法迭代")
    except ValueError:
        print("Error: 无效参数")
    else:
        return result


ans=list()
f=dataSampling(int,{1,100},10)
while True:
    try:
        ans.append(next(f))
    except StopIteration:
        break
print("随机生成的整数：",ans)
mydict={"value":ans}
myIntValue.insert_one(mydict)
for x in myIntValue.find():
    y=x

y["value"]=ans
ans1=dataScreening(ans,"item<50","item>20")
print("从MongoDB数据库中取出并筛选后的整数：",ans1)


ans=list()
f=dataSampling(float,{1.0,100.0},10)
while True:
    try:
        ans.append(next(f))
    except StopIteration:
        break
print("随机生成的浮点数：",ans)
mydict={"value":ans}
myIntValue.insert_one(mydict)
for x in myIntValue.find():
    y=x

y["value"]=ans
ans1=dataScreening(ans,"item<50","item>20")
print("从MongoDB数据库中取出并筛选后的浮点数：",ans1)


ans=list()
f=dataSampling(str,string.printable,20)
while True:
    try:
        ans.append(next(f))
    except StopIteration:
        break
print("随机生成的字符：",ans)
mydict={"value":ans}
myIntValue.insert_one(mydict)
for x in myIntValue.find():
    y=x

y["value"]=ans
ans1=dataScreening(ans,"item.find('a')!=-1")
print("从MongoDB数据库中取出并筛选后的字符：",ans1)