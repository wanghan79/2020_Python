
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

def ran(t):
    if t == 1:
        ret = randomInt(0,100)
        print(ret)
    
    elif t == 2:
        ret = randomDouble(1.5,3.8)
        print(ret)

    elif t == 3:
        ret = randomStr(10)
        print(ret)


ran(1)
ran(2)
ran(3)