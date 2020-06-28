import random
import string

def generator(dtype, count,d,u):
    i=0
    while i<=count:
        if dtype == int:
            yield random.randint(d, u)
        elif dtype == float:
            yield  random.uniform(d, u)
        elif dtype == str:
            yield ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
        i+=1
def slect(dtype,list1,*con):
    if dtype==int or dtype==float:
        a=0
        for i in range (0,len(list1)):
            if list1[i-a] < con[0] or list1[i-a]>con[1]:
                del list1[i-a]
                a+=1
        print(list1)
        list1.clear()
    elif dtype==str:
        a = 0
        for i in range(0, len(list1)):
            if con[0] not in list1[i-a]:
                del list1[i-a]
                a+=1
        print(list1)

list1=[]
#整数生成器
int_it=generator(int,20,0,120)
for i in int_it:
    list1.append(i)
print(list1)
slect(int,list1,60,120)
#浮点数生成器
float_it=generator(float,20,0.0,120)
for i in float_it:
    list1.append(i)
print(list1)
slect(float,list1,60,120)
#字符串生成器
str_it=generator(str,2000,None,None)
for i in str_it:
    list1.append(i)
print(list1)
slect(str,list1,"ak")

