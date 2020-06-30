import random

def use_logging(func):
    def Generate(x, y):
        a = random.randint(x, y)
        b = random.uniform(x, y)
        c = ["Romance", "of", "the", "Three", "Kingdoms"]
        random.shuffle(c)
        print(a)
        print(b)
        print(c)
        print("正在运行的函数:",func.__name__)
        return func(a,b,c,x,y)
    return Generate


@use_logging
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
Datascreening(x, y)