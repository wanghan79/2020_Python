import random
import string

#随机数生成器
def randnum(dtype, count,d,u):
    list1=[]
    if dtype == int:
        for i in range(0,count):
            list1.append(random.randint(d,u))
        print((list1))
        return  list1
    elif dtype == float:
        for i in range(count):
            list1.append(random.uniform(d,u))
        print((list1))
        return list1
    elif dtype == str:
        for i in range(0,count):
            a= ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
            list1.append(a)
        print(list1)
        return list1

#筛选器
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

def test():
    pass
    #随机生成整数，再筛选
    list2=randnum(int,100 ,0,120)
    slect(int,list2,60,120,list2)
    #随机生成浮点数，再筛选
    list2=randnum(float, 20,0,300)
    slect(float,list2,100,200,list2)
    #随机生成字符串，再筛选
    list2=randnum(str,2000,None,None)
    slect(str,list2,"az")

if __name__ == '__main__':
     test()
