import random

def decorator1(func):
    def Work(a,b):
        print("this decorator1 is worked")
        return func(a,b)
    return Work

def decorator2(func):
    def Work(maxlen):
        print("this decorator2 is worked")
        return func(maxlen)
    return Work

@decorator1
def randomInt(minnum,maxnum):
    return random.randint(minnum,maxnum)

@decorator1
def randomDouble(minnum,maxnum):
    return random.uniform(minnum,maxnum)

@decorator2
def randomStr(maxlen):
    s = ''
    ch = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(maxlen):
        index = random.randint(0,len(ch) - 1)
        s = s + ch[index]
    return s

print(randomInt(1,100))
print(randomDouble(3.5,4.8))
print(randomStr(50))