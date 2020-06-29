import random
import string

def DataSampling(datatype, datarange, num, strlen=8):
    for index in range(0,num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it),next(it))
            yield item
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it),next(it))
            yield item
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            yield item
            continue
        else:
            continue

def DataScreening(data,condition):
    for i in data:
        if type(i) is int:
            if i>=condition[0] and i<=condition[1]:
                yield i
        if type(i) is float:
            if i>=condition[0] and i<=condition[1]:
                yield i
        if type(i) is str:
            for item in condition:
                if item in i:
                    yield i

result_int1 = set()
result_int2 = set()
for x in DataSampling(int,[0,200],100):
    result_int1.add(x)
print(result_int1)
for y in DataScreening(result_int1,(0,100)):
    result_int2.add(y)
print(result_int2)


result_float1 = set()
result_float2 = set()
for x in DataSampling(float,[0,100],100):
    result_float1.add(x)
print(result_float1)
for y in DataScreening(result_float1,(10,50)):
    result_float2.add(y)
print(result_float2)


result_str1 = set()
result_str2 = set()
for x in DataSampling(str,string.ascii_letters+string.digits,100,20):
    result_str1.add(x)
print(result_str1)
for y in DataScreening(result_str1,('in','out','1')):
    result_str2.add(y)
print(result_str2)
