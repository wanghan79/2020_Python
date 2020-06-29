"""
  Author:  jianxi.li
  Purpose: homework3:Generator modification homework1.
  Created: 17/6/2020
"""
import string
import random
def dataSampling(type,datarangement,number,strlen=20):
    try:
        if type is int:
            for j in range(0,number):
                options=iter(datarangement)
                document=random.randint(next(options),next(options))
                yield document
        elif type is float:
            for j in range(0,number):
                options=iter(datarangement)
                document=random.uniform(next(options),next(options))
                yield document
        elif type is str:
            for j in range(0,number):
                document=''.join(random.SystemRandom().choice(datarangement) for _ in range(strlen))
                yield document
    except ValueError:
        print("Error1:ValueError")
    except TypeError:
        print("Error2:TypeError")
def dataScreening(data,*args):
    try:
        output=set()
        for i in data:
            number=0
            for arg in args:
                if (eval(arg)):
                    number=number+1
            if number==len(args):
                output.add(i)
    except NameError:
        print("Error3:NameError")
    except TypeError:
        print("Error2:TypeError")
    except ValueError:
        print("Error1:ValueError")
    else:
        return output
data=set()
x=dataSampling(int,{1,150},10)
while True:
    try:
        data.add(next(x))
    except StopIteration:
        break
print(data)
output=dataScreening(data,"i<80","i>30")
print("result 1")
print(output)
data=set()
y=dataSampling(float,{1.0,120.0},10)
while True:
    try:
        data.add(next(y))
    except StopIteration:
        break
print(data)
output=dataScreening(data,"i<80","i>30")
print("result 2")
print(output)
data=set()
z=dataSampling(str,string.printable,20)
while True:
    try:
        data.add(next(z))
    except StopIteration:
        break
print(data)
output=dataScreening(data,"i.find('a')!=-1")
print("result 3")
print(output)

