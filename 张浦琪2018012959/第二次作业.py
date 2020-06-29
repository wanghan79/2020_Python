import random

def ModifiedRandom1(func):
    def Work(a,b,c,d):
        print("this modified is worked")
        return func(a,b,c,d)
    return Work

def ModifiedRandom2(func):
    def Work():
        print("this modified is worked")
        return func()
    return Work


@ModifiedRandom1
def RandomInt(a,b,c,d):
    ran=random.randint(a,b)
    #生成a到b之间的随机整数
    if c<=ran<=d:
        return "%s   yes"%ran
    else:
        return "%s   no" %ran

@ModifiedRandom1
def RandomFloat(a,b,c,d):
    ran=random.uniform(a,b)
    #生成a-b之间的随机浮点数
    if c <= ran <= d:
        return "%s   yes" %ran
    else:
        return "%s   no" %ran

@ModifiedRandom2
def RandomStr():
    str='abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
    ch = random.choice(str)
    if 'a' <= ch <= 'z':
        return "%s   yes" %ch
    else:
        return "%s   no" %ch

print(RandomInt(1,100,5,20)) #生成1-100之间的随机整数输出并判断是否在5-20区间内
print(RandomFloat(1,100,5,20)) #生成1-100之间的随机浮点数输出并判断是否在5-20区间内
print(RandomStr()) #生成随机字符输出并判断是否在a-z区间内