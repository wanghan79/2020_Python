import random
import string

def randnum(fun):
    def wrap(dtype, count,d,u,*con):
        list1 = []
        str1 = ""
        if dtype == int:
            for i in range(0, count):
                list1.append(random.randint(d, u))
            print((list1))
            fun(dtype,list1,*con)
        elif dtype == float:
            for i in range(count):
                list1.append(random.uniform(d, u))
            print((list1))
            fun(dtype,list1,*con)
        elif dtype == str:
            for i in range(0, count):
                a = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
                list1.append(a)
            print(list1)
            fun(dtype, list1, *con)
    return wrap

@randnum
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
    slect(int,100 ,0,120,5,50)
    slect(float,20 ,10,20,15,20)
    slect(str,200,None,None,"aj")

if __name__ == '__main__':
    test()
