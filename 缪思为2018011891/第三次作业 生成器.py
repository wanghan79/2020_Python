import string
import random
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


ans=set()
f=dataSampling(int,{1,100},10)
while True:
    try:
        ans.add(next(f))
    except StopIteration:
        break
print(ans)
ans1=dataScreening(ans,"item<50","item>20")
print(ans1)


ans=set()
f=dataSampling(float,{1.0,100.0},10)
while True:
    try:
        ans.add(next(f))
    except StopIteration:
        break
print(ans)
ans1=dataScreening(ans,"item<50","item>20")
print(ans1)


ans=set()
f=dataSampling(str,string.printable,20)
while True:
    try:
        ans.add(next(f))
    except StopIteration:
        break
print(ans)
ans1=dataScreening(ans,"item.find('a')!=-1")
print(ans1)