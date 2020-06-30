
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

result1 = []
for i in range(5):
    ret = randomInt(1,200)
    result1.append(ret)
results1s = dataScreening(result1, 10, 100)
print(results1s)

result2 = []
for i in range(5):
    ret = randomDouble(0.1,100.0)
    result2.append(ret)
results2s = dataScreening(result2, 9.9, 89.9)
print(results2s)

result3 = []
for i in range(5):
    s = randomStr(10)
    result3.append(s)

results3s = dataScreening(result3,'o')
print(results3s)